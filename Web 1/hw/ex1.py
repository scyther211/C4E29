from flask import Flask,redirect,render_template
app = Flask(__name__)

@app.route('/about-me/')
def about():
    return render_template("ex1.html")

@app.route('/school/')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)