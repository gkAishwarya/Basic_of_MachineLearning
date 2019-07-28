from flask import Flask,render_template,request
from random import choice

quotes = "Nothing is as easy as it looks",\
"Everything takes longer than you think",\
"Anything that can go wrong will go wrong",\
"If there is a possibility of several things going wrong,the one that will cause the most damage will be the one to go wrong",\
"If there is a worse time for something to go wrong,it will happen then",\
"If anything simply cannot go wrong,it will anyway",\
"If you perceive that there are four possible ways in which a procedure can go wrong,and will promptly develop",\
"Left to themselves, things tend to go from bad to worse",\
"If everything seems to be going well, you have obviously overlooked something",\
"Nature always sides with the hidden flaw",\
"It is impossible to make anything foolproof because fools are so ingenious",\
"Whenever you set out to do something, something else must be done first",\
"Every solution breeds new problems",\
"Trust everybody ,then cut the cards",\
"Two wrongs are only the beginning",\
"If at first you don't succeed, destroy all evidence that you tried",\
"To succeed in politics, it is often necessary to rise above your principles",\
"Exceptions prove the rule, and wreck the budget",\
"Success always occurs in private, and failure in full view"

str=choice(quotes)

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def index1():
    return render_template('gamepage.html',str=str)

@app.route('/next',methods=['GET','POST'])
def index2():
    lin = request.form.get('lines')
    wd = request.form.get('words')
    chac = request.form.get('chart')
    a=len(str)
    b=len(str.split(' '))
    c=len(str.split('\n'))
    d=a-(b-1)
    if int(lin)==c and int(wd)==b and int(chac)==d:
        return render_template('game_res.html')
    else:
        return render_template('game_fail.html')

@app.route('/timeup')
def index3():
    return "TIME UP!!\nFAIL..."

if __name__=="__main__":
    app.run()
