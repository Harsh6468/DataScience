# 12. How do you define a custom Jinja filter in Flask?
from flask import Flask, render_template

app = Flask(__name__)

def capitalize_words(value):
    """Converts a string to title case (capitalizes each word)."""
    return value.title()

app.jinja_env.filters['capitalize'] = capitalize_words

@app.route('/')
def home():
    text = "welcome to flask custom filters"
    return render_template('index.html', message=text)

if __name__ == '__main__':
    app.run(debug=True)
