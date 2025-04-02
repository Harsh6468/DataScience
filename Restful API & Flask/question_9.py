# 9. How do you redirect to a different route in Flask?
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))  # Redirects to the login route

@app.route('/login')
def login():
    return "You have been redirected to the login page."

if __name__ == '__main__':
    app.run(debug=True)
