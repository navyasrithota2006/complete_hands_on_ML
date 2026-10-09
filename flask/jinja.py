#building url dynamically
#variable rule
#jinja2 template engine


#jinja 2  template engine
'''
{{  }} - expressions to print output in html
{%....%} - conditions, for loops
{#....#} - thisis for comments

'''

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

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name}!"
    return render_template('form.html')


#variable rule
@app.route('/success/<int:score>')
def success(score):
    #return "The marks you got is "+str(score) - in this example
    #whatever you assigned ot the variable score it must be returned in the form of string
    res = ''
    if score >= 50:
        res='passed'
    else:
        res="failed"
    return render_template('result.html',results=res)


if __name__=="__main__":
    app.run(debug=True)