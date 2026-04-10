import streamlit as st     
import pandas as pd     
import pickle     
   
# Load model    
model = pickle.load(open('model.pkl', 'rb'))     
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))     
   
# Title    
st.title('❤️ Heart Disease Prediction System')    
st.write('Enter your health data below to estimate your heart disease risk.')    
   
# Inputs    
age = st.number_input('Age', value=25, min_value=1, max_value=100)     
gender = st.selectbox('Gender', ['Male', 'Female'])     
height = st.number_input("Height (cm)", value=170)     
weight = st.number_input("Weight (kg)", value=70)     
ap_hi = st.number_input("Systolic Blood Pressure (ap_hi)", value=120)     
ap_lo = st.number_input("Diastolic Blood Pressure (ap_lo)", value=80)     
   
cholesterol = st.selectbox('Cholesterol Level' , ['Normal', 'Above Normal', 'Well Above Normal'])     
gluc = st.selectbox('Glucose Level' , ['Normal', 'Above Normal', 'Well Above Normal'])     
   
smoke = st.selectbox('Do you smoke?' , ['No', 'Yes'])     
alco = st.selectbox('Do you drink alcohol?' , ['No', 'Yes'])     
active = st.selectbox('Are you physically active?' , ['Yes', 'No'])     
   
# Encoding    
gender_val = 1 if gender == 'Male' else 0    
cholesterol_val = 1 if cholesterol == 'Normal' else 2 if cholesterol == 'Above Normal' else 3    
gluc_val = 1 if gluc == 'Normal' else 2 if gluc == 'Above Normal' else 3    
smoke_val = 1 if smoke == 'Yes' else 0    
alco_val = 1 if alco == 'Yes' else 0    
active_val = 1 if active == 'Yes' else 0    
   
# Predict Button    
if st.button("🔍 Prediction"):  

    data = {     
        'age':age,     
        'gender':gender_val,     
        'height':height,     
        'weight':weight,     
        'ap_hi':ap_hi,     
        'ap_lo':ap_lo,     
        'cholesterol':cholesterol_val,     
        'gluc':gluc_val,     
        'smoke':smoke_val,     
        'alco':alco_val,     
        'active':active_val     
    }     
      
    data_df = pd.DataFrame(data, index=[0])     
    data_preprocessed = preprocessor.transform(data_df)     
      
    prob = model.predict_proba(data_preprocessed)[0][1] * 100    

    # Save in session_state
    st.session_state['patient_data'] = data 
    st.session_state['risk_percentage'] = prob 


# ✅ عرض النتيجة بعد التخزين (مش جوه الزرار)
if 'risk_percentage' in st.session_state:

    prob = st.session_state['risk_percentage']
    
    st.subheader(f"Risk Percentage: {prob:.2f}%")

    if prob < 50:  
        st.success("✅ You are in good condition, but keep taking care of your health 💚")  

    elif prob < 65:  
        st.warning("⚠️ It is recommended to visit a doctor for a quick check-up 💛")  

    elif prob < 75:  
        st.error("🚨 You should visit a doctor soon 🔴")  

    elif prob < 85:  
        st.error("🚨🚨 Visit a doctor immediately! This needs attention 🔴")  

    elif prob < 95:  
        st.error("🚨🚨🚨 Visit a doctor as soon as possible! 🔴")  

    else:  
        st.error("🚨🚨🚨🚨 Critical condition! Seek medical help immediately! 🔴")  

    # زرار الانتقال
    if prob > 50:
        if st.button("👨‍⚕️ Find Doctor"):
            st.switch_page("pages/2_Doctors.py")