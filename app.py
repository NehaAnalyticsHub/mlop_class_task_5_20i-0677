from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
collection = db['users']

# Route to serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.form  # Get form data
    name = data.get('name')
    email = data.get('email')
    print(name)
    
    # Insert data into MongoDB
    user_data = {
        'name': name,
        'email': email
    }
    result = collection.insert_one(user_data)
    
    return jsonify({"message": "Data stored successfully", "userID": str(result.inserted_id)}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

