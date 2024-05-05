from flask_mysqldb import MySQL
from services.auth_services import AuthService
from services.db_services import MySQLDatabase
from flask import Flask

app = Flask(__name__)
app.secret_key = 'abc123'

app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER']= 'abc_group'
app.config['MYSQL_PASSWORD'] = '123abc'
app.config['MYSQL_DB']='events_abc_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
db=MySQLDatabase(mysql)

auth_service = AuthService(app.secret_key)