import unittest
from unittest.mock import MagicMock
from flask_sqlalchemy import SQLAlchemy
from backend.app import app, db
from backend.services.modelService import ModelService
from backend.models.modelModel import Model

class TestModelService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuração inicial antes de todos os testes
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'  # Usando SQLite para testes
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['TESTING'] = True
        db.init_app(app)
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Limpar após todos os testes
        with app.app_context():
            db.drop_all()

    def setUp(self):
        # Configuração antes de cada teste
        with app.app_context():
            model1 = Model(name='Model A', max_token=100, min_token=10)
            model2 = Model(name='Model B', max_token=200, min_token=20)
            db.session.add(model1)
            db.session.add(model2)
            db.session.commit()

    def tearDown(self):
        # Limpar após cada teste
        with app.app_context():
            db.session.rollback()
            db.session.query(Model).delete()
            db.session.commit()

    def test_create_model(self):
        data = {
            'name': 'Model C',
            'max_token': 150,
            'min_token': 15
        }
        result = ModelService.create_model(**data)
        self.assertEqual(result['message'], 'Model created successfully')

    def test_get_all_models(self):
        result = ModelService.get_all_model()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)  # Assuming setUp adds two models

    def test_get_model(self):
        model = Model.query.filter_by(name='Model A').first()
        model_id = model.id if model else 1  # Fallback ID
        result = ModelService.get_model(model_id)
        self.assertEqual(result['name'], 'Model A')

    def test_update_model(self):
        model = Model.query.filter_by(name='Model B').first()
        model_id = model.id if model else 2  # Fallback ID
        data = {
            'name': 'Model B Updated',
            'max_token': 250,
            'min_token': 25
        }
        result = ModelService.update_model(model_id, **data)
        self.assertEqual(result['message'], 'Model updated successfully')

    def test_delete_model(self):
        model = Model.query.filter_by(name='Model A').first()
        model_id = model.id if model else 1  # Fallback ID
        result = ModelService.delete_model(model_id)
        self.assertEqual(result['message'], 'Model deleted successfully')

if __name__ == '__main__':
    unittest.main()
