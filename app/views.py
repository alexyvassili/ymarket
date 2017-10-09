from flask import render_template
import decimal
from app import app
from app.models import Product

import jinja2


def costformat(cost):
    return '{0:,}'.format(decimal.Decimal(cost)).replace(',', ' ')

jinja2.filters.FILTERS['costformat'] = costformat


@app.route('/')
@app.route('/index.html')
def index():
    products = Product.query.order_by(Product.id).all()
    return render_template("index.html",
                           title = 'Home',
                           products = products)


@app.route('/product/<int:product_id>')
def product(product_id):
    prod = Product.query.filter(Product.id == product_id).first_or_404()
    product_description = {
        'name': prod.name,
        'properties': prod.properties.split('\n'),
        'cost': prod.cost,
        'jpeg': prod.jpeg,
    }
    return render_template("product.html",
                           title = product_description['name'],
                           product = product_description)
