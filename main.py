import os
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pickle
import calc
import pandas as pd
import sklearn

class InheritanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inheritance Calculator")

        # Dapatkan path direktori dari file yang sedang dieksekusi
        self.base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

        self.model = self.load_model("id3_without_pruning_model.pkl")

        self.create_widgets()
        self.center_window()

    def load_model(self, filename):
        # Gabungkan path direktori dengan nama file
        file_path = os.path.join(self.base_path, filename)
        with open(file_path, 'rb') as file:
            models = pickle.load(file)
        return models

    def create_widgets(self):
        # Define fonts
        self.default_font = ("Helvetica", 9)
        self.label_font = ("Helvetica", 9, "bold")
        self.result_font = ("Helvetica", 9)

        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Configure grid for root and main_frame to ensure resizing behavior
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(21, weight=1)  # Ensure the last row (result frame) grows
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)  # Added for the result frame

        # Title
        instruction_label = ttk.Label(main_frame, text="PEMBAGIAN WARIS MENURUT HUKUM ISLAM", font=(self.label_font[0], 14, "bold"))
        instruction_label.grid(row=0, column=0, columnspan=3, pady=(0, 10), padx=7, sticky="n")

        # Input fields
        self.create_custom_label(main_frame, "Total harta kepemilikan*:", 2)
        self.total_assets = self.create_entry(main_frame, 2)

        self.create_custom_label(main_frame, "Total hutang*:", 3)
        self.total_debts = self.create_entry(main_frame, 3)

        self.create_custom_label(main_frame, "Total wasiat*:", 4)
        self.will = self.create_entry(main_frame, 4)

        self.create_custom_label(main_frame, "Biaya perawatan selama sakit*:", 5)
        self.medical_expenses = self.create_entry(main_frame, 5)

        self.create_custom_label(main_frame, "Biaya pengurusan jenazah*:", 6)
        self.funeral_expenses = self.create_entry(main_frame, 6)

        # Family member inputs
        self.family_members = {}
        family_labels = {
            "ap": "Anak perempuan",
            "al": "Anak laki-laki",
            "cp": "Cucu perempuan",
            "cl": "Cucu laki-laki",
            "suami": "Suami",
            "istri": "Istri",
            "ayah": "Ayah",
            "ibu": "Ibu",
            "kakek": "Kakek",
            "nenek": "Nenek",
            "si": "Saudara seibu",
            "sdlk": "Saudara laki-laki kandung",
            "sdpk": "Saudara perempuan kandung"
        }

        for i, (key, label) in enumerate(family_labels.items()):
            self.create_custom_label(main_frame, f"Jumlah {label}*:", 7 + i)
            self.family_members[key] = self.create_entry(main_frame, 7 + i)

        # Add asterisk information label
        asterisk_info_label = ttk.Label(main_frame, text="Kolom yang bertanda bintang (*) wajib diisi. Jika tidak ada tanggungan atau anggota keluarga, isi dengan 0.", font=self.default_font, foreground='red')
        asterisk_info_label.grid(row=20, column=0, columnspan=2, pady=10, sticky=tk.W)

        # Calculate button
        self.calculate_button = ttk.Button(main_frame, text="Calculate", command=self.calculate_inheritance, style='TButton')
        self.calculate_button.grid(row=21, column=0, columnspan=2, pady=5)

        # Result label
        result_label = ttk.Label(main_frame, text="Hasil Perhitungan:", font=self.label_font)
        result_label.grid(row=1, column=2, pady=(0, 10), padx=7, sticky="n")

        # Result display
        result_frame = ttk.Frame(main_frame)
        result_frame.grid(row=2, column=2, rowspan=18, pady=5, padx=7, sticky=(tk.N, tk.S, tk.E, tk.W))
        result_frame.grid_rowconfigure(0, weight=1)
        result_frame.grid_columnconfigure(0, weight=1)

        self.result_text = tk.Text(result_frame, height=30, width=30, font=self.result_font, wrap=tk.WORD)
        self.result_text.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Add scrollbar to the result text
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Configure styles
        style = ttk.Style()
        style.configure('TButton', font=self.default_font)
        style.configure('TLabel', font=self.label_font)
        style.configure('TEntry', font=self.default_font)

    def create_custom_label(self, parent, text, row):
        # Memisahkan Teks Label dan Asterisk
        label_text, asterisk = text.split('*')

        # Membuat Frame untuk Label
        label_frame = ttk.Frame(parent)
        label_frame.grid(row=row, column=0, pady=2, padx=(7, 20), sticky=tk.E)

        # Membuat dan Menambahkan Label Teks
        label = ttk.Label(label_frame, text=label_text, font=self.label_font)
        label.pack(side=tk.LEFT)

        # Membuat dan Menambahkan Label Asterisk
        asterisk_label = ttk.Label(label_frame, text='*', font=self.label_font, foreground='red')
        asterisk_label.pack(side=tk.LEFT)

    def create_entry(self, parent, row):
        # Membuat Entry Widget
        entry = ttk.Entry(parent, font=self.default_font, width=20)

        # Menempatkan Entry dalam Grid Layout
        entry.grid(row=row, column=1, pady=2, padx=(20, 7), sticky=tk.W)
        return entry

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def predict_inheritance(self, predictors, dt_model):
        feature_names = ['total_ap', 'total_al', 'total_cp', 'total_cl', 'total_suami', 'total_istri', 
                            'total_ayah', 'total_ibu', 'total_kakek', 'total_nenek', 'total_si', 
                            'total_sdlk', 'total_sdpk']
        
        predictors_df = pd.DataFrame([predictors], columns=feature_names)
        model = dt_model['model']

        # Memprediksi Probabilitas
        prediction_proba = model.predict_proba(predictors_df)[0]
        
        return 'TIDAK DAPAT' if prediction_proba[1] >= 0.5 else 'DAPAT'
    
    def calculate_inheritance(self):
        # Collect the input fields to check
        input_fields = [
            ("Total harta kepemilikan", self.total_assets),
            ("Total hutang", self.total_debts),
            ("Total wasiat", self.will),
            ("Biaya perawatan selama sakit", self.medical_expenses),
            ("Biaya pengurusan jenazah", self.funeral_expenses)
        ]
        
        family_labels = {
            "ap": "anak perempuan",
            "al": "anak laki-laki",
            "cp": "cucu perempuan",
            "cl": "cucu laki-laki",
            "suami": "suami",
            "istri": "istri",
            "ayah": "ayah",
            "ibu": "ibu",
            "kakek": "kakek",
            "nenek": "nenek",
            "si": "saudara seibu",
            "sdlk": "saudara laki-laki kandung",
            "sdpk": "saudara perempuan kandung"
        }

        for key, label in family_labels.items():
            input_fields.append((f"Jumlah {label}", self.family_members[key]))

        # Validate the inputs
        invalid_fields = []
        non_numeric_fields = []
        for label, field in input_fields:
            if not field.get():
                invalid_fields.append(label)
            else:
                try:
                    float(field.get())
                except ValueError:
                    non_numeric_fields.append(label)

        if invalid_fields:
            invalid_fields_str = ", ".join(invalid_fields)
            messagebox.showerror("Input Error", f"Semua kolom harus diisi! {invalid_fields_str} belum terisi.")
            return

        if non_numeric_fields:
            non_numeric_fields_str = ", ".join(non_numeric_fields)
            messagebox.showerror("Input Error", f"Kolom berikut harus diisi dengan angka yang valid: {non_numeric_fields_str}.")
            return

        # Check if both suami and istri are filled
        if float(self.family_members["suami"].get()) > 0 and float(self.family_members["istri"].get()) > 0:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Pilih salah satu antara suami atau istri! Tidak boleh pilih keduanya.\n", 'error')
            self.result_text.tag_config('error', foreground='red')
            return

        # Proceed with the calculation if all inputs are valid
        total_assets = float(self.total_assets.get())
        total_debts = float(self.total_debts.get())
        will = float(self.will.get())
        medical_expenses = float(self.medical_expenses.get())
        funeral_expenses = float(self.funeral_expenses.get())

        if will > (total_assets / 3):
            messagebox.showerror("Input Error", "Wasiat tidak boleh lebih dari 1/3 bagian dari total harta kepemilikan!")
            self.will.focus_set()
            return
        
        family_members = {f"total_{key}": float(self.family_members[key].get()) for key in self.family_members}
        
        total_inheritance = total_assets - total_debts - will - medical_expenses - funeral_expenses
        
        # Check if the total of debts, will, medical expenses, and funeral expenses exceeds total assets
        if total_debts + will + medical_expenses + funeral_expenses > total_assets:
            total_inheritance = 0
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Tidak ada harta waris yang dapat dibagi. Tanggungan yang harus dibayar melebihi total harta yang dimiliki, tolong selesaikan permasalahan tersebut dahulu.", 'error')
            self.result_text.tag_config('error', foreground='red')
            return

        inheritance_status = {}
        
        feature_names = ['total_ap', 'total_al', 'total_cp', 'total_cl', 'total_suami', 'total_istri', 
                        'total_ayah', 'total_ibu', 'total_kakek', 'total_nenek', 'total_si', 
                        'total_sdlk', 'total_sdpk']
        predictors = [family_members[feature] for feature in feature_names]
        
        # Iterasi melalui Anggota Keluarga
        for relationship, _ in family_members.items():
            if relationship.startswith("total_"):
                prediction_key = relationship.replace("total_", "hw_")
                if prediction_key not in self.model:
                    messagebox.showerror("Model Error", f"No model found for {prediction_key}")
                    continue
                
                prediction = self.predict_inheritance(predictors, self.model[prediction_key])
                inheritance_status[relationship] = prediction
        
        self.display_results(total_inheritance, inheritance_status, family_members)
    
    def display_results(self, total_inheritance, inheritance_status, family_members):
        # Membersihkan dan Mengisi result_text
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Total harta warisan yang dibagi: {total_inheritance}\n")
        self.result_text.insert(tk.END, "Bagian masing-masing ahli waris:\n")

        # Mengambil Nilai dari family_members
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

        # Menghitung dan Menampilkan Bagian Warisan
        for relationship, status in inheritance_status.items():
            if relationship == "total_suami" and status == "DAPAT":
                share_suami = calc.hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
                self.result_text.insert(tk.END, f"Suami: {share_suami:.2f}\n")
            if relationship == "total_istri" and status == "DAPAT":
                share_istri = calc.hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
                self.result_text.insert(tk.END, f"Istri: {share_istri:.2f}\n")
            if relationship == "total_ayah" and status == "DAPAT":
                share_ayah = calc.hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
                self.result_text.insert(tk.END, f"Ayah: {share_ayah:.2f}\n")
            if relationship == "total_ibu" and status == "DAPAT":
                share_ibu = calc.hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
                self.result_text.insert(tk.END, f"Ibu: {share_ibu:.2f}\n")
            if relationship == "total_kakek" and status == "DAPAT":
                share_kakek = calc.hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
                self.result_text.insert(tk.END, f"Kakek: {share_kakek:.2f}\n")
            if relationship == "total_nenek" and status == "DAPAT":
                share_nenek = calc.hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
                self.result_text.insert(tk.END, f"Nenek: {share_nenek:.2f}\n")
            if relationship == "total_al" and status == "DAPAT":  # Anak laki-laki
                share_al = calc.hitung_bagian_anak_laki(anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek)
                self.result_text.insert(tk.END, f"Anak laki-laki: {share_al:.2f}\n")
            if relationship == "total_ap" and status == "DAPAT":  # Anak perempuan
                share_ap = calc.hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung)
                self.result_text.insert(tk.END, f"Anak perempuan: {share_ap:.2f}\n")
            if relationship == "total_cl" and status == "DAPAT":  # Cucu laki-laki dari anak laki-laki
                share_cl = calc.hitung_bagian_cucu_laki(cucu_laki, anak_laki, cucu_perempuan, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
                self.result_text.insert(tk.END, f"Cucu laki-laki: {share_cl:.2f}\n")
            if relationship == "total_cp" and status == "DAPAT":  # Cucu perempuan dari anak laki-laki
                share_cp = calc.hitung_bagian_cucu_perempuan(cucu_perempuan, cucu_laki, anak_laki, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
                self.result_text.insert(tk.END, f"Cucu perempuan: {share_cp:.2f}\n")
            if relationship == "total_si" and status == "DAPAT":  # Saudara seibu
                share_si = calc.hitung_bagian_si(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, saudara_seibu, ayah, kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_laki_kandung, saudara_perempuan_kandung)           
                self.result_text.insert(tk.END, f"Saudara seibu: {share_si:.2f}\n")
            if relationship == "total_sdlk" and status == "DAPAT": # Saudara kandung laki-laki
                share_sdlk = calc.hitung_bagian_sdlk(total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_ap, share_cp, share_si, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan)
                self.result_text.insert(tk.END, f"Saudara laki-laki kandung: {share_sdlk:.2f}\n")
            if relationship == "total_sdpk" and status == "DAPAT": # Saudara kandung perempuan
                share_sdpk = calc.hitung_bagian_sdpk(total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_ap, share_cp, share_si, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan) 
                self.result_text.insert(tk.END, f"Saudara perempuan kandung: {share_sdpk:.2f}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("950x630")  # Adjusted window size for better fit
    app = InheritanceApp(root)
    root.mainloop()
