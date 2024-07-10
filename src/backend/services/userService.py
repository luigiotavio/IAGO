from sqlalchemy.exc import SQLAlchemyError
from models.userModel import User

class UserService:
    @staticmethod
    def create_user(name, email, occupation, cell, age, gender, subscription_id, role):
        from database.database import db  # Importação localizada
        try:
            new_user = User(
                name=name,
                email=email,
                occupation=occupation,
                cell=cell,
                age=age,
                gender=gender,
                subscription_id=subscription_id,
                role=role
            )
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_all_user():
        from database.database import db  # Importação localizada
        try:
            users = User.query.all()
            return [user.to_dict() for user in users]
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def get_user(user_id):
        from database.database import db  # Importação localizada
        try:
            user = User.query.get(user_id)
            if user:
                return user.to_dict()
            else:
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_user(user_id, name, email, occupation, cell, age, gender, subscription_id, role):
        from database.database import db  # Importação localizada
        try:
            user = User.query.get(user_id)
            if user:
                user.name = name
                user.email = email
                user.occupation = occupation
                user.cell = cell
                user.age = age
                user.gender = gender
                user.subscription_id = subscription_id
                user.role = role
                db.session.commit()
                return {"message": "User updated successfully"}
            else:
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_user(user_id):
        from database.database import db  # Importação localizada
        try:
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                return {"message": "User deleted successfully"}
            else:
                return {"error": "User not found"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
