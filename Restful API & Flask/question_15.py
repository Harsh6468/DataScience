#  15. How do you capture URL parameters in Flask?

from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def greet_user(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
