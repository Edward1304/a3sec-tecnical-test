from datetime import datetime, timedelta
import jwt


class AuthService:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generate_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Su token ha expirado. Por favor, inicie sesión nuevamente.'
        except jwt.InvalidTokenError:
            return 'Su token es inválido. Por favor, inicie sesión nuevamente.'

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False
    
    
    