from services.modelService import ModelService
from flask import Blueprint, request, jsonify

model_bp = Blueprint('model_bp', __name__, url_prefix='/model')

@model_bp.route('/', methods=['POST'])
def create_model():
    data = request.json
    result = ModelService.create_model(
        name=data.get('name'),
        max_token=data.get('max_token'),
        min_token=data.get('min_token')
    )
    return jsonify(result)

@model_bp.route('/<int:model_id>', methods=['GET'])
def get_model(model_id):
    result = ModelService.get_model(model_id)
    return jsonify(result)

@model_bp.route('/', methods=['GET'])
def get_all_model():
    try:
        models = ModelService.get_all_model()
        return jsonify(models)
    except Exception as e:
        return jsonify({"error": str(e)})

@model_bp.route('/<int:model_id>', methods=['PUT'])
def update_model(model_id):
    data = request.json
    result = ModelService.update_model(
        model_id,
        name=data.get('name'),
        max_token=data.get('max_token'),
        min_token=data.get('min_token')
    )
    return jsonify(result)

@model_bp.route('/<int:model_id>', methods=['DELETE'])
def delete_model(model_id):
    result = ModelService.delete_model(model_id)
    return jsonify(result)
