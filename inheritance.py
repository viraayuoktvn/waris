import pandas as pd
import pickle
import calc

# Memuat model
def load_model(filename):
    with open(filename, 'rb') as file:
        models = pickle.load(file)
    return models

def predict_inheritance(predictors, dt_model):
    feature_names = ['total_ap', 'total_al', 'total_cp', 'total_cl', 'total_suami', 'total_istri', 
                     'total_ayah', 'total_ibu', 'total_kakek', 'total_nenek', 'total_si', 
                     'total_sdlk', 'total_sdpk']
    
    # Buat DataFrame dari predictors dengan nama kolom yang sesuai
    predictors_df = pd.DataFrame([predictors], columns=feature_names)
    
    model = dt_model['model']
    prediction_proba = model.predict_proba(predictors_df)[0]
    
    if prediction_proba[1] >= 0.5:
        prediction_string = 'TIDAK DAPAT'
    else:
        prediction_string = 'DAPAT'
    
    return prediction_string

# Menampilkan status warisan
def print_inheritance_status(inheritance_status):
    for relationship, status in inheritance_status.items():
        if status == "DAPAT":
            print(f"Status warisan untuk {relationship}: {status}")

# Fungsi untuk menghitung warisan
def calculate_inheritance(total_assets, total_debts, will, medical_expenses, funeral_expenses, family_members, dt_model):
    inheritance_status = {}
    total_inheritance = total_assets - total_debts - will - medical_expenses - funeral_expenses

    # Nama-nama fitur yang digunakan saat melatih model
    feature_names = ['total_ap', 'total_al', 'total_cp', 'total_cl', 'total_suami', 'total_istri', 
                     'total_ayah', 'total_ibu', 'total_kakek', 'total_nenek', 'total_si', 
                     'total_sdlk', 'total_sdpk']

    # Buat list dari family_members
    predictors = [family_members[feature] for feature in feature_names]

    for relationship, _ in family_members.items():
        if relationship.startswith("total_"):
            prediction_key = relationship.replace("total_", "hw_")
            if prediction_key not in dt_model:
                print(f"Error: No model found for {prediction_key}")
                continue
            
            # Panggil fungsi predict_inheritance dengan list sebagai input
            prediction = predict_inheritance(predictors, dt_model[prediction_key])
            inheritance_status[relationship] = prediction

    return total_inheritance, inheritance_status

def main():
    # Input data
    while True:
        try:
            total_assets = float(input("Total harta kepemilikan: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue
        break

    while True:
        try:
            total_debts = float(input("Total hutang: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue
        break

    print("Jumlah wasiat tidak boleh lebih dari 1/3 total harta kepemilikan.")
    while True:
        try:
            will = float(input("Total wasiat: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue

        if will > (total_assets / 3):
            print("Wasiat tidak boleh lebih dari 1/3 bagian dari total harta kepemilikan!")
            continue
        break

    while True:
        try:
            medical_expenses = float(input("Biaya perawatan selama sakit: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue
        break

    while True:
        try:
            funeral_expenses = float(input("Biaya pengurusan jenazah: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue
        break

    # Input jumlah dan nilai prediksi untuk setiap jenis anggota keluarga
    family_members = {}

    # Input jumlah anggota keluarga untuk masing-masing jenis hubungan
    print("Masukkan jumlah anggota keluarga yang masih hidup!")
    print("Untuk suami, istri, ayah, ibu, kakek, dan nenek masukkan 1 untuk ada dan 0 untuk tidak ada.")

    for relationship in ["ap", "al", "cp", "cl", "suami", "istri", "ayah", "ibu", "kakek", "nenek", "si", "sdlk", "sdpk"]:
        while True:
            try:
                family_members[f"total_{relationship}"] = float(input(f"Total {relationship}: "))
                break  # Keluar dari loop while setelah input valid
            except ValueError:
                print("Input tidak valid. Masukkan angka.")

    # dt_model = load_model("id3_without_pruning_model.pkl")
    dt_model = load_model("id3_without_pruning_model.pkl")
    
    total_inheritance, inheritance_status = calculate_inheritance(total_assets, total_debts, will, medical_expenses, funeral_expenses, family_members, dt_model)
    
    print_inheritance_status(inheritance_status)

    suami = family_members.get("total_suami", 0)
    istri = family_members.get("total_istri", 0)
    anak_laki = family_members.get("total_al", 0)
    anak_perempuan = family_members.get("total_ap", 0)
    cucu_laki = family_members.get("total_cl", 0)
    cucu_perempuan = family_members.get("total_cp", 0)
    ayah = family_members.get("total_ayah", 0)
    ibu = family_members.get("total_ibu", 0)
    kakek = family_members.get("total_kakek", 0)
    nenek = family_members.get("total_nenek", 0)
    saudara_seibu = family_members.get("total_si", 0)
    saudara_laki_kandung = family_members.get("total_sdlk", 0)
    saudara_perempuan_kandung = family_members.get("total_sdpk", 0)

    share_suami = 0
    share_istri = 0
    share_al = 0
    share_ap = 0
    share_cl = 0
    share_cp = 0
    share_ayah = 0
    share_ibu = 0
    share_kakek = 0
    share_nenek = 0
    share_si = 0
    share_sdlk = 0
    share_sdpk = 0

    print("Total harta warisan yang dibagi: ", total_inheritance)
    print("Bagian masing-masing ahli waris:")

    # Menampilkan status warisan
    for relationship, status in inheritance_status.items():
        if relationship == "total_suami" and status == "DAPAT":
            share_suami = calc.hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
            print("Suami: {:.2f}".format(share_suami))
        if relationship == "total_istri" and status == "DAPAT":
            share_istri = calc.hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
            print("Istri: {:.2f}".format(share_istri))
        if relationship == "total_ayah" and status == "DAPAT":
            share_ayah = calc.hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
            print("Ayah: {:.2f}".format(share_ayah))
        if relationship == "total_ibu" and status == "DAPAT":
            share_ibu = calc.hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
            print("Ibu: {:.2f}".format(share_ibu))
        if relationship == "total_kakek" and status == "DAPAT":
            share_kakek = calc.hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
            print("Kakek: {:.2f}".format(share_kakek))
        if relationship == "total_nenek" and status == "DAPAT":
            share_nenek = calc.hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
            print("Nenek: {:.2f}".format(share_nenek))
        if relationship == "total_al" and status == "DAPAT":  # Anak laki-laki
            share_al = calc.hitung_bagian_anak_laki(anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek)
            print("Anak laki-laki: {:.2f}".format(share_al))
        if relationship == "total_ap" and status == "DAPAT":  # Anak perempuan
            share_ap = calc.hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung)
            print("Anak perempuan: {:.2f}".format(share_ap))
        if relationship == "total_cl" and status == "DAPAT":  # Cucu laki-laki dari anak laki-laki
            share_cl = calc.hitung_bagian_cucu_laki(cucu_laki, anak_laki, cucu_perempuan, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
            print("Cucu laki-laki: {:.2f}".format(share_cl))
        if relationship == "total_cp" and status == "DAPAT":  # Cucu perempuan dari anak laki-laki
            share_cp = calc.hitung_bagian_cucu_perempuan(cucu_perempuan, cucu_laki, anak_laki, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
            print("Cucu perempuan: {:.2f}".format(share_cp))
        if relationship == "total_si" and status == "DAPAT":  # Saudara seibu
            share_si = calc.hitung_bagian_si(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, saudara_seibu, ayah, kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_laki_kandung, saudara_perempuan_kandung)           
            print("Saudara seibu: {:.2f}".format(share_si))
        if relationship == "total_sdlk" and status == "DAPAT": # Saudara kandung laki-laki
            share_sdlk = calc.hitung_bagian_sdlk(total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_ap, share_cp, share_si, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan)
            print("Saudara laki-laki kandung: {:.2f}".format(share_sdlk))
        if relationship == "total_sdpk" and status == "DAPAT": # Saudara kandung perempuan
            share_sdpk = calc.hitung_bagian_sdpk(total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_ap, share_cp, share_si, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan) 
            print("Saudara perempuan kandung: {:.2f}".format(share_sdpk))
if __name__ == "__main__":
    main()
