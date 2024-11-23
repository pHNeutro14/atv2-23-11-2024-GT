from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/arduino')
def arduino():
    return render_template('arduino.html')