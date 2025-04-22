# cd "C:\Users\aryan\Downloads\project of ml"

# cd "C:\Users\aryan\Downloads\New folder"


# streamlit run app.py

# browser will open automatically


import pickle

# Save the model and scaler as a tuple
with open("diabetes_model.pkl", "wb") as file:
    pickle.dump((model, scaler), file)

print("✅ Model saved successfully as 'diabetes_model.pkl'")
