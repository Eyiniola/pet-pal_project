#!/usr/bin/python3

from flask import request, jsonify, Blueprint
from ..services.accessory_service import AccesoryServices


accesory = Blueprint('accesory', __name__, url_prefix='/accesory')

@accesory.route('/accesories', methods=['GET'])
def get_all_toys():
    accesories = AccesoryServices.get_all_toys()
    return jsonify([accesory.__dict__ for accesory in accesories])

@accesory.route('/shopping', methods=['GET'])
def get_shopping_cart():
    cart = AccesoryServices.get_shopping_cart()
    return jsonify([item.__dict__ for item in cart])

@accesory.route('/shopping/add', methods=['POST'])
def add_to_cart():
    user_id = request.json['user_id']
    item_id = request.json['item_id']
    quantity = request.json['quantity']
    price = request.json['price']
    cart_item = AccesoryServices.add_to_cart(user_id, item_id, quantity, price)
    return jsonify(cart_item.__dict__)

@accesory.route('/shopping/remove', methods=['DELETE'])
def remove_from_cart():
    item_id = request.json['item_id']
    cart_item = AccesoryServices.remove_from_cart(item_id)
    return jsonify(cart_item.__dict__)

@accesory.route('/shopping/checkout', methods=['POST'])
def checkout():
    user_id = request.json['user_id']
    AccesoryServices.checkout(user_id)
    return jsonify({'message': 'Checkout successful'})

@accesory.route('/shopping/update', methods=['PUT'])
def update_cart():
    item_id = request.json['item_id']
    quantity = request.json['quantity']
    cart_item = AccesoryServices.update_cart(item_id, quantity)
    return jsonify(cart_item.__dict__)

