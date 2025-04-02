# 6. How do you handle forms in Flask?

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return render_template('success.html', name=name, email=email)
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
