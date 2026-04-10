import streamlit as st
import pandas as pd
import urllib.parse
import os
from PIL import Image

st.set_page_config(layout="wide")

# ---------- LOAD DATA ----------
sheet_url = "https://docs.google.com/spreadsheets/d/1UwAoDRHtT8tFLraCJ8CQKhqnPnZAZv9sG9KvomYiOPE/export?format=csv"
df = pd.read_csv(sheet_url)

# ---------- PAGE TITLE ----------
st.title("👨‍⚕️ Available Cardiologists")
st.write("Browse doctors and book an appointment easily.")
st.divider()

# ---------- HELP FUNCTION (IMAGE) ----------
def load_image(image_path):
    image_path = str(image_path).strip()

    try:
        # Google Drive image
        if "drive.google.com" in image_path:
            file_id = image_path.split("/d/")[1].split("/")[0]
            return f"https://drive.google.com/uc?export=download&id={file_id}"

        # Online image
        if image_path.startswith("http"):
            return image_path

        # Local image
        local_path = os.path.join("images", image_path)
        if os.path.exists(local_path):
            return Image.open(local_path)

        return "https://via.placeholder.com/120"

    except:
        return "https://via.placeholder.com/120"


# ---------- SESSION CHECK ----------
has_prediction = "patient_data" in st.session_state and "risk_percentage" in st.session_state

if not has_prediction:
    st.warning("⚠️ Please complete prediction first before booking a doctor.")

# ---------- DOCTORS UI ----------
for i, (_, row) in enumerate(df.iterrows()):

    with st.container(border=True):
        col1, col2 = st.columns([1, 4])

        # ---------- IMAGE ----------
        with col1:
            img = load_image(row["image"])
            st.image(img, width=120)

        # ---------- INFO ----------
        with col2:
            st.subheader(row["name"])
            st.write(f"🩺 **Specialty:** {row['specialty']}")
            st.write(f"📍 {row['address']}")

            # ---------- DETAILS ----------
            with st.expander("📅 View Availability & Booking"):

                days = [d.strip() for d in str(row["days"]).split(",")]
                times = [t.strip() for t in str(row["times"]).split(",")]

                col_days, col_times = st.columns(2)

                with col_days:
                    st.markdown("### Available Days")
                    for d in days:
                        st.info(d)

                with col_times:
                    st.markdown("### Available Times")
                    for t in times:
                        st.info(t)

                st.markdown("---")

                # ---------- BOOKING ----------
                if has_prediction:
                    patient = st.session_state.patient_data
                    risk = st.session_state.risk_percentage

                    # 🔥 Mapping values to readable text
                    chol_map = {
                        1: "Normal",
                        2: "Above Normal",
                        3: "Well Above Normal"
                    }

                    gluc_map = {
                        1: "Normal",
                        2: "Above Normal",
                        3: "Well Above Normal"
                    }

                    chol_text = chol_map.get(patient['cholesterol'], "Unknown")
                    gluc_text = gluc_map.get(patient['gluc'], "Unknown")

                    # 💬 WhatsApp Message
                    message = f"""
🫀 *Heart Disease Risk Report*

📊 Risk Probability: *{risk:.1f}%*

👤 *Patient Information*
- Age: {patient['age']}
- Gender: {'Male' if patient['gender']==1 else 'Female'}
- Height: {patient['height']}
- Weight: {patient['weight']}
- Blood Pressure: {patient['ap_hi']}/{patient['ap_lo']}
- Cholesterol: {chol_text}
- Glucose: {gluc_text}
- Smoking: {'Yes' if patient['smoke']==1 else 'No'}
- Alcohol: {'Yes' if patient['alco']==1 else 'No'}
- Active: {'Yes' if patient['active']==1 else 'No'}

📅 Please confirm the appointment.
"""

                    encoded_message = urllib.parse.quote(message)
                    whatsapp_url = f"https://wa.me/{row['phone']}?text={encoded_message}"

                    st.link_button("💬 Book via WhatsApp", whatsapp_url)

                else:
                    st.button("🔒 Complete Prediction First", disabled=True, key=f"disabled_btn_{i}")

    st.divider()