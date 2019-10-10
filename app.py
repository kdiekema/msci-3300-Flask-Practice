from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle ='My Calculator')

@app.route('/Karina')
def Karina():
    return render_template('karina.html', pageTitle = 'Karina')

if __name__=='__main__':
    app.run(debug=True)
