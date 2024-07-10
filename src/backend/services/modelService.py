from sqlalchemy.exc import SQLAlchemyError
from models.modelModel import Model

class ModelService:
    @staticmethod
    def create_model(name, max_token, min_token):
        from database.database import db  # Importação localizada
        try:
            new_model = Model(
                name=name,
                max_token=max_token,
                min_token=min_token
            )
            db.session.add(new_model)
            db.session.commit()
            return {"message": "Model created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_model(model_id):
        from database.database import db  # Importação localizada
        try:
            model = Model.query.get(model_id)
            if model:
                return model.to_dict()
            else:
                return {"error": "Model not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}
        
    @staticmethod
    def get_all_model():
        from database.database import db  # Importação localizada
        try:
            models = Model.query.all()
            return [model.to_dict() for model in models]
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_model(model_id, **kwargs):
        from database.database import db  # Importação localizada
        try:
            update_values = {key: value for key, value in kwargs.items() if value is not None}
            if update_values:
                Model.query.filter_by(id=model_id).update(update_values)
                db.session.commit()
                return {"message": "Model updated successfully"}
            else:
                return {"error": "No values provided for update"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_model(model_id):
        from database.database import db  # Importação localizada
        try:
            model = Model.query.get(model_id)
            if model:
                db.session.delete(model)
                db.session.commit()
                return {"message": "Model deleted successfully"}
            else:
                return {"error": "Model not found"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
