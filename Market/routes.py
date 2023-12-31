from Market import app
from flask import render_template
from Market.models import Item 
from Market.forms import RegisterForm


@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html",items=items)

@app.route('/register')
def resgister_page():
    form = RegisterForm()
    return render_template('register.html',form=form)

