import json
from flask import Flask, request, jsonify
from sql_connector import get_sql_connector

import product_dao
import orders_dao
import uom_dao

connection = get_sql_connector()
app = Flask(__name__)

@app.route('/getProducts')
def get_products():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = product_dao.insert_new_products(connection, request_payload)
    response = jsonify({
        'product_id':product_id
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id':order_id
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id':return_id
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting python Flask server for Grocery Store management system.")
    app.run(port=5000)