from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to first course"
@app.route("/index",methods = ['GET'])  #default method is get
def index():
    return render_template("index.html")

@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'POST': #it captures the post requests
        name = request.form['name']
        return f'Hello {name}!'  #we got here the name but i want it to redirect it to html page, this uses jinja2 template
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)