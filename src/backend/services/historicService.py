from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from models.historicModel import Historic

class HistoricService:
    @staticmethod
    def create_historic(user_id, subscription_id, total_price, payment_method, status):
        from database.database import db  # Importação localizada
        try:
            new_purchase = Historic(
                user_id=user_id,
                purchase_date=datetime.utcnow(),
                subscription_id=subscription_id,
                total_price=total_price,
                payment_method=payment_method,
                status=status
            )
            db.session.add(new_purchase)
            db.session.commit()
            return {"message": "Purchase history created successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def get_historic(historic_id):
        from database.database import db  # Importação localizada
        try:
            historic = Historic.query.get(historic_id)
            if historic:
                return historic.to_dict()
            else:
                return {"error": "Purchase history not found"}
        except SQLAlchemyError as e:
            return {"error": str(e)}
        
    @staticmethod
    def get_all_historic():
        from database.database import db  # Importação localizada
        try:
            historics = Historic.query.all()
            return [historic.to_dict() for historic in historics]
        except SQLAlchemyError as e:
            return {"error": str(e)}

    @staticmethod
    def update_historic(historic_id, **kwargs):
        from database.database import db
        try:
            update_values = {key: value for key, value in kwargs.items() if value is not None}
            if update_values:
                Historic.query.filter_by(id=historic_id).update(update_values)
                db.session.commit()
                return {"message": "Purchase history updated successfully"}
            else:
                return {"error": "No values provided for update"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    @staticmethod
    def delete_historic(historic_id):
        from database.database import db
        try:
            historic = Historic.query.get(historic_id)
            if historic:
                db.session.delete(historic)
                db.session.commit()
                return {"message": "Purchase history deleted successfully"}
            else:
                return {"error": "Purchase history not found"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
