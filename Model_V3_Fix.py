import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras import layers, models
import joblib

# Load dataset
data = pd.read_csv('Data_Seluruh_Gangguan.csv')

# Definisi fitur (X) dan target (y)
X = data[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 
          'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 
          'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25']]
y = data[['Level Kecemasan', 'Level Depresi', 'Level Bipolar', 'Level Skizofrenia', 'Level OCD']]

# Split dataset menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Bagian 1: Latih model TensorFlow untuk semua label sekaligus ---
# Normalisasi data
X_train_norm = X_train / X_train.max()
X_test_norm = X_test / X_train.max()

# Ubah target menjadi array numpy
y_train_np = y_train.to_numpy()
y_test_np = y_test.to_numpy()

# Definisi model TensorFlow untuk semua label
model = models.Sequential([
    layers.Dense(64, activation='relu', input_dim=X_train.shape[1]),
    layers.Dense(32, activation='relu'),
    layers.Dense(y_train.shape[1], activation='sigmoid')  # Output multi-class dengan sigmoid
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training model
history = model.fit(X_train_norm, y_train_np, epochs=10, batch_size=32, verbose=1)

# Prediksi dan evaluasi model TensorFlow
y_pred_tf = model.predict(X_test_norm)

# Konversi hasil prediksi ke biner (0/1)
y_pred_tf_binary = (y_pred_tf > 0.5).astype(int)

# Evaluasi model
for i, column in enumerate(y.columns):
    print(f"Classification Report untuk {column} (TensorFlow):")
    print(classification_report(y_test_np[:, i], y_pred_tf_binary[:, i]))
    print(f"Accuracy untuk {column} (TensorFlow): {accuracy_score(y_test_np[:, i], y_pred_tf_binary[:, i])}\n")

# Simpan model TensorFlow
model.save('tf_model_multi_output.h5')

print("Model TensorFlow multi-output disimpan dengan sukses!")

# --- Bagian 2: Latih model Random Forest setelah TensorFlow ---
# Definisi model Random Forest untuk setiap label
rf_models = {}
for column in y.columns:
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train[column])
    rf_models[column] = rf


# Prediksi dan evaluasi dengan Random Forest
y_pred_rf = pd.DataFrame()
for column in y.columns:
    y_pred_rf[column] = rf_models[column].predict(X_test)

# Evaluasi model Random Forest
for column in y.columns:
    print(f"Classification Report untuk {column} (Random Forest):")
    print(classification_report(y_test[column], y_pred_rf[column]))
    print(f"Accuracy untuk {column} (Random Forest): {accuracy_score(y_test[column], y_pred_rf[column])}\n")

# Simpan seluruh model TensorFlow dan Random Forest dalam satu file
joblib.dump(rf_models, 'rf_models_all_labels_V2.pkl')

# # Simpan seluruh model TensorFlow dalam satu file
# for column, model in tensorflow_models.items():
#     model.save(f'tf_model_{column}.h5')

print("Seluruh model disimpan dengan sukses!")
