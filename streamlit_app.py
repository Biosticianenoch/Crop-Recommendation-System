
import pickle
import os
import numpy as np
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Crop Recommendation System", layout="centered")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("crop_recommendation1.sav", 'rb'))

# ---------------- LABEL TO CROP NAME MAP ----------------
label_to_crop = {
    0: 'apple', 1: 'banana', 2: 'blackgram', 3: 'chickpea', 4: 'coconut',
    5: 'coffee', 6: 'cotton', 7: 'grapes', 8: 'jute', 9: 'kidneybeans',
    10: 'lentil', 11: 'maize', 12: 'mango', 13: 'mothbeans', 14: 'mungbean',
    15: 'muskmelon', 16: 'orange', 17: 'papaya', 18: 'pigeonpeas',
    19: 'pomegranate', 20: 'rice', 21: 'watermelon'
}

# ---------------- VISITOR COUNTER ----------------
counter_file = "visitor_data.pkl"

if os.path.exists(counter_file):
    with open(counter_file, 'rb') as f:
        visitor_data = pickle.load(f)
else:
    visitor_data = {'count': 0, 'timestamps': []}

if 'counted' not in st.session_state:
    st.session_state['counted'] = True
    visitor_data['count'] += 1
    visitor_data['timestamps'].append(str(datetime.datetime.now()))
    with open(counter_file, 'wb') as f:
        pickle.dump(visitor_data, f)

# ---------------- SIDEBAR MENU ----------------
with st.sidebar:
    selected = option_menu("Main Menu", 
                           ["Welcome", "Prediction", "FAQ", "Disclaimer", "Analytics", "Donate & Support"], 
                           icons=['house', 'activity', 'question-circle', 'exclamation-circle', 'bar-chart'],
                           menu_icon="cast", default_index=0)

# ---------------- WELCOME PAGE ----------------
if selected == "Welcome":
    st.markdown("<h1 style='text-align: center; color: green;'>🌿 Crop Recommendation System</h1>", unsafe_allow_html=True)
    st.success(f"🚜 *Total Visitors:* {visitor_data['count']}")
    st.write("""
    This intelligent tool helps farmers and agricultural experts recommend the most suitable crop to grow based on soil and climate parameters.

    ✅ Data-driven predictions  
    ✅ Easy-to-use interface  
    ✅ Supports smart agriculture

    👉 Use the sidebar to start predicting now!
    """)

# ---------------- PREDICTION PAGE ----------------
elif selected == "Prediction":
    st.markdown("<h2 style='text-align: center;'>🌾 Recommend the Best Crop</h2>", unsafe_allow_html=True)
    st.write("Input the following soil and environmental data:")

    with st.form("crop_form"):
        N = st.number_input("Nitrogen (N)", 0.0, 140.0, step=1.0)
        P = st.number_input("Phosphorus (P)", 0.0, 145.0, step=1.0)
        K = st.number_input("Potassium (K)", 0.0, 205.0, step=1.0)
        temperature = st.number_input("Temperature (°C)", 8.0, 45.0, step=0.1)
        humidity = st.number_input("Humidity (%)", 10.0, 100.0, step=0.1)
        ph = st.number_input("pH Level", 3.0, 10.0, step=0.1)
        rainfall = st.number_input("Rainfall (mm)", 20.0, 300.0, step=1.0)

        submit = st.form_submit_button("Recommend Crop")

    if submit:
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction_raw = model.predict(input_data)[0]

        # Handle numerical predictions
        prediction = label_to_crop.get(prediction_raw, prediction_raw)  # fallback if already string
        st.success(f"🌱 *Recommended Crop to Grow:* {prediction.capitalize()}")

# ---------------- FAQ PAGE ----------------
elif selected == "FAQ":
    st.markdown("<h2 style='text-align: center;'>❓ Frequently Asked Questions</h2>", unsafe_allow_html=True)

    with st.expander("📌 What does this app do?"):
        st.write("It recommends the best crop to grow based on soil nutrients and environmental factors using machine learning.")

    with st.expander("📌 How was the model trained?"):
        st.write("Using a dataset with labeled crop data, various ML models were tested, and Random Forest was selected based on accuracy.")

    with st.expander("📌 What if I input unusual values?"):
        st.write("The model will still predict, but predictions are most accurate with realistic, field-based values.")

    with st.expander("📌 What crops are included?"):
        st.write("Crops like rice, maize, lentil, banana, coconut, cotton, ground nut, mango, apple, and many more are covered.")

    with st.expander("📌 Can this tool work offline?"):
        st.write("Yes. Once deployed locally, it can work without an internet connection.")

    with st.expander("📌 Can I use this app for other regions?"):
        st.write("Yes, but performance will depend on how similar local conditions are to those in the training data.")

    with st.expander("📌 Can I use this for fertilizer recommendation?"):
        st.write("This app focuses on crop prediction, but similar models can be trained for fertilizer recommendation as well.")

# ---------------- DISCLAIMER PAGE ----------------
elif selected == "Disclaimer":
    st.markdown("<h2 style='text-align: center;'>⚠ Disclaimer</h2>", unsafe_allow_html=True)
    st.warning("""
    - This app is meant to aid agricultural decision-making.
    - It does not replace field trials or expert agronomist advice.
    - Always combine predictions with local knowledge.
    """)

# ---------------- ANALYTICS PAGE ----------------
elif selected == "Analytics":
    st.markdown("<h2 style='text-align: center;'>📊 Visitor Analytics</h2>", unsafe_allow_html=True)

    st.info(f"👥 *Total Visitors:* {visitor_data['count']}")

    if visitor_data['timestamps']:
        st.write("### 🕒 Visitor Log")
        st.dataframe(visitor_data['timestamps'])

    if st.button("🔄 Reset Visitor Counter"):
        visitor_data = {'count': 0, 'timestamps': []}
        with open(counter_file, 'wb') as f:
            pickle.dump(visitor_data, f)
        st.success("Visitor counter reset. Please refresh to see update.")

# ---------------- DONATION PAGE ----------------
elif selected == "Donate & Support":
    st.markdown("<h2 style='text-align: center;'>💖 Support My Work</h2>", unsafe_allow_html=True)

    st.write("""
    If this tool has helped you and you'd like to support its further development, please consider donating 🙏

    - *PayPal:* dataquestsolutions2@gmail.com  
    - *Buy Me a Coffee (M-Pesa):* +254701344230  
    - *M-Pesa Paybill (Kenya):*  
        - *Paybill:* 522522  
        - *Account Number:* 1340849054  

    Every contribution fuels innovation in smart agriculture 💚
    """)
