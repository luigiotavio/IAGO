from flask import Blueprint, request, jsonify
from services.historicService import HistoricService

historic_bp = Blueprint('historic_bp', __name__, url_prefix='/historic')

@historic_bp.route('/', methods=['POST'])
def create_purchase_history():
    data = request.json
    result = HistoricService.create_historic(
        user_id=data.get('user_id'),
        subscription_id=data.get('subscription_id'),
        total_price=data.get('total_price'),
        payment_method=data.get('payment_method'),
        status=data.get('status')
    )
    return jsonify(result)

@historic_bp.route('/<int:historic_id>', methods=['GET'])
def get_purchase_history(historic_id):
    result = HistoricService.get_historic(historic_id)
    return jsonify(result)

@historic_bp.route('/', methods=['GET'])
def get_all_historics():
    try:
        historics = HistoricService.get_all_historic()
        return jsonify(historics)
    except Exception as e:
        return jsonify({"error": str(e)})

@historic_bp.route('/<int:historic_id>', methods=['PUT'])
def update_purchase_history(historic_id):
    data = request.json
    result = HistoricService.update_historic(
        historic_id,
        user_id=data.get('user_id'),
        subscription_id=data.get('subscription_id'),
        total_price=data.get('total_price'),
        payment_method=data.get('payment_method'),
        status=data.get('status')
    )
    return jsonify(result)

@historic_bp.route('/<int:historic_id>', methods=['DELETE'])
def delete_purchase_history(historic_id):
    result = HistoricService.delete_historic(historic_id)
    return jsonify(result)
