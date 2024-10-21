from flask import Flask

app = Flask(__name__)  # Benenne die Flask-Instanz "app"

@app.route('/')
def home():
    return "Hello, Flask!"

