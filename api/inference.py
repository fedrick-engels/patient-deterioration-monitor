from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    features = np.array([
        data['heart_rate'],
        data['spo2'],
        data['map'],
        data['resp_rate'],
        data['temp']
    ]).reshape(1, -1)
    
    prob = model.predict_proba(features)[0][1]
    
    if prob > 0.7:
        status = "Critical"
    elif prob > 0.4:
        status = "Warning"
    else:
        status = "Stable"
    
    return jsonify({
        "risk_score": float(prob * 100),
        "status": status
    })

app.run(port=5000)
