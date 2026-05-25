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

## 🌐 Live Demo
> 🚀 The app is now deployed and live on **Render.com**!

👉 **[Click here to try the app](https://breast-cancer-prediction-6vho.onrender.com)**


## 🌟 About This App

- ✅ Easy-to-use web interface
- 📊 Utilizes a trained ML model for fast predictions
- 🧬 Helps raise awareness for early detection of breast cancer
- 👩‍⚕️ Educational and user-friendly tool for academic and demo purposes
- ☁️ Deployed on Render.com for public access

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
git clone https://github.com/poornimasonkar/Breast-Cancer-Prediction.git
cd breast-cancer-prediction
pip install -r requirements.txt


### ▶️ Run Locally
```bash
python app.py
```
Then open your browser and go to `http://127.0.0.1:5000`

---

## 📦 Deployment (Render.com)
This app is deployed using **[Render.com](https://render.com)**. To deploy your own:

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a **New Web Service**
3. Connect your GitHub repo
4. Set the **Start Command** to:
```bash
   gunicorn app:app
```
5. Add a `requirements.txt` with all dependencies
6. Click **Deploy** 🚀

---

## 👩‍💻 Author
**Poornima Sonkar**
- 🐙 [GitHub](https://github.com/poornimasonkar)
- 💼 [LinkedIn](https://linkedin.com/in/poornima-sonkar-8507692b5)
