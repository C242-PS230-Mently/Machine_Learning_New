import tensorflow as tf
import tensorflow_decision_forests as tfdf
import pandas as pd
import joblib

# Load dataset
data = pd.read_csv('Data_Seluruh_Gangguan.csv')

# Define features (X) and targets (y)
X = data[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 
          'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 
          'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25']]
y = data[['Level Kecemasan', 'Level Depresi', 'Level Bipolar', 'Level Skizofrenia', 'Level OCD']]

# Combine X and y into a single dataframe for TensorFlow Decision Forests
data_combined = X.copy()
data_combined[['Level Kecemasan', 'Level Depresi', 'Level Bipolar', 'Level Skizofrenia', 'Level OCD']] = y

# Initialize an empty dictionary to store models
models = {}

# Loop through all target labels and train a model for each
for column in y.columns:
    print(f"Training model for {column}...")
    
    # Convert dataset to TensorFlow dataset
    train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(data_combined, label=column)
    test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(data_combined, label=column)
    
    # Initialize and train Random Forest model
    model = tfdf.keras.RandomForestModel()
    model.fit(train_ds)
    
    # Evaluate model
    model.compile(metrics=["accuracy"])
    accuracy = model.evaluate(test_ds, return_dict=True)
    print(f"Accuracy for {column}: {accuracy['accuracy']}")
    
    # Add the trained model to the models dictionary
    models[column] = model

# Save the dictionary of models into a single .pkl file
joblib.dump(models, 'model_all_gangguan.pkl')

print("All models have been trained and saved into 'model_all_gangguan.pkl' successfully!")
