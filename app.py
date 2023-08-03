## simple app

from flask import Flask,render_template,request,redirect,url_for

## create flask app

app= Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello world</h1>"

@app.route('/welcome')
def welcome():
    return "this is flask tuttorial"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the result is"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is fail andthe result is"+str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        math=float(request.form['mathMarks'])
        science=float(request.form['scienceMarks'])

        avg_marks=(math+science)/2

        result=""
        if avg_marks>50:
            result="success"
        else:
            result="fail"
        return redirect(url_for(result,score=avg_marks))

        #return render_template('result.html',results=avg_marks)

@app.route('/calculatemarks')
def calculatemarks():
    return 




if __name__=='__main__':
    app.run(debug=True)
