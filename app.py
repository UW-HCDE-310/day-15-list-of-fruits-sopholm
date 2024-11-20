from flask import Flask, render_template
import keys
app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    return render_template("index.html", fruits=fruits, key_1=MY_SECRET_API_KEY_1, key_2=MY_SECRET_API_KEY_2 )

#fruits that have more than 3 of
    #fruits = [fruit for fruit in fruits if fruit["quantity"] > 3]
    #return render_template("index.html", fruits=fruits)