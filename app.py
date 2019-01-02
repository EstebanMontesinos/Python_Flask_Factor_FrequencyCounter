from flask import Flask,request,request,render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/factor', methods=['GET', 'POST'])
def factor():
    primeN=False;
    numbers=[]
    if request.method=="POST":
        form=int(request.form['fact'])
        for i in range(1,form+1):
            if form % i==0:
                numbers.append(i)

        for i in range(2,form):
            if form % i==0:
                primeN=True

    return render_template('factor.html',form=numbers,primeN=primeN)


@app.route('/wordcount.html', methods=['GET', 'POST'])
def word():
    frequency={}
    if request.method=='POST':
        word=request.form['words']
        lines=word.split('\n')
        for line in lines:
            words=line.strip().split(' ')
            for word in words:
                if word not in frequency:
                    frequency[word]=1
                elif word in frequency:
                    frequency[word]+=1

    return render_template('wordcount.html',frequency=frequency)





app.run(debug=True)