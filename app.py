from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model_filename = 's_prediction_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        # Extract and convert input values to the correct format
        input_data = [
            int(data['gender']),
            float(data['age']),
            int(data['hypertension']),
            int(data['heart_disease']),
            int(data['ever_married']),
            int(data['work_type']),
            int(data['Residence_type']),
            float(data['avg_glucose_level']),
            float(data['bmi']),
            int(data['smoking_status'])
        ]

        # Convert to numpy array and reshape for prediction
        input_array = np.array(input_data).reshape(1, -1)

        # Predict using the loaded model
        prediction = model.predict(input_array)
        prediction_proba = model.predict_proba(input_array)[0]

        if prediction[0] == 1:
            return render_template('stroke_alert.html')
        else:
            return render_template('no_stroke.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

