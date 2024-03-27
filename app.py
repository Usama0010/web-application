from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://database:27017/")
db = client["mydatabase"]
collection = db["users"]

@app.route('/store', methods=['POST'])
def store_user_info():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        user = {'name': name, 'email': email}
        collection.insert_one(user)
        return jsonify({'message': 'User information stored successfully'}), 201
    else:
        return jsonify({'error': 'Name and Email are required'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
