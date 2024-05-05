from flask import Blueprint, render_template, request, redirect, url_for, session
from utils.utils import token_required
from extensions import db, auth_service

# Crear un nuevo Blueprint con el nombre 'events'
bp = Blueprint('events', __name__)

@bp.route('/event/')
@token_required
def event():
    """
    Ruta para mostrar los eventos de un usuario. Requiere autenticación.
    Si el usuario está autenticado, muestra sus eventos.
    Si no, redirige a la página de inicio de sesión.
    """
    token = session.get('token')  # Obtener el token de la sesión
    user_id = auth_service.decode_token(token)['user_id']
    if user_id:
        events = db.get_user_events(user_id)
        return render_template('event.html',events=events)
    return redirect(url_for('login'))

@bp.route('/update_event/<int:id>', methods=['POST'])
def update_event(id):
    """
    Ruta para actualizar un evento existente. Acepta un ID de evento como parámetro en la URL.
    Recoge los datos del formulario y llama a la función de actualización de la base de datos.
    """
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    mode = request.form['mode']
    user_id =  1 

    db.update_event(id, user_id, name, date, location, mode)

    return render_template('index.html') 

@bp.route('/add_event', methods=['POST'])
@token_required
def add_event():
    """
    Ruta para añadir un nuevo evento. Requiere autenticación.
    Si el usuario está autenticado, recoge los datos del formulario y llama a la función de añadir de la base de datos.
    Si no, redirige a la página de inicio de sesión.
    """
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
    """
    Ruta para eliminar un evento existente. Acepta un ID de evento como parámetro en la URL.
    Llama a la función de eliminación de la base de datos y luego redirige a la página de inicio.
    """
    db.delete_event(id)
    return render_template('index.html')  # Aquí puedes redirigir a donde quieras después de eliminar el evento