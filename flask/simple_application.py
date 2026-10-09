from flask import Flask
app = Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to navyas first flask application"
@app.route("/index")
def index():
    return "welcome to navyas index page,here you could see nothing"

if __name__ == "__main__":
    app.run(debug = True)