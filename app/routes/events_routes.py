from flask import Blueprint, render_template, request, redirect, url_for, session
from utils.utils import token_required
from extensions import db, auth_service

bp = Blueprint('events', __name__)





@bp.route('/event/')
@token_required
def event():
    token = session.get('token')  # Obtener el token de la sesión
    user_id = auth_service.decode_token(token)['user_id']
    if user_id:
        events = db.get_user_events(user_id)
        return render_template('event.html',events=events)
    return redirect(url_for('login'))

@bp.route('/update_event/<int:id>', methods=['POST'])
def update_event(id):
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    mode = request.form['mode']
    user_id = 1  # Aquí puedes obtener el ID del usuario de la sesión o de donde sea que lo estés almacenando

    db.update_event(id, user_id, name, date, location, mode)

    return render_template('index.html')  # Aquí puedes redirigir a donde quieras después de actualizar el evento

@bp.route('/add_event', methods=['POST'])
@token_required
def add_event():
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    mode = request.form['mode']
    token = session.get('token')  # Obtener el token de la sesión
    user_id = auth_service.decode_token(token)['user_id']
    if user_id:
        db.add_event(user_id, name, date, location, mode)
        return redirect(url_for('events.event'))  # Redirigir a la página de eventos
    return redirect(url_for('login'))  # Si no hay un usuario autenticado, redirigir a la página de inicio de sesión

@bp.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(id):
    db.delete_event(id)
    return render_template('index.html')  # Aquí puedes redirigir a donde quieras después de eliminar el evento
