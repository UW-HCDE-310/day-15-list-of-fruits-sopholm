from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    #return render_template("index.html", fruits=fruits)

#fruits that have more than 3 of
    fruits = [fruit for fruit in fruits if fruit["quantity"] > 3]
    return render_template("index.html", fruits=fruits)