from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model and feature names once, when the server starts
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))
model_path = os.path.join(BASE_DIR, "cancer_model.pkl")
features_path = os.path.join(BASE_DIR, "feature_names.pkl")
model = joblib.load(model_path)
feature_names = joblib.load(features_path)
@app.route('/')
def home():
    return render_template('index.html', feature_names=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    # Ensure request is JSON
    if not request.is_json:
        return jsonify({"error": "Invalid content type, JSON expected."}), 415
    data = request.get_json()

    # Validate that all required features are present
    missing = [f for f in feature_names if f not in data]
    if missing:
        return jsonify({"error": f"Missing required features: {', '.join(missing)}"}), 400

    # Convert inputs to float, with per‑feature validation
    input_values = []
    for feature in feature_names:
        try:
            input_values.append(float(data[feature]))
        except (ValueError, TypeError):
            return jsonify({"error": f"Feature '{feature}' must be a numeric value."}), 400
    input_array = np.array(input_values).reshape(1, -1)

    try:
        prediction = model.predict(input_array)[0]
        probabilities = model.predict_proba(input_array)[0]
        result = "Benign" if prediction == 1 else "Malignant"
        confidence = float(probabilities[prediction]) * 100
        return jsonify({
            "prediction": result,
            "confidence": round(confidence, 2),
            "probabilities": {
                "malignant": round(float(probabilities[0]) * 100, 2),
                "benign": round(float(probabilities[1]) * 100, 2)
            }
        })
    except Exception:
        # Internal server error – log can be added later
        return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Host 0.0.0.0 makes the app reachable from containers; debug disabled for production
    app.run(host='0.0.0.0', port=5000, debug=False)