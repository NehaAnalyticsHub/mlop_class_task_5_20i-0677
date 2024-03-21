from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data sent by the client
        data = request.get_json()
        
        # Convert the JSON data to a DataFrame
        input_data = pd.DataFrame(data, index=[0])
        
        # Make predictions
        predictions = model.predict(input_data)
        
        # Return the predictions as JSON
        return jsonify({'predictions': predictions.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
