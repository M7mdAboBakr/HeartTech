import streamlit as st

st.set_page_config(layout="wide")

# ---------- TITLE ----------
st.title("❤️ Heart Disease Prediction & Doctor Booking Platform")

st.divider()

# ---------- INTRO ----------
st.markdown("""
## 🧠 About the Project

This platform helps users:
- Predict heart disease risk using machine learning
- Get a personalized risk percentage
- Find available cardiologists
- Book appointments directly via WhatsApp

The goal is to make healthcare access easier, faster, and more connected.
""")

st.divider()

# ---------- HOW IT WORKS ----------
st.markdown("""
## ⚙️ How to Use the Platform

### 1️⃣ Enter Patient Data  
Go to the **Prediction page** and input your medical and personal data.

### 2️⃣ Get Risk Prediction  
The system will analyze your data and generate a **heart disease risk percentage**.

### 3️⃣ Browse Doctors  
Navigate to the **Doctors page** to view available cardiologists.

### 4️⃣ Book Appointment  
Choose a doctor and book instantly via **WhatsApp** with your generated report.

""")

st.divider()

# ---------- FEATURES ----------
st.markdown("""
## 🚀 Key Features

- 🤖 AI-powered heart disease prediction  
- 📊 Risk percentage output  
- 👨‍⚕️ Doctor directory with availability  
- 💬 WhatsApp booking integration  
- 📱 Simple and user-friendly interface  
""")

st.divider()

# ---------- CTA ----------
st.success("👉 Start by entering your data from the Prediction page!")


st.info("💡 Tip: Make sure to complete the prediction first before booking a doctor.")