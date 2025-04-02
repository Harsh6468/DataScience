# How do you manage sessions in Flask?
from flask import Flask, session, redirect, url_for, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def home():
    return render_template('index4.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    if username:
        session['user'] = username
        flash("Login successful!", "success")
        return redirect(url_for('dashboard'))
    flash("Username is required!", "error")
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', username=session['user'])
    flash("Please log in first.", "warning")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
