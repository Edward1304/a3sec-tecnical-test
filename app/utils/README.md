# utils.py

Este programa contiene una función decoradora `token_required` que se utiliza para requerir un token de autenticación en las rutas de una aplicación Flask.

## AuthService

al inicio del programa, se crea una instancia de `AuthService` con una ***'secretkey'***. `AuthService` es una clase importada del módulo `services.auth_services` que se utiliza para manejar la autenticación.

## token_required

`token_required` es una función decoradora que se puede aplicar a cualquier ruta en la aplicación Flask para requerir un token de autenticación. Cuando se llama a una ruta decorada con `token_required`, la función primero intenta obtener el token de la sesión. Si no hay token, devuelve un ***error 401*** con el mensaje ***'Falta el token'***.

Si hay un token, la función intenta decodificarlo utilizando el método `decode_token` de `auth_service`. Si el token es inválido o ha expirado (lo que se indica si `decode_token` devuelve una cadena), la función devuelve un ***error 401*** con el mensaje correspondiente.

Si el token es válido, la función decorada se ejecuta normalmente. Si ocurre cualquier otro error al decodificar el token, la función devuelve un ***error 401*** con el mensaje ***'Token invalido!'***.