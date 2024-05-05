from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
from utils.utils import token_required
from extensions import db, auth_service

# Creacionn del Blueprint de 'auth'
bp = Blueprint('auth', __name__)

@bp.route('/register/',methods=['GET','POST'])
def register():
    """
    Ruta para registrar un nuevo usuario. Si el método es POST, intenta registrar al usuario.
    Si el método es GET, muestra la página de registro.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if name and email and password:  
            db.register_user(name,email,password)
            return redirect(url_for('auth.login'))
        else:
            error = 'Por favor, completa todos los campos'
            return render_template('register.html', error=error)
    return render_template('register.html')

@bp.route('/login/',methods=['GET','POST'])
def login():
    """
    Ruta para iniciar sesión. Si el método es POST, intenta iniciar sesión con las credenciales proporcionadas.
    Si el método es GET, muestra la página de inicio de sesión.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            user = db.authenticate_user(email,password)
            if  user:
                token = auth_service.generate_token(user['user_id'])
                session['token'] = token  
                return redirect(url_for('events.event'))  
            else:
                error='Usuario o contraseña incorrectos'
                return render_template('login.html',error=error)
        else:
            error='Por favor, proporciona un email y una contraseña'
            return render_template('login.html',error=error)
    return render_template('login.html')

@bp.route('/logout/')
def logout():
    """
    Ruta para cerrar sesión. Elimina el token de la sesión y redirige al usuario a la página de inicio.
    """
    session.pop('token',None)
    return redirect(url_for('auth.index'))

@bp.route('/')
def index():
    token = session.get('token') if 'token' in session else None
    if token:
        try:
            user_id = auth_service.decode_token(token)['user_id']
            if user_id:
                events = db.get_user_events(user_id)
                return render_template('index.html',events=events)
        except Exception as e:
            return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))


@bp.route('/')
def home():
    """
    Ruta de inicio. Si el usuario está autenticado, redirige a la página de inicio.
    Si no, redirige a la página de inicio de sesión.
    """
    if 'token' in session:
        return redirect(url_for('auth.index'))
    else:
        return redirect(url_for('auth.login'))
