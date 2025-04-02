# 3. How do you define different routes with different HTTP methods in Flask4
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask practicle!"

@app.route('/user/<username>')
def greet_user(username):
    return f"Hello, {username}!"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    return jsonify({"message": "Data received", "data": data})

@app.route('/update', methods=['PUT'])
def update():
    data = request.json
    return jsonify({"message": "Data updated", "data": data})

@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    return jsonify({"message": f"Item {item_id} deleted"})

if __name__ == '__main__':
    app.run(debug=True)
