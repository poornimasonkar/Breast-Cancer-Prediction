# 🎗️ Breast Cancer Prediction Web App

Welcome to the **Breast Cancer Prediction Web Application** – a simple yet powerful tool built using **Machine Learning, Flask, and HTML** to help identify whether a tumor is **cancerous** or **non-cancerous** based on 30 key input features.

---

## 📌 Project Highlights

- 🤖 **ML Model**: Logistic Regression
- 🧪 **Input**: 30 numerical features related to tumor characteristics
- 🔮 **Output**: Predicts if the tumor is `Cancerous (Malignant)` or `Non-Cancerous (Benign)`
- 💻 **Tech Stack**: Python, Flask, HTML/CSS, Pickle
- 📂 **Dataset**: UCI Breast Cancer Wisconsin (Diagnostic)

---

## 🌟 About This App

- ✅ Easy-to-use web interface
- 📊 Utilizes a trained ML model for fast predictions
- 🧬 Helps raise awareness for early detection of breast cancer
- 👩‍⚕️ Educational and user-friendly tool for academic and demo purposes

---

## 🔍 How It Works

1. The user enters 30 features from a tumor analysis.
2. The backend sends the features to a Logistic Regression model.
3. The model returns a prediction.
4. The result is displayed on the page as:
   - ✅ **Non-Cancerous**
   - 🧬 **Cancerous**

---

## 📁 Dataset Information

- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- **Features**: 30 real-valued inputs from digitized tumor images
- **Classes**: Malignant (M), Benign (B)

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.x
- Flask
- NumPy
- scikit-learn
- Pickle
- Jupyter Notebook (optional for training)

### 🔽 Installation

```bash
git clone https://github.com/yourusername/breast-cancer-prediction.git
cd breast-cancer-prediction
pip install -r requirements.txt
