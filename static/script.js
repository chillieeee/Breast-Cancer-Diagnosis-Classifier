// Group feature names by their prefix, matching how the dataset is structured
function groupFeatures(names) {
    const groups = { mean: [], error: [], worst: [] };
    names.forEach(name => {
        if (name.startsWith('mean ')) groups.mean.push(name);
        else if (name.includes('error')) groups.error.push(name);
        else if (name.startsWith('worst ')) groups.worst.push(name);
    });
    return groups;
}

// Build the 30 input fields inside their correct section
function buildForm() {
    const groups = groupFeatures(FEATURE_NAMES);

    Object.keys(groups).forEach(groupKey => {
        const container = document.getElementById(`grid-${groupKey}`);
        groups[groupKey].forEach(feature => {
            const wrapper = document.createElement('div');
            wrapper.className = 'form-group';

            const label = document.createElement('label');
            label.setAttribute('for', feature);
            label.textContent = feature;

            const input = document.createElement('input');
            input.type = 'number';
            input.step = 'any';
            input.id = feature;
            input.name = feature;
            input.required = true;

            wrapper.appendChild(label);
            wrapper.appendChild(input);
            container.appendChild(wrapper);
        });
    });
}

// Real sample data pulled from the dataset
const SAMPLES = {
    malignant: {
        'mean radius': 17.99, 'mean texture': 10.38, 'mean perimeter': 122.8, 'mean area': 1001.0,
        'mean smoothness': 0.1184, 'mean compactness': 0.2776, 'mean concavity': 0.3001,
        'mean concave points': 0.1471, 'mean symmetry': 0.2419, 'mean fractal dimension': 0.07871,
        'radius error': 1.095, 'texture error': 0.9053, 'perimeter error': 8.589, 'area error': 153.4,
        'smoothness error': 0.006399, 'compactness error': 0.04904, 'concavity error': 0.05373,
        'concave points error': 0.01587, 'symmetry error': 0.03003, 'fractal dimension error': 0.006193,
        'worst radius': 25.38, 'worst texture': 17.33, 'worst perimeter': 184.6, 'worst area': 2019.0,
        'worst smoothness': 0.1622, 'worst compactness': 0.6656, 'worst concavity': 0.7119,
        'worst concave points': 0.2654, 'worst symmetry': 0.4601, 'worst fractal dimension': 0.1189
    },
    benign: {
        'mean radius': 13.54, 'mean texture': 14.36, 'mean perimeter': 87.46, 'mean area': 566.3,
        'mean smoothness': 0.09779, 'mean compactness': 0.08129, 'mean concavity': 0.06664,
        'mean concave points': 0.04781, 'mean symmetry': 0.1885, 'mean fractal dimension': 0.05766,
        'radius error': 0.2699, 'texture error': 0.7886, 'perimeter error': 2.058, 'area error': 23.56,
        'smoothness error': 0.008462, 'compactness error': 0.0146, 'concavity error': 0.02387,
        'concave points error': 0.01315, 'symmetry error': 0.0198, 'fractal dimension error': 0.0023,
        'worst radius': 15.11, 'worst texture': 19.26, 'worst perimeter': 99.7, 'worst area': 711.2,
        'worst smoothness': 0.144, 'worst compactness': 0.1773, 'worst concavity': 0.239,
        'worst concave points': 0.1288, 'worst symmetry': 0.2977, 'worst fractal dimension': 0.07259
    }
};

function loadSample(sampleData) {
    Object.keys(sampleData).forEach(feature => {
        const input = document.getElementById(feature);
        if (input) input.value = sampleData[feature];
    });
    document.getElementById('result').classList.add('hidden');
}

function clearForm() {
    FEATURE_NAMES.forEach(feature => {
        const input = document.getElementById(feature);
        if (input) input.value = '';
    });
    document.getElementById('result').classList.add('hidden');
}

async function handleSubmit(e) {
    e.preventDefault();

    const btn = document.getElementById('predict-btn');
    const spinner = document.getElementById('btn-spinner');
    btn.disabled = true;
    spinner.classList.remove('hidden');

    const data = {};
    FEATURE_NAMES.forEach(feature => {
        data[feature] = document.getElementById(feature).value;
    });

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();

        const resultBox = document.getElementById('result');
        const resultIcon = document.getElementById('result-icon');
        const resultLabel = document.getElementById('result-label');
        const resultConfidence = document.getElementById('result-confidence');
        const confidenceFill = document.getElementById('confidence-fill');

        if (result.error) {
            resultBox.className = 'result-box';
            resultIcon.textContent = '⚠️';
            resultLabel.textContent = 'Error';
            resultConfidence.textContent = result.error;
            confidenceFill.style.width = '0%';
        } else {
            const isBenign = result.prediction === 'Benign';
            resultBox.className = 'result-box ' + result.prediction.toLowerCase();
            resultIcon.textContent = isBenign ? '✅' : '⚠️';
            resultLabel.textContent = `Prediction: ${result.prediction}`;
            resultConfidence.textContent =
                `Confidence: ${result.confidence}%  •  Malignant: ${result.probabilities.malignant}%  •  Benign: ${result.probabilities.benign}%`;
            confidenceFill.style.width = result.confidence + '%';
        }

        resultBox.classList.remove('hidden');
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } catch (err) {
        alert('Something went wrong contacting the server: ' + err.message);
    } finally {
        btn.disabled = false;
        spinner.classList.add('hidden');
    }
}

// Wire everything up once the page loads
document.addEventListener('DOMContentLoaded', () => {
    buildForm();
    document.getElementById('predict-form').addEventListener('submit', handleSubmit);
    document.getElementById('load-malignant').addEventListener('click', () => loadSample(SAMPLES.malignant));
    document.getElementById('load-benign').addEventListener('click', () => loadSample(SAMPLES.benign));
    document.getElementById('clear-form').addEventListener('click', clearForm);
});