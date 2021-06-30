from flask import render_template
from app import app
from models.games_list import orders

@app.route('/')
def index():
    return render_template('index.html', title='SSC Game shop', orders=orders)