from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and feature names once, when the server starts
model = joblib.load('models/cancer_model.pkl')
feature_names = joblib.load('models/feature_names.pkl')

@app.route('/')
def home():
    return render_template('index.html', feature_names=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        # Build the input array in the exact order the model expects
        input_values = [float(data[feature]) for feature in feature_names]
        input_array = np.array(input_values).reshape(1, -1)

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
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)