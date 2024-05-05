from functools import wraps
from flask import session, jsonify
from services.auth_services import AuthService

# Llama la instancia de AuthService con una 'secretkey'
auth_service = AuthService('secretkey')

def token_required(f):
    """
    Decorador para requerir un token de autenticación en las rutas.
    Si el token no está presente, es inválido o ha expirado, devuelve un error 401.
    Si el token es válido, permite que la función decorada se ejecute normalmente.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = session.get('token')  # Obtiene el token de la sesión

        # Si no hay token, devuelve  error
        if not token:
            return jsonify({'message': 'Falta el token'}), 401

        try:
            # Trata de decodificar el token
            data = auth_service.decode_token(token)
            # Si el token es inválido o ha expirado, devolver error
            if isinstance(data, str):  
                return jsonify({'message': data}), 401
        except:
            # Si ocurre cualquier otro error al decodificar, devolver  error
            return jsonify({'message': 'Token invalido!'}), 401

        # Si todo va bien, ejecutar la función decorada
        return f(*args, **kwargs)

    return decorated