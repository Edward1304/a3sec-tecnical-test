# Services

Este directorio contiene dos programas : `auth_services.py` y `db_services.py`.

## auth_services.py

Este programa contiene la clase `AuthService`, que se encarga de la autenticación de usuarios utilizando ***JSON Web Tokens (JWT)***. Esta clase puede generar, decodificar y verificar tokens de autenticación.

Métodos principales:

- `generate_token(user_id)`: Genera un token de autenticación para un usuario.
- `decode_token(token)`: Decodifica un token de autenticación.
- `verify_token(token)`: Verifica la validez de un token de autenticación.

## db_services.py

Este módulo contiene la clase `MySQLDatabase`, que se encarga de manejar las operaciones de la base de datos MySQL.

Métodos principales:

- `register_user(name, email, password)`: Registra un nuevo usuario en la base de datos.
- `authenticate_user(email, password)`: Autentica a un usuario en la base de datos.
- `create_event(user_id, name, date, location, mode)`: Crea un nuevo evento en la base de datos.
- `get_event(id)`: Obtiene un evento de la base de datos.
- `add_event(user_id, name, date, location, mode)`: Añade un nuevo evento a la base de datos.
- `delete_event(id)`: Elimina un evento de la base de datos.
- `update_event(id, user_id, name, date, location, mode)`: Actualiza un evento en la base de datos.
- `get_user_events(user_id)`: Obtiene todos los eventos de un usuario de la base de datos.

Para más detalles, consulte el código fuente de cada módulo.