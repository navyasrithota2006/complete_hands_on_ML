#building url dynamically
#variable rule
#jinja2 template engine


#jinja 2  template engine
'''
{{  }} - expressions to print output in html
{%....%} - conditions, for loops
{#....#} - thisis for comments

'''

from flask import Flask,render_template,request,redirect,url_for
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

@app.route('/submit1',methods=['GET','POST'])
def submit1():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name}!"
    return render_template('form.html')


#variable rule #using jinja template {{}}
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



#loop jinja template {%..%}
@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score >= 50:
        res='passed'
    else:
        res="failed"

    exp = {'score':score,'res':res}
    return render_template('result1.html',results=exp)

#using jinja template {%...%} - if statement
@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result2.html',results=score)

#here now i want to build the dynamic url like i will 
#get my results and calculate and it should redirect me with 
#pass or fail page
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result2.html',results = score)

@app.route('/submit',methods =['POST','GET'])
def submit():
    total_score = 0
    #we have got the ids in the get result.html and whenever 
    #the person posts into the form we have to collect it and do the sum
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c= float(request.form['c'])
        data_science= float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    #to get the results we have to show the form 
    else:  
        return render_template('get_result.html')
    return redirect(url_for('successres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)