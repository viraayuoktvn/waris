import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Baca dataset
data = pd.read_csv("aauji.csv", delimiter=';')

# Pisahkan variabel target dan variabel prediktor untuk setiap variabel target
targets = ['hw_ap', 'hw_al', 'hw_cl', 'hw_cp', 'hw_suami', 'hw_istri', 'hw_ayah', 'hw_ibu', 'hw_kakek', 'hw_nenek', 'hw_si', 'hw_sdlk', 'hw_sdpk']
predictors = ['total_hw', 'total_ap', 'total_al', 'total_cl', 'total_cp', 'total_suami', 'total_istri', 'total_ayah', 'total_ibu', 'total_kakek', 'total_nenek', 'total_si', 'total_sdlk', 'total_sdpk']

# Lakukan iterasi untuk setiap variabel target
for target in targets:
    # Pisahkan variabel target dan variabel prediktor
    X = data[predictors]
    y = data[target]
    
    # Bagi data menjadi set pelatihan dan pengujian
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Inisialisasi dan latih model CART
    model = DecisionTreeRegressor(max_depth=5, min_samples_leaf=10)  # Atur parameter sesuai kebutuhan
    model.fit(X_train, y_train)
    
    # Lakukan prediksi pada set pengujian
    y_pred = model.predict(X_test)
    
    # Hitung mean squared error (MSE)
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error for {}: {:.2f}".format(target, mse))
