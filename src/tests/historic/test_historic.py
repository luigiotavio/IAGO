import unittest
from unittest.mock import MagicMock
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from backend.services.historicService import HistoricService
from backend.models.historicModel import Historic

class TestHistoricService(unittest.TestCase):

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
            historic1 = Historic(description='Event A')
            historic2 = Historic(description='Event B')
            db.session.add(historic1)
            db.session.add(historic2)
            db.session.commit()

    def tearDown(self):
        # Limpar após cada teste
        with app.app_context():
            db.session.rollback()
            db.session.query(Historic).delete()
            db.session.commit()

    def test_create_historic(self):
        data = {
            'description': 'Event C'
        }
        result = HistoricService.create_historic(**data)
        self.assertEqual(result['message'], 'Historic created successfully')

    def test_get_all_historics(self):
        result = HistoricService.get_all_historic()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)  # Assuming setUp adds two historics

    def test_get_historic(self):
        historic = Historic.query.filter_by(description='Event A').first()
        historic_id = historic.id if historic else 1  # Fallback ID
        result = HistoricService.get_historic(historic_id)
        self.assertEqual(result['description'], 'Event A')

    def test_update_historic(self):
        historic = Historic.query.filter_by(description='Event B').first()
        historic_id = historic.id if historic else 2  # Fallback ID
        data = {
            'description': 'Event B Updated'
        }
        result = HistoricService.update_historic(historic_id, **data)
        self.assertEqual(result['message'], 'Historic updated successfully')

    def test_delete_historic(self):
        historic = Historic.query.filter_by(description='Event A').first()
        historic_id = historic.id if historic else 1  # Fallback ID
        result = HistoricService.delete_historic(historic_id)
        self.assertEqual(result['message'], 'Historic deleted successfully')

if __name__ == '__main__':
    unittest.main()
