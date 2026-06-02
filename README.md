# 🏥 Health Prediction App (Flask + ML)

This is a simple **Health Prediction Web Application** built using **Flask, SQLite, and Machine Learning (Scikit-learn)**.  
The system predicts possible health risks based on patient blood test data.

---

## 🚀 Features

- ➕ Add new patient records
- 📄 View all patient records
- ✏️ Edit patient details
- ❌ Delete patient records
- 🤖 AI/ML-based health prediction (Remarks generation)
- 💾 SQLite database storage
- 🎨 Simple Bootstrap UI

---

## 🧠 Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Scikit-learn (Decision Tree ML Model)
- HTML, CSS, Bootstrap

---

## 📊 Input Fields

- Full Name
- Date of Birth
- Email
- Glucose
- Haemoglobin
- Cholesterol

---

## 🤖 ML Prediction Logic

The system predicts health conditions such as:

- High Risk of Diabetes
- High Cholesterol Risk
- Possible Anemia
- Normal Health Indicators

---

## ⚙️ How to Run Project

```bash
pip install -r requirements.txt
python app.py


The open
http://127.0.0.1:5000/

health_prediction_app/
│
├── app.py
├── models.py
├── ml_model.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── add_patient.html
│   └── edit_patient.html
│
└── static/
    └── style.css
