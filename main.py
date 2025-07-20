from flask import Flask, render_template, redirect

app = Flask(__name__)

vars = {
    'name':'Bimbo!'
    }

@app.route("/") # Route decorator
def home():
    return render_template("base.html", vars=vars)

if __name__ == "__main__":
    app.run(debug=True)