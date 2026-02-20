# =========================================================
# 🔹 IMPORTS
# =========================================================
import streamlit as st
import numpy as np
import pickle
import base64
import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
load_dotenv() 


# =========================================================
# 🔹 EMAIL CONFIGURATION
# =========================================================
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASS")



# =========================================================
# 🔹 LOAD MODEL & SCALER
# =========================================================
model = pickle.load(open("logistic_regression_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


# =========================================================
# 🔹 DEFAULT VALUES
# =========================================================
default_values = {
    "age": 30,
    "sleep": 7,
    "exercise": "Moderate",
    "family": "No",
    "diet": "Average",
    "bp": 120,
    "glucose": 100,
    "cholesterol": 180,
    "heart_rate": 72,
    "waist": 85
}


# =========================================================
# 🔹 SESSION STATE INIT
# =========================================================
for k, v in default_values.items():
    if k not in st.session_state:
        st.session_state[k] = v

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "probability" not in st.session_state:
    st.session_state.probability = None

if "reset_trigger" not in st.session_state:
    st.session_state.reset_trigger = False


# =========================================================
# 🔹 APPLY RESET BEFORE WIDGETS LOAD (CRITICAL FIX)
# =========================================================
if st.session_state.reset_trigger:
    for k, v in default_values.items():
        st.session_state[k] = v
    st.session_state.prediction = None
    st.session_state.probability = None
    st.session_state.reset_trigger = False


# =========================================================
# 🔹 RESET FUNCTION
# =========================================================
def reset_inputs():
    st.session_state.reset_trigger = True


# =========================================================
# 🔹 PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Healthcare Risk Predictor",
    page_icon="🩺",
    layout="wide"
)


# =========================================================
# 🔹 BACKGROUND IMAGE
# =========================================================
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64("BG1.avif")

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{bg_img}");
    background-size: cover;
    background-attachment: fixed;
}}
[data-testid="stSidebar"] {{
    background: rgba(52,152,219,0.65);
}}
.stButton>button {{
    background-color: #1f77b4;
    color: white;
    border-radius: 8px;
}}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 🔹 HEADER
# =========================================================

st.markdown(
    """
    <h1 style='text-align: center;'>🩺 MedPlus Health Risk Predictor</h1>
    <p style='text-align: center; font-size:18px; color:gray;'>
        Predict risk. Prevent disease. Protect lives
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# 🔹 SIDEBAR INPUTS
# =========================================================
st.sidebar.header("🧾 Patient Health Information")

age = st.sidebar.slider("Age", 1, 120, key="age")
sleep = st.sidebar.slider("Sleep Hours", 0, 15, key="sleep")
exercise = st.sidebar.selectbox("Exercise Level", ["Low", "Moderate", "High"], key="exercise")
family = st.sidebar.selectbox("Family History", ["No", "Yes"], key="family")
diet = st.sidebar.selectbox("Diet Quality", ["Poor", "Average", "Healthy"], key="diet")


# =========================================================
# 🔹 MAIN LAYOUT
# =========================================================
left_main, right_panel = st.columns([2, 1])


# =========================================================
# 🔹 CLINICAL INPUTS
# =========================================================
with left_main:

    st.subheader("📊 Clinical Measurements")

    col1, col2 = st.columns(2)
    with col1:
        bp = st.number_input("Blood Pressure (mmHg)", 50, 250, key="bp")
    with col2:
        glucose = st.number_input("Glucose (mg/dL)", 50, 300, key="glucose")

    col3, col4 = st.columns(2)
    with col3:
        cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 400, key="cholesterol")
    with col4:
        heart_rate = st.number_input("Heart Rate (bpm)", 40, 180, key="heart_rate")

    waist = st.number_input("Waist Circumference (cm)", 50, 150, key="waist")

    st.divider()

    col_btn1, col_btn2 = st.columns(2)
    predict_btn = col_btn1.button("🔍 Predict Disease Risk")
    clear_btn = col_btn2.button("🧹 Clear Inputs")

    if clear_btn:
        reset_inputs()
        st.rerun()


# =========================================================
# 🔹 ENCODING
# =========================================================
exercise_map = {"Low":0, "Moderate":1, "High":2}
family_map = {"No":0, "Yes":1}
diet_map = {"Poor":0, "Average":1, "Healthy":2}


# =========================================================
# 🔹 RECOMMENDATION
# =========================================================
def recommendation(risk):
    if risk == 2:
        return "HIGH RISK — Consult doctor immediately"
    elif risk == 1:
        return "MEDIUM RISK — Improve lifestyle"
    else:
        return "LOW RISK — Maintain healthy lifestyle"


# =========================================================
# 🔹 PDF GENERATOR
# =========================================================
def generate_pdf(pred):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Healthcare Risk Prediction Report", styles["Title"]))
    story.append(Spacer(1,10))

    story.append(Paragraph(f"Age: {st.session_state.age}", styles["Normal"]))
    story.append(Paragraph(f"Sleep: {st.session_state.sleep}", styles["Normal"]))
    story.append(Paragraph(f"Exercise: {st.session_state.exercise}", styles["Normal"]))
    story.append(Paragraph(f"BP: {st.session_state.bp}", styles["Normal"]))
    story.append(Paragraph(f"Glucose: {st.session_state.glucose}", styles["Normal"]))
    story.append(Paragraph(f"Cholesterol: {st.session_state.cholesterol}", styles["Normal"]))
    story.append(Paragraph(f"Heart Rate: {st.session_state.heart_rate}", styles["Normal"]))
    story.append(Paragraph(f"Waist: {st.session_state.waist}", styles["Normal"]))
    story.append(Spacer(1,10))

    story.append(Paragraph("Prediction Result", styles["Heading2"]))
    story.append(Paragraph(recommendation(pred), styles["Normal"]))

    doc.build(story)
    buffer.seek(0)
    return buffer


# =========================================================
# 🔹 EMAIL FUNCTION
# =========================================================
def send_email(receiver, pdf_buffer):

    msg = EmailMessage()
    msg["Subject"] = "Healthcare Risk Report"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver

    msg.set_content("Attached is your health prediction report.")

    msg.add_attachment(
        pdf_buffer.getvalue(),
        maintype="application",
        subtype="pdf",
        filename="health_report.pdf"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)


# =========================================================
# 🔹 PREDICTION
# =========================================================
if predict_btn:

    features = np.array([[
        age, bp, glucose, cholesterol,
        exercise_map[exercise],
        sleep,
        family_map[family],
        diet_map[diet],
        heart_rate, waist
    ]])

    scaled = scaler.transform(features)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)

    st.session_state.prediction = pred
    st.session_state.probability = prob


# =========================================================
# 🔹 RESULTS PANEL
# =========================================================
with right_panel:

    st.subheader("🩺 Health Recommendation")

    if st.session_state.prediction is None:
        st.info("Enter details and predict")

    else:
        pred = st.session_state.prediction

        if pred == 2:
            st.error("HIGH RISK")
        elif pred == 1:
            st.warning("MEDIUM RISK")
        else:
            st.success("LOW RISK")

        pdf = generate_pdf(pred)

        st.download_button(
            "📄 Download Report",
            pdf,
            "health_report.pdf",
            "application/pdf"
        )

        st.divider()
        st.write("📧 Email Report")

        email = st.text_input("Enter email")

        if st.button("Send Email"):
            send_email(email, generate_pdf(pred))
            st.success("Report sent successfully!")