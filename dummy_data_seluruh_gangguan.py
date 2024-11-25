from faker import Faker
import random
import csv
import pandas as pd

fake = Faker()

data = pd.read_csv('Data_Kecemasan.csv')
for record in data:
    print(record)
    def calculate_level(q1, q2, q3, q4, q5):
        total_score = q1 + q2 + q3 + q4 + q5
        if total_score <= 5:
            return 1
        elif total_score <= 10:
            return 2
        else:
            return 3

    def generate_dummy_data(num_records):
        data = []
        for _ in range(num_records):
            q1 = random.randint(1, 3)
            q2 = 1
            q3 = random.randint(1, 3)
            q4 = random.randint(1, 2)
            q5 = random.randint(1, 3)
            q6 = random.randint(1, 3)
            q7 = 1
            q8 = random.randint(1, 3)
            q9 = random.randint(1, 2)
            q10 = random.randint(1, 3)
            q11 = random.randint(1, 3)
            q12 = 1
            q13 = random.randint(1, 3)
            q14 = random.randint(1, 2)
            q15 = random.randint(1, 3)
            q16 = random.randint(1, 3)
            q17 = 1
            q18 = random.randint(1, 3)
            q19 = random.randint(1, 2)
            q20 = random.randint(1, 3)
            q21 = 1
            q22 = random.randint(1, 3)
            q23 = random.randint(1, 3)
            q24 = random.randint(1, 2)
            q25 = random.randint(1, 3)
            level_kecemasan = calculate_level(q1, q2, q3, q4, q5)
            level_depresi = calculate_level(q6, q7, q8, q9, q10)
            level_bipolar = calculate_level(q11, q12, q13, q14, q15)
            level_skizofrenia = calculate_level(q16, q17, q18, q19, q20)
            level_OCD = calculate_level(q21, q22, q23, q24, q25)
            record = {
                'name': fake.name(),
                'Q1': q1,
                'Q2': q2,
                'Q3': q3,
                'Q4': q4,
                'Q5': q5,
                'Q6': q6,
                'Q7': q7,
                'Q8': q8,
                'Q9': q9,
                'Q10': q10,
                'Q11': q11,
                'Q12': q12,
                'Q13': q13,
                'Q14': q14,
                'Q15': q15,
                'Q16': q16,
                'Q17': q17,
                'Q18': q18,
                'Q19': q19,
                'Q20': q20,
                'Q21': q21,
                'Q22': q22,
                'Q23': q23,
                'Q24': q24,
                'Q25': q25,
                'Level Kecemasan': level_kecemasan,
                'Level Depresi': level_depresi,
                'Level Bipolar': level_bipolar,
                'Level Skizofrenia': level_skizofrenia,
                'Level OCD': level_OCD
            }
            data.append(record)
        return data

    # Generate 10,000 dummy records
    dummy_data = generate_dummy_data(25000)
    df = pd.DataFrame(dummy_data)

    # Save the data to an Excel file
    df.to_csv('Data_Seluruh_Gangguan.csv', index=False)
   
        
            