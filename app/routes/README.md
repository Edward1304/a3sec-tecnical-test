# Routes

Esta carpeta contiene los archivos `auth_routes.py` y `events_routes.py`, los cuales definen las rutas para la autenticación de usuarios y la gestión de eventos, respectivamente.

---

### **auth_routes.py**
 Este progtrama ,estan las rutas para el  realizar el registro, login y el cierre de sesion y la pagina de inicio que se va mostrar.
- `@bp.route('/register/',methods=['GET','POST'])`: Esta ruta permite a los usuarios registrarse en la aplicación. Si el método es POST, intenta registrar al usuario. Si el método es GET, muestra la página de registro.

- `@bp.route('/login/',methods=['GET','POST'])`:Esta ruta permite a los usuarios iniciar sesión en la aplicación. Si el método es POST, intenta iniciar sesión con las credenciales proporcionadas. Si el método es GET, muestra la página de inicio de sesión.

- `@bp.route('/logout/')`:Esta ruta permite a los usuarios cerrar sesión. Elimina el token de la sesión y redirige al usuario a la página de inicio.

- `@bp.route('/')`: Esta ruta redirige a los usuarios a la página de inicio si están autenticados, de lo contrario, los redirige a la página de inicio de sesión.

---
### **events_routes.py**

Este programa, define las rutas para la visualización, actualización, adición y eliminación de eventos.

- `@bp.route('/event/')`: Esta ruta muestra los eventos de un usuario autenticado. Si el usuario no está autenticado, redirige a la página de inicio de sesión.

- `@bp.route('/update_event/<int:id>', methods=['POST'])`: Esta ruta permite a los usuarios actualizar un evento existente. Acepta un ID de evento como parámetro en la URL y recoge los datos del formulario para actualizar el evento en la base de datos.

- `@bp.route('/add_event', methods=['POST'])`: Esta ruta permite a los usuarios añadir un nuevo evento. Si el usuario está autenticado, recoge los datos del formulario y añade el evento a la base de datos. Si el usuario no está autenticado, redirige a la página de inicio de sesión.

- `@bp.route('/delete_event/<int:event_id>', methods=['POST'])`: Esta ruta permite a los usuarios eliminar un evento existente. Acepta un ID de evento como parámetro en la URL, elimina el evento de la base de datos y luego redirige a la página de inicio.

En este casos todas las rutas que requieren autenticación , si que se utilizan el decorador `@token_required` para asegurarse de que el usuario está autenticado antes de permitir el acceso a la ruta.

