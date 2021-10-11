import os
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from models import *
import sys

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

app = Flask(__name__)


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTION')
        return response

    @app.route('/')
    def init():
        # if os.environ.get('GAE_ENV') == 'standard':
        #     host = '/cloudsql/{}'.format(db_connection_name)
        # else:
        #     host = '127.0.0.1'

        # cnx = psycopg2.connect(dbname=db_name, user=db_user,
        #                     password=db_password, host=host)

        # with cnx.cursor() as cursor:
        #     cursor.execute('SELECT NOW() as now;')
        #     result = cursor.fetchall()

        # current_time = result[0][0]
        # cnx.commit()
        # cnx.close()

        sql = "SELECT NOW() as now;"
        try:
            data = DBUtil.call_raw_sql(sql)
            return jsonify({
                    'success': True,
                    'time': str(data)
                })
        except:
            msg = sys.exc_info()
            return jsonify({
                    'success': False, 
                    'message': str(msg)
                })

        # return str(current_time)
        # return jsonify({
        # 		'success': True,
        # 		'time': str(current_time)
        # 	})

    return app

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True)
