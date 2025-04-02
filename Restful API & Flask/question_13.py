# 13. How can you redirect with query parameters in Flask?

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/redirect-example')
def redirect_example():
    return redirect(url_for('greet', name='Harsh', age=25))

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'Unknown')
    return f"Hello, {name}! You are {age} years old."

if __name__ == '__main__':
    app.run(debug=True)
