#!/usr/bin/python3

from flask import request, jsonify, Blueprint
from services.adopt_service import AdoptServices

adopt = Blueprint('adopt', __name__, url_prefix='/adopt')

@adopt.route('/pets', methods=['GET'])
def get_pets():
    pets = AdoptServices.get_pets()
    return jsonify([pet.__dict__ for pet in pets])

@adopt.route('/shopping', methods=['GET'])
def get_shopping_cart():
    cart = AdoptServices.get_shopping_cart()
    return jsonify([item.__dict__ for item in cart])

@adopt.route('/shopping/add', methods=['POST'])
def add_to_cart():
    user_id = request.json['user_id']
    item_id = request.json['item_id']
    quantity = request.json['quantity']
    price = request.json['price']
    cart_item = AdoptServices.add_to_cart(user_id, item_id, quantity, price)
    return jsonify(cart_item.__dict__)

@adopt.route('/shopping/remove', methods=['DELETE'])
def remove_from_cart():
    user_id = request.json['user_id']
    item_id = request.json['item_id']
    cart_item = AdoptServices.remove_from_cart(user_id, item_id)
    return jsonify(cart_item.__dict__)

@adopt.route('/shopping/checkout', methods=['POST'])
def checkout():
    user_id = request.json['user_id']
    AdoptServices.checkout(user_id)
    return jsonify({'message': 'Checkout successful'})

@adopt.route('/shopping/update', methods=['PUT'])
def update_cart():
    user_id = request.json['user_id']
    item_id = request.json['item_id']
    quantity = request.json['quantity']
    cart_item = AdoptServices.update_cart(user_id, item_id, quantity)
    return jsonify(cart_item.__dict__)
