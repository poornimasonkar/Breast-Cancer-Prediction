from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features_str = request.json['features']
        values = [float(x.strip()) for x in features_str.split(',')]
        
        if len(values) != 30:
            return jsonify({'prediction': '❌ Please enter exactly 30 values'}), 400
            
        input_array = np.array(values).reshape(1, -1)
        pred = model.predict(input_array)[0]
        
        result = "Malignant (Cancerous) ❌" if pred == 0 else "Benign (Non-Cancerous) ✅"
        return jsonify({'prediction': result})
        
    except:
        return jsonify({'prediction': '❌ Invalid input. Enter 30 comma-separated numbers'}), 400

if __name__ == '__main__':
    app.run(debug=True)
