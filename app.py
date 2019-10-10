from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/Karina')
def Karina():
    return "Hello Karina"

if __name__=='__main__':
    app.run(debug=True)
