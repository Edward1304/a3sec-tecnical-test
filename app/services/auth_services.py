from datetime import datetime, timedelta
import jwt 


class InvalidTokenError(Exception):
    pass

class ExpiredTokenError(Exception):
    pass


class AuthService:
    """
    AuthService es una clase para manejar la autenticación de los usuarios.
    Utiliza JSON Web Tokens (JWT) para generar y verificar tokens de autenticación.
    """

    def __init__(self, secret_key):
        """
         Se nicializa la clase AuthService con la clave secreta para codificar y decodificar los tokens.
        :param secret_key: La clave secreta para codificar y decodificar los tokens.
        """
        self.secret_key = secret_key

    def generate_token(self, user_id):
        """
        Genera un token de autenticación para un usuario.
        
        :param user_id: El ID del usuario para el que se generará el token.
        :return: Un token de autenticación codificado.
        """
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(3600)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def decode_token(self, token):
        """
        Decodifica un token de autenticación.
        
        :param token: El token de autenticación a decodificar.
        :return: El payload del token si es válido, o un mensaje de error si el token ha expirado o es inválido.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Su token ha expirado. Por favor, inicie sesión nuevamente.'
        except jwt.InvalidTokenError:
            return 'Su token es invalido. Por favor, inicie sesión nuevamente.'

    def verify_token(self, token):
        """
        Verifica la validez de un token de autenticación.
        
        :param token: El token de autenticación a verificar.
        :return: True si el token es válido, False si el token ha expirado o es inválido.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False