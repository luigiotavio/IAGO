import unittest
from unittest.mock import MagicMock
from flask_sqlalchemy import SQLAlchemy
from backend.app import app, db
from backend.services.userService import UserService
from backend.models.userModel import User


class TestUserService(unittest.TestCase):
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
            user1 = User(name='Alice', email='alice@example.com')
            user2 = User(name='Bob', email='bob@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

    def tearDown(self):
        # Limpar após cada teste
        with app.app_context():
            db.session.rollback()
            db.session.query(User).delete()
            db.session.commit()

    def test_create_user(self):
        data = {
            'name': 'Charlie',
            'email': 'charlie@example.com',
            'occupation': 'Developer',
            'cell': '+1234567890',
            'age': 30,
            'gender': 'Male',
            'subscription_id': 1,
            'role': 'Admin'
        }
        result = UserService.create_user(**data)
        self.assertEqual(result['message'], 'User created successfully')

    def test_get_all_users(self):
        result = UserService.get_all_user()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)  # Assuming setUp adds two users

    def test_get_user(self):
        user = User.query.filter_by(name='Alice').first()
        user_id = user.id if user else 1  # Fallback ID
        result = UserService.get_user(user_id)
        self.assertEqual(result['name'], 'Alice')

    def test_update_user(self):
        user = User.query.filter_by(name='Bob').first()
        user_id = user.id if user else 2  # Fallback ID
        data = {
            'name': 'Bobby',
            'email': 'bobby@example.com',
            'occupation': 'Designer',
            'cell': '+9876543210',
            'age': 25,
            'gender': 'Female',
            'subscription_id': 2,
            'role': 'User'
        }
        result = UserService.update_user(user_id, **data)
        self.assertEqual(result['message'], 'User updated successfully')

    def test_delete_user(self):
        user = User.query.filter_by(name='Alice').first()
        user_id = user.id if user else 1  # Fallback ID
        result = UserService.delete_user(user_id)
        self.assertEqual(result['message'], 'User deleted successfully')

if __name__ == '__main__':
    unittest.main()
