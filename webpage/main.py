from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! You are on the main page"

if __name__ == "main":
    app.run()
