from flask import Flask,render_template,request,redirect

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    email=request.form.get('email')
    pwd= request.form.get('pass')
    if email=='abc@gmail.com':
        if pwd=='123':
            return redirect('/next1')
        else:
            return "<script>alert('Invalid Password..!!');</script>"
    elif email!='abc@gmail.com' and pwd!='123':
        return "<script>alert('Invalid Input..!!');</script>"
    else:
        return "<script>alert('Invalid Username..!!');</script>"
@app.route('/next1')
def index1():
    lst=[2,3,4,5,6,7,8]
    return render_template('dropdown.html',lst=lst)

@app.route('/table',methods=['GET','POST'])
def index2():
    val=request.form.get('mylist',type=int)
    return render_template('display.html',val=val)

if __name__=="__main__":
    app.run()
