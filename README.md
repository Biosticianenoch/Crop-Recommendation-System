# 🌾 Crop Recommendation System using Machine Learning

Welcome to the **Smart Crop Recommendation System**, a machine learning-powered tool designed to help farmers, agriculturalists, and researchers make data-driven decisions about which crop to grow based on soil and environmental conditions.

---

## 🚀 Features at a Glance

✨ **ML-Powered Predictions** — Recommends the best crop based on real-time input  
📊 **Visitor Analytics** — Tracks and displays total visits and interaction timestamps  
🧠 **Trained with Real Agricultural Data** — Built with a Random Forest model trained on real soil and crop data  
🖥 **Streamlit Web Interface** — Fully interactive, fast, and responsive  
💸 **Donation Support** — Accepts contributions via PayPal and M-Pesa  
📚 **Multi-Page Interface** — Includes Welcome, FAQ, Disclaimer, Analytics, and more!

---

## 📁 Project Structure

```bash
.
├── crop_recommendation1.sav          # Trained ML model
├── app.py                            # Main Streamlit application
├── Crop Recommendation.ipynb         # Jupyter notebook for model development
├── visitor_data.pkl                  # Visitor log
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

---

## 🧠 How the Model Works

- **Input Features:**
  - 🧪 Nitrogen (N)
  - 🧪 Phosphorus (P)
  - 🧪 Potassium (K)
  - 🌡 Temperature (°C)
  - 💧 Humidity (%)
  - ⚗️ pH
  - 🌧 Rainfall (mm)

- **Model:** Random Forest Classifier  
- **Target:** One of 22 crops including `rice`, `maize`, `banana`, `mango`, `apple`, `cotton`, `coffee`, `lentil`, `jute`, `mungbean`, and more.

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crop-recommendation-system.git
cd crop-recommendation-system
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Launch the App

```bash
streamlit run app.py
```

The app will open at [http://localhost:8501](http://localhost:8501)

---

## 📸 Screenshots

> _Add screenshots here to give users a visual idea of the app interface._

---

## 📬 Donate & Support

If this project has helped you, consider supporting it 🙏

- 📧 **PayPal:** dataquestsolutions2@gmail.com  
- ☕ **M-Pesa (Buy Me a Coffee):** +254701344230  
- 🏦 **M-Pesa Paybill:**
  - Paybill: `522522`
  - Account: `1340849054`

> Your contribution fuels innovation in smart agriculture 💚

---

## ⚠️ Disclaimer

- This is a decision-support tool and should not replace professional agronomic advice.
- Best results are achieved when combined with field experience and localized data.

---

## 🧑‍💻 Developed By

**Enoch Bereka**  
Email: [dataquestsolutions2@gmail.com](dataquestsolutions2@gmail.com)  
Location: Kakamega, Kenya  
Organization: [DataQuest Solutions]([https://github.com/your-org](https://my-project-git-main-enocks-projects-27f604c8.vercel.app))

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

