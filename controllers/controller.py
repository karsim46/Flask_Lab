from flask import render_template
from app import app
from models.games_list import orders
from models.games_list import orders_1

@app.route('/')
def index():
    return render_template('index.html', title='SSC Game shop', orders=orders)

@app.route('/order')
def order():
    return render_template('order.html', title='SSC Game shop', orders_1=orders_1)
        