# 7. How can you validate form data in Flask?

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            flash("All fields are required!", "error")
            return redirect(url_for('index'))

        if "@" not in email:
            flash("Invalid email address!", "error")
            return redirect(url_for('index'))

        return render_template('success.html', name=name, email=email)

    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
