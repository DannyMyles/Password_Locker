from flask import Flask, app
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hellow, World!<p>"