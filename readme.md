# 🩺 MedPlus Health Risk Predictor

An AI-powered healthcare risk prediction web application built with **Streamlit** that analyzes patient lifestyle and clinical measurements to estimate disease risk levels and provide preventive health recommendations.

The system uses a trained **Logistic Regression model** to predict whether a patient falls into:

* 🟢 Low Risk
* 🟠 Medium Risk
* 🔴 High Risk

It also generates a **medical report PDF** and allows users to **email the report automatically**.

---

## 🚀 Live Purpose

This application helps with:

✔ Early health risk screening
✔ Preventive care awareness
✔ Lifestyle improvement guidance
✔ Digital medical reporting
✔ Automated patient report sharing

It can be used for:

* Health awareness tools
* Academic ML projects
* Clinical demo systems
* Preventive care dashboards
* Telehealth support prototypes

---

## ✨ Features

### 🔍 Risk Prediction

* Machine learning based health risk classification
* Logistic Regression trained model
* Real-time prediction from patient inputs

### 📊 Clinical Input System

* Age
* Sleep duration
* Exercise level
* Family history
* Diet quality
* Blood pressure
* Glucose level
* Cholesterol
* Heart rate
* Waist circumference

### 🧠 Health Recommendation

Personalized guidance based on predicted risk level.

### 📄 Medical Report Generation

* Professional PDF report
* Patient information summary
* Clinical measurements
* Risk classification
* Preventive recommendations

### 📧 Automatic Email Delivery

* Sends report directly to patient email
* Secure SMTP email transfer
* PDF attachment included

### 🔄 Smart Reset System

* Clears all inputs safely
* Streamlit session-safe reset handling

### 🎨 Custom UI

* Background styling
* Structured layout
* Responsive design

---

## 🧠 Machine Learning Model

| Component     | Description                                   |
| ------------- | --------------------------------------------- |
| Algorithm     | Logistic Regression                           |
| Input Type    | Numerical + Encoded categorical               |
| Output        | Risk class (0,1,2)                            |
| Preprocessing | Feature scaling                               |
| Files         | `logistic_regression_model.pkl`, `scaler.pkl` |

---

## 🏗️ Project Structure

```
MedPlus-Health-Risk-Predictor/
│
├── app.py
├── logistic_regression_model.pkl
├── scaler.pkl
├── BG1.avif
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/yourusername/medplus-health-risk-predictor.git
cd medplus-health-risk-predictor
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Required libraries

```
streamlit
numpy
reportlab
scikit-learn
```

---

## 🔐 Email Configuration (IMPORTANT)

This app sends reports using Gmail SMTP.

### Step 1 — Enable 2-Step Verification

https://myaccount.google.com/security

### Step 2 — Generate App Password

https://myaccount.google.com/apppasswords

### Step 3 — Update in code

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_16_digit_app_password"
```

⚠ Never share your app password publicly.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 🧪 How to Use

1. Enter patient details in sidebar
2. Provide clinical measurements
3. Click **Predict Disease Risk**
4. View risk classification
5. Download PDF report (optional)
6. Enter email and send report (optional)
7. Click **Clear Inputs** to reset form

---

## 📄 Generated Report Contains

* Patient profile
* Clinical measurements
* Risk classification
* Preventive recommendation
* Structured medical summary

---

## 🛠️ Technology Stack

| Layer           | Technology   |
| --------------- | ------------ |
| Frontend        | Streamlit    |
| ML Model        | Scikit-learn |
| Data Processing | NumPy        |
| PDF Engine      | ReportLab    |
| Email Service   | SMTP (Gmail) |
| Language        | Python       |

---

## 🔒 Security Notes

* Use Gmail App Password (not real password)
* Do not commit credentials to GitHub
* Use environment variables for production

Example:

```python
import os
SENDER_EMAIL = os.getenv("EMAIL")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")
```

---


## 🧩 Future Enhancements

* Patient database storage
* Doctor dashboard login
* Health risk visualization charts
* AI medical chatbot
* SMS report delivery
* Appointment booking system
* Multi-disease prediction


---

## 🐞 Troubleshooting

### ReportLab import error

```
pip install reportlab
```

### Streamlit session error

Ensure reset is applied before widget creation.

### Email sending failed

* Check App Password
* Enable 2FA
* Verify SMTP port 465

---

## 📜 License

This project is intended for educational and demonstration purposes.

For clinical use, proper medical validation and regulatory compliance are required.

---

## 👨‍💻 Author

**- Shantanu Deshmukh**

Developed as part of an AI Healthcare Risk Prediction System project.

---

## ❤️ Acknowledgements

* Streamlit framework
* Scikit-learn ML tools
* ReportLab PDF engine

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository
⭐ Share with others
⭐ Improve preventive healthcare awareness

---

**Predict risk. Prevent disease. Protect lives.**
