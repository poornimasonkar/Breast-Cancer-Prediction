import streamlit as st
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            features = request.form['features']
            features = [float(x.strip()) for x in features.split(',')]
            if len(features) != 30:
                raise ValueError("Exactly 30 features are required.")
            final_features = [np.array(features)]
            result = model.predict(final_features)[0]

            if result == 1:
                prediction = "🧬 Cancerous"
            else:
                prediction = "✅ Non-Cancerous"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)



