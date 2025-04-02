# 14. How do you return JSON responses in Flask?
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user')
def get_data():
    response = {
        "message": "Hello, this is a JSON response!",
        "status": "success",
        "data": {"name": "Harsh", "age": 25}
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
