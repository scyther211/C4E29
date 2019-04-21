from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello dude"

@app.route('/say-hi')
def say_hi():
    return "Noob"

@app.route('/say-hi/<name>')
def say_hi_smb(name):
    return "Xin chao {}".format(name)

if __name__ == '__main__':
  app.run(debug=True)
 