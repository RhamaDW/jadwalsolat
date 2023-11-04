from flask import Flask,render_template
from waktusholat import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

