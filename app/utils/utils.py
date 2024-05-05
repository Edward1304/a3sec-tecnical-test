from functools import wraps
from flask import session, jsonify
from services.auth_services import AuthService

auth_service = AuthService('secretkey')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = session.get('token')

        if not token:
            return jsonify({'message': 'Falta el token'}), 401

        try:
            data = auth_service.decode_token(token)
            if isinstance(data, str):  #si el token es invalido o expirado
                return jsonify({'message': data}), 401
        except:
            return jsonify({'message': 'Token invalido!'}), 401

        return f(*args, **kwargs)

    return decorated