from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from controllers.historicController import historic_bp
# from controllers.modelController import model_bp
# from controllers.subscriptionController import subscription_bp
from controllers.userController import user_bp
from database.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0994@localhost/iago'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(user_bp)
# app.register_blueprint(subscription_bp, url_prefix='/subscriptions')
# app.register_blueprint(model_bp, url_prefix='/models')
# app.register_blueprint(historic_bp, url_prefix='/historics')

if __name__ == '__main__':
    app.run(debug=True)