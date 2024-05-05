from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
from utils.utils import token_required
from extensions import db, auth_service

bp = Blueprint('auth', __name__)


@bp.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if name and email and password:  # Asegurarse de que name, email y password no sean nulos
            db.register_user(name,email,password)
            return redirect(url_for('auth.login'))
        else:
            error = 'Por favor, completa todos los campos'
            return render_template('register.html', error=error)
    return render_template('register.html')

@bp.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            user = db.autenticate_user(email,password)
            if  user:
                token = auth_service.generate_token(user['user_id'])
                session['token'] = token  # Guardar el token en la sesión
                return redirect(url_for('events.event'))  # Redirigir a la página de eventos
            else:
                error='Usuario o contraseña incorrectos'
                return render_template('login.html',error=error)
        else:
            error='Por favor, proporciona un email y una contraseña'
            return render_template('login.html',error=error)
    return render_template('login.html')




@bp.route('/logout/')
def logout():
    session.pop('token',None)
    return redirect(url_for('auth.index'))



''''
#@bp.route('/')
#@token_required
#ef index():
#    token = session.get('token')  # obtener el token de la sesión
#    user_id = auth_service.decode_token(token)['user_id']
#    if user_id:
#        events = db.get_user_events(user_id)
#        return render_template('index.html',events=events)
#    return redirect(url_for('auth.login'))
'''


@bp.route('/')
def home():
    if 'token' in session:
        return redirect(url_for('auth.index'))
    else:
        return redirect(url_for('auth.login'))