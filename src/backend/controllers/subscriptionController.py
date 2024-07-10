from services.subscriptionService import SubscriptionService
from flask import Blueprint, request, jsonify

subscription_bp = Blueprint('subscription_bp', __name__, url_prefix='/subscription')

@subscription_bp.route('/', methods=['POST'])
def create_subscription():
    data = request.json
    result = SubscriptionService.create_subscription(
        name=data.get('name'),
        price=data.get('price'),
        model_id=data.get('model_id'),
        active=data.get('active')
    )
    return jsonify(result)

@subscription_bp.route('/<int:subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
    result = SubscriptionService.get_subscription(subscription_id)
    return jsonify(result)

@subscription_bp.route('/', methods=['GET'])
def get_all_subscription():
    try:
        subs = SubscriptionService.get_all_subscription()
        return jsonify(subs)
    except Exception as e:
        return jsonify({"error": str(e)})

@subscription_bp.route('/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    data = request.json
    result = SubscriptionService.update_subscription(
        subscription_id,
        name=data.get('name'),
        price=data.get('price'),
        model_id=data.get('model_id'),
        active=data.get('active')
    )
    return jsonify(result)

@subscription_bp.route('/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    result = SubscriptionService.delete_subscription(subscription_id)
    return jsonify(result)
