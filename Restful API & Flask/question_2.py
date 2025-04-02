# 2. How do you serve static files like images or CSS in Flask?

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index3.html')

if __name__ == '__main__':
    app.run(debug=True)
