import sqlite3

# Connect to SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect('diabetes_prediction.db')
c = conn.cursor()

# Create a table to store patient predictions
c.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        pregnancies INTEGER,
        glucose INTEGER,
        blood_pressure INTEGER,
        skin_thickness INTEGER,
        insulin INTEGER,
        bmi REAL,
        dpf REAL,
        age INTEGER,
        prediction_result TEXT
    )
''')

conn.commit()
conn.close()
