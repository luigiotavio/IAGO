import unittest
from unittest.mock import MagicMock
from flask_sqlalchemy import SQLAlchemy
from backend.app import app, db
from backend.services.subscriptionService import SubscriptionService
from backend.models.subscriptionModel import Subscription

class TestSubscriptionService(unittest.TestCase):

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
            sub1 = Subscription(name='Basic', price=10, model=1, active=True)
            sub2 = Subscription(name='Premium', price=20, model=2, active=True)
            db.session.add(sub1)
            db.session.add(sub2)
            db.session.commit()

    def tearDown(self):
        # Limpar após cada teste
        with app.app_context():
            db.session.rollback()
            db.session.query(Subscription).delete()
            db.session.commit()

    def test_create_subscription(self):
        data = {
            'name': 'Gold',
            'price': 30,
            'model': 3,
            'active': True
        }
        result = SubscriptionService.create_subscription(**data)
        self.assertEqual(result['message'], 'Subscription created successfully')

    def test_get_all_subscriptions(self):
        result = SubscriptionService.get_all_subscriptions()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)  # Assuming setUp adds two subscriptions

    def test_get_subscription(self):
        subscription = Subscription.query.filter_by(name='Basic').first()
        subscription_id = subscription.id if subscription else 1  # Fallback ID
        result = SubscriptionService.get_subscription(subscription_id)
        self.assertEqual(result['name'], 'Basic')

    def test_update_subscription(self):
        subscription = Subscription.query.filter_by(name='Premium').first()
        subscription_id = subscription.id if subscription else 2  # Fallback ID
        data = {
            'name': 'Premium Plus',
            'price': 25,
            'model': 3,
            'active': False
        }
        result = SubscriptionService.update_subscription(subscription_id, **data)
        self.assertEqual(result['message'], 'Subscription updated successfully')

    def test_delete_subscription(self):
        subscription = Subscription.query.filter_by(name='Basic').first()
        subscription_id = subscription.id if subscription else 1  # Fallback ID
        result = SubscriptionService.delete_subscription(subscription_id)
        self.assertEqual(result['message'], 'Subscription deleted successfully')

if __name__ == '__main__':
    unittest.main()
