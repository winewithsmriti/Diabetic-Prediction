🩺 Diabetes Prediction Using Machine Learning

This project is a web-based application that predicts whether a person is likely to have diabetes based on various health parameters. It uses machine learning techniques for prediction and is deployed using Streamlit for easy access and interaction.

📌 Project Overview

Early detection of diabetes is crucial for timely treatment and lifestyle adjustments. This project aims to assist individuals and medical professionals by providing a quick, data-driven diabetes prediction tool.

🚀 Features

- User-friendly interface built with Streamlit
- Accepts input for health-related parameters
- Predicts the likelihood of diabetes using trained ML models
- Uses preprocessed and cleaned dataset for accurate results
- Saves the best-performing model using `joblib`
- Connected to SQLite database to store user input and predictions

📊 Dataset

The dataset used in this project is the Pima Indians Diabetes Dataset, which is publicly available on platforms like Kaggle or UCI Machine Learning Repository.

Features used:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

⚙️ Technologies Used

- Python 🐍
- Pandas & NumPy – Data manipulation
- Matplotlib & Seaborn – Data visualization
- Scikit-learn – Machine learning models and preprocessing
- Joblib – Model saving/loading
- Streamlit – Web app deployment
- SQLite – Database for storing input and results

🧠 Machine Learning Models

Multiple models were tested:
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

The best model was selected based on accuracy and performance metrics such as:
- Confusion Matrix
- Accuracy Score
- Precision, Recall, F1 Score

🧪 How to Run the Project
streamlit run app.py
diabetes-prediction/
│
├── app.py                  # Streamlit application
├── diabetes_model.pkl      # Trained model
├── scaler.pkl              # Scaler for preprocessing
├── diabetes.csv            # Dataset
├── Project.ipynb        # Python dependencies
├── setup_db.py             # SQLite database
└── README.md               # Project documentation



