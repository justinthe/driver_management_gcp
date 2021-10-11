import os
from datetime import datetime 
from sqlalchemy import Column, String, Integer, create_engine, Boolean, \
        ForeignKey, DateTime, func, text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import json


db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
# db_path = "postgresql+pg8000://{}:{}@/{}?unix_sock=cloudsql/{}/.s.PGSQL.5432".format(db_user, db_password, db_name, db_connection_name)
db_path = "postgresql://{}:{}@/{}?host=/cloudsql/{}".format(db_user, db_password, db_name, db_connection_name)

db = SQLAlchemy()

def setup_db(app, database_path=db_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    db.app = app
    db.init_app(app)
    db.create_all()


class DBUtil():
    def call_raw_sql(sql):
        statement = text(sql)
        data = db.session.execute(statement)
        db.session.commit()
        return data
