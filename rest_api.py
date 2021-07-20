from flask import Flask
from flask import request
from product_dao import *
import json
import sqlite3

app = Flask(__name__)


@app.route('/product/', methods=['GET', 'POST'])
def get_product():
    conn = sqlite3.connect('products.db')

    if request.method == 'GET':
        results = get_all_products(conn)
        json_list = []

        for e in results:
            json_list.append(json.dumps(e.__dict__))

        return json.dumps(json_list)

    if request.method == 'POST':
        obj = request.get_json()
        e = Product(id, obj['name'], obj['price'], obj['quantity'])
        insert_new_product(conn, e)

        return 'success'


@app.route('/product/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def product_by_id(id):
    conn = sqlite3.connect('products.db')

    if request.method == 'GET':
        result = get_product_by_id(conn, id)

        return json.dumps(result.__dict__)

    if request.method == 'DELETE':
        delete_product_by_id(conn, id)

        return 'success'

    if request.method == 'PUT':
        obj = request.get_json()

        e = Product(id, obj['name'], obj['price'], obj['quantity'])
        update_product_by_id(conn, e, id)

        return 'success'


app.run()
