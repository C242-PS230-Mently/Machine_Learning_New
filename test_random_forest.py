import pandas as pd
import joblib

# Memuat seluruh model dari file
models_loaded = joblib.load('Model_Fix_RF_TF.pkl')


# Misalnya, ingin melakukan prediksi untuk input baru
input_baru = pd.DataFrame({
    'Q1': [3], 'Q2': [2], 'Q3': [2], 'Q4': [2], 'Q5': [1],
    'Q6': [1], 'Q7': [1], 'Q8': [1], 'Q9': [1], 'Q10': [1],
    'Q11': [1], 'Q12': [1], 'Q13': [2], 'Q14': [2], 'Q15': [2],
    'Q16': [1], 'Q17': [1], 'Q18': [1], 'Q19': [1], 'Q20': [1],
    'Q21': [1], 'Q22': [1], 'Q23': [1], 'Q24': [1], 'Q25': [1]
})

# Melakukan prediksi untuk setiap gangguan
prediksi = {}
for gangguan in models_loaded.keys():
    model = models_loaded[gangguan]
    prediksi[gangguan] = model.predict(input_baru)[0]

# Menampilkan hasil prediksi untuk semua gangguan
for gangguan, hasil in prediksi.items():
    print(f"Prediksi {gangguan}: {hasil}")
