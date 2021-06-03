from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/vikas")
def vikas():
    return "Hello vikas bhai"

app.run(debug=True)
