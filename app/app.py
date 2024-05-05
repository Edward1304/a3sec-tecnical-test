from routes import auth_routes, events_routes
from extensions import app, db, auth_service

app.register_blueprint(auth_routes.bp)
app.register_blueprint(events_routes.bp)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
    