from flask_mysqldb import MySQL
from services.auth_services import AuthService
from services.db_services import MySQLDatabase
from flask import Flask

# Se crea  la instancia de la aplicación Flask
app = Flask(__name__)
# Se configura la clave secreta de la aplicación
app.secret_key = 'secretkey'

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_PORT'] = 3306  # Opción para configurar el puerto, relacionado con el despliegue en Docker hecho 
app.config['MYSQL_USER']= 'abc_group'  # Nombre de usuario de la base de datos
app.config['MYSQL_PASSWORD'] = '123abc'  # Contraseña dela base de datos
app.config['MYSQL_DB']='events_abc_db'  # Nombre  de base de datos
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Configuracion del cursor para devolver los resultados como diccionarios

# Se Crea la  instancia de MySQL con la configuración de la aplicación
mysql = MySQL(app)
# Se crea la instancia de MySQLDatabase con la instancia de MySQL
db=MySQLDatabase(mysql)

# Se crea la  instancia de AuthService con la clave secreta de la aplicación
auth_service = AuthService(app.secret_key)