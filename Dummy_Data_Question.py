from faker import Faker
import pandas as pd

# Initialize Faker instance
fake = Faker()

# Define the possible answers for each question (Tidak Pernah, Kadang-Kadang, Sering)
answers = ["Tidak Pernah", "Kadang-Kadang", "Sering"]

# Create a list of questions for each section
questions = {
    "Kecemasan": [
        "Apakah Anda sering merasa khawatir berlebihan terhadap situasi yang belum terjadi?",
        "Apakah Anda merasa sulit untuk bersantai karena pikiran terus berputar?",
        "Apakah Anda merasa gugup atau takut saat berada di tempat umum?",
        "Apakah Anda sering merasa tidak yakin dengan kemampuan Anda dalam menghadapi tantangan hidup?",
        "Apakah Anda merasa tegang atau sulit tidur karena pikiran yang mengganggu?"
    ],
    "Depresi": [
        "Apakah Anda sering merasa kehilangan minat atau kesenangan dalam melakukan aktivitas sehari-hari?",
        "Apakah Anda merasa lelah atau tidak bertenaga meskipun tidak melakukan aktivitas berat?",
        "Apakah Anda merasa sedih atau hampa dalam waktu yang cukup lama?",
        "Apakah Anda merasa sulit untuk berkonsentrasi pada pekerjaan atau kegiatan Anda?",
        "Apakah Anda sering merasa tidak berarti atau putus asa?"
    ],
    "Bipolar": [
        "Apakah Anda pernah merasa sangat bersemangat dan penuh energi, lalu tiba-tiba merasa sangat sedih tanpa alasan yang jelas?",
        "Apakah Anda merasa memiliki periode di mana Anda berbicara atau berpikir lebih cepat dari biasanya?",
        "Apakah Anda mengalami perubahan drastis dalam pola tidur, seperti tidak bisa tidur selama beberapa hari?",
        "Apakah Anda merasa sangat percaya diri dalam satu waktu, lalu merasa sangat rendah diri di waktu lain?",
        "Apakah Anda pernah mengambil keputusan impulsif yang Anda sesali kemudian?"
    ],
    "Skizofrenia": [
        "Apakah Anda pernah merasa mendengar suara-suara yang orang lain tidak dengar?",
        "Apakah Anda merasa sulit untuk memahami atau menjelaskan pikiran Anda kepada orang lain?",
        "Apakah Anda merasa seseorang mengawasi atau mengendalikan Anda tanpa alasan yang jelas?",
        "Apakah Anda merasa sulit mengekspresikan emosi Anda atau merasa tidak memiliki emosi sama sekali?",
        "Apakah Anda merasa terpisah dari kenyataan atau memiliki pikiran yang tidak sesuai dengan dunia nyata?"
    ],
    "OCD": [
        "Apakah Anda merasa harus mengulangi suatu tindakan hingga merasa puas, seperti mencuci tangan atau memeriksa sesuatu?",
        "Apakah Anda memiliki pemikiran tertentu yang terus berulang dan sulit diabaikan?",
        "Apakah Anda merasa perlu mengatur barang-barang Anda dengan pola tertentu untuk merasa nyaman?",
        "Apakah Anda merasa khawatir bahwa sesuatu yang buruk akan terjadi jika Anda tidak melakukan sesuatu dengan cara tertentu?",
        "Apakah Anda merasa sulit untuk menghentikan atau mengontrol kebiasaan yang Anda tahu tidak diperlukan?"
    ]
}



# Function to generate random responses for each question with multiple answers
def generate_dummy_data_with_multiple_answers(questions, answers):
    data = []
    for section, qs in questions.items():
        for question in qs:
            for _ in range(3):  # Generate 3 answers for each question
                # Randomly select an answer from the possible answers
                answer = fake.random_element(answers)
                # Create a dummy response entry with fake name and answer
                data.append([fake.name(), section, question, answer])
    return data

# Generate dummy data with multiple answers
dummy_data = generate_dummy_data_with_multiple_answers(questions, answers)

# Create a DataFrame
df = pd.DataFrame(dummy_data, columns=["Name", "Section", "Question", "Answer"])

# Display the first few rows of the dummy data
df.head()

# Save the dummy data to an Excel file
df.to_excel("dummy_data_with_multiple_answers.xlsx", index=False)
# Ensure at least 500 rows of data
while len(df) < 500:
    additional_data = generate_dummy_data_with_multiple_answers(questions, answers)
    df = pd.concat([df, pd.DataFrame(additional_data, columns=["Name", "Section", "Question", "Answer"])])

# Reset index after concatenation
df.reset_index(drop=True, inplace=True)

# Display the first few rows of the dummy data
print(df.head())

# Save the dummy data to an Excel file
df.to_excel("dummy_data_with_multiple_answers.xlsx", index=False)


# Transform the data to have each question as a column
transformed_data = []
names = set(df["Name"])

for name in names:
    person_data = {"Name": name}
    for section, qs in questions.items():
        person_data[section] = section
        for question in qs:
            answer = df[(df["Name"] == name) & (df["Question"] == question)]["Answer"].values
            if len(answer) > 0:
                person_data[question] = answer[0]
            else:
                person_data[question] = None
    transformed_data.append(person_data)

# Create a new DataFrame with the transformed data
transformed_df = pd.DataFrame(transformed_data)

# Display the first few rows of the transformed data
print(transformed_df.head())

# Save the transformed data to an Excel file
transformed_df.to_excel("transformed_dummy_data.xlsx", index=False)
# Ensure all questions have answers for each person
transformed_data = []
names = set(df["Name"])

for name in names:
    person_data = {"Name": name}
    for section, qs in questions.items():
        person_data[section] = section
        for question in qs:
            answer = df[(df["Name"] == name) & (df["Question"] == question)]["Answer"].values
            if len(answer) > 0:
                person_data[question] = answer[0]
            else:
                # If no answer exists, randomly select one from the possible answers
                person_data[question] = fake.random_element(answers)
    transformed_data.append(person_data)

# Create a new DataFrame with the transformed data
transformed_df = pd.DataFrame(transformed_data)

# Display the first few rows of the transformed data
print(transformed_df.head())

# Save the transformed data to an Excel file
transformed_df.to_excel("transformed_dummy_data.xlsx", index=False)