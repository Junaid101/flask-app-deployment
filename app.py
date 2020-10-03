from flask import Flask
app = Flask(__name__)

@app.route('/moon')
def hello_moon():
    return 'Ami ekta baal! Hello World'

@app.route('/junaid')
def hello_junu():
    return 'Arro boto ekta baal! Hello World'

@app.route('/')
def hello_world():
    return 'shobai baal! Hello Wasdrld'