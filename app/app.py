from routes import auth_routes, events_routes
from extensions import app, db, auth_service

# progrma principal

# Registrar los blueprints de auth y event en la aplicación
app.register_blueprint(auth_routes.bp)
app.register_blueprint(events_routes.bp)

# se verifica si el archivo es el principal para ejecutar la aplicación
if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración en el puerto 5000
    app.run(debug=True,port=5000)