# Breast‑Cancer‑Diagnosis‑Classifier 🩺

[![CI](https://github.com/your-username/Breast-Cancer-Diagnosis-Classifier/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/Breast-Cancer-Diagnosis-Classifier/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **beautiful, production‑ready** web app that predicts whether a breast mass is **malignant** or **benign** using a Random Forest model trained on the Wisconsin Breast Cancer dataset.

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/your-username/Breast-Cancer-Diagnosis-Classifier.git
cd Breast-Cancer-Diagnosis-Classifier

# Create a virtual environment and install dependencies
python -m venv venv
source venv/Scripts/activate   # PowerShell on Windows
pip install -r requirements.txt

# Train the model (only needed the first time)
python train_model.py

# Run the Flask app
python app.py
```

Open your browser at `http://127.0.0.1:5000` – you’ll see a sleek UI where you can load sample data, fill in the 30 numeric fields, and get a real‑time prediction with confidence bars.

---

## 📸 Screenshot

![App mockup](file:///C:/Users/Welcome/.gemini/antigravity-ide/brain/76ecc8d6-3cb9-4749-883a-e043177eec64/ui_mockup_1791538255808.jpg)

---

## 🛠️ Features

- **Exploratory data analysis** script (`explore_data.py`).
- **Random Forest** model trained on the classic breast‑cancer dataset.
- **Flask backend** with a clean, responsive front‑end (glass‑morphism, subtle animations).
- **Robust API** – strict JSON validation, clear error messages, production‑ready server launch.
- **Full test suite** & CI pipeline that lint, type‑check, and run functional tests on every push.

---

## 📖 Usage via API

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
        "mean radius": 13.54,
        "mean texture": 14.36,
        ... (all 30 features) ...
      }'
```

Response (pretty‑printed):

```json
{
  "prediction": "Benign",
  "confidence": 96.23,
  "probabilities": {
    "malignant": 3.77,
    "benign": 96.23
  }
}
```

---

## 🧪 Development

```bash
# Install dev tools
pip install -r dev-requirements.txt

# Run tests
pytest
```

The CI workflow (`.github/workflows/ci.yml`) automatically runs the same checks on every push.

---

## 🤝 Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit issues, fork the repo, and open pull requests.

---

## 📜 License

Distributed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🛡️ Security

If you discover a security vulnerability, please report it responsibly by emailing the maintainers (see `CODE_OF_CONDUCT.md`).
