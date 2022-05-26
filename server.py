from flask import Flask, render_template,request, redirect,session

app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit',methods=['POST'])
def submit():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['favlang']=request.form['favlang']
    session['comments']=request.form['comments']
    session['gridRadios']=request.form['gridRadios']
    
    if request.form.get('notif')==None:
        session['notif']=" You will NOT NOT receive Coding Dojo Notifications"
    else:
        session['notif']="You subscribed to receive Coding Dojo Notifications"
    if request.form.get('20min')==None:
        session['20min']=" You Dont agree on the 20 minutes rule"
    else:
        session['20min']="You  agree on the 20 minutes rule"
    
    print(session)
    return render_template("submit.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)