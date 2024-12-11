from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/arduino')
def arduino():
    return render_template('arduino.html')

@app.route('/protoboard')
def protoboard():
    return render_template('protoboard.html')

@app.route('/pic16f628')
def pic16f628():
    return render_template('pic16f628.html')

@app.route('/raspberry')
def raspberry():
    return render_template('raspberry.html')