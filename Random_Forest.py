import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('Data_Seluruh_Gangguan.csv')

# Definisi fitur (X) dan target (y)
X = data[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 
          'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 
          'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25']]
y = data[['Level Kecemasan', 'Level Depresi', 'Level Bipolar', 'Level Skizofrenia', 'Level OCD']]

# Split dataset menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Bagian 2: Latih model Random Forest ---
# Definisi model Random Forest untuk setiap label
models = {}
for column in y.columns:
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train[column])
    models[column] = rf

# Prediksi dan evaluasi
y_pred = pd.DataFrame()
for column in y.columns:
    y_pred[column] = models[column].predict(X_test)

# Evaluasi model
for column in y.columns:
    print(f"Classification Report untuk {column}:")
    print(classification_report(y_test[column], y_pred[column]))
    print(f"Accuracy untuk {column}: {accuracy_score(y_test[column], y_pred[column])}\n")

import joblib

# Simpan seluruh model Random Forest dalam satu file
joblib.dump(models, 'rf_models_all_labels.pkl')

print("Seluruh model disimpan dengan sukses!")

