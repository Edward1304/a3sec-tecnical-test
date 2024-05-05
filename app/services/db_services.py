class MySQLDatabase:
    """
    MySQLDatabase es la  clase  que se usa para manejar las operaciones de la base de datos MySQL.
    """

    def __init__(self, mysql):
        """
        Inicializa la clase MySQLDatabase con una conexión a MySQL.

        :param mysql: La conexión a la base de datos MySQL.
        """
        self.mysql = mysql

    def register_user(self, name, email, password):
        """
        Registra un nuevo usuario en la base de datos.

        :param name: El nombre del usuario.
        :param email: El correo electrónico del usuario.
        :param password: La contraseña del usuario.
        """
        cursor = self.mysql.connection.cursor()
        cursor.execute('INSERT INTO users(name, email, password) VALUES(%s, %s, %s)', (name, email, password))
        self.mysql.connection.commit()
        cursor.close()

    def authenticate_user(self, email, password):
        """
        Autentica a un usuario en la base de datos.

        :param email: El correo electrónico del usuario.
        :param password: La contraseña del usuario.
        :return: Los datos del usuario si la autenticación es exitosa, None en caso contrario.
        """
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        cursor.close()
        return user

    def create_event(self, user_id, name, date, location, mode):
        """
        Crea un nuevo evento en la base de datos.

        :param user_id: El ID del usuario que crea el evento.
        :param name: El nombre del evento.
        :param date: La fecha del evento.
        :param location: La ubicación del evento.
        :param mode: El modo del evento (presencial /virtual).
        """
        cursor = self.mysql.connection.cursor()
        cursor.execute('INSERT INTO events(user_id, name, date, location, mode) VALUES(%s, %s, %s, %s, %s)', (user_id, name, date, location, mode))
        self.mysql.connection.commit()
        cursor.close()

    def get_event(self, id):
        """
        Obtiene un evento de la base de datos.

        :param id: El ID del evento.
        :return: Los datos del evento si se encuentra, None en caso contrario.
        """
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM events WHERE id=%s', (id,))
        event = cursor.fetchone()
        cursor.close()
        return event

    def add_event(self, user_id, name, date, location, mode):
        """
        Añade un nuevo evento a la base de datos.

        :param user_id: El ID del usuario que añade el evento.
        :param name: El nombre del evento.
        :param date: La fecha del evento.
        :param location: La ubicación del evento.
        :param mode: El modo del evento.
        """
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO events(user_id, name, date, location, mode) VALUES(%s, %s, %s, %s, %s)", (user_id, name, date, location, mode))
        self.mysql.connection.commit()
        cur.close()

    def delete_event(self, id):
        """
        Elimina un evento de la base de datos.

        :param id: El ID del evento.
        """
        cursor = self.mysql.connection.cursor()
        cursor.execute('DELETE FROM events WHERE id=%s', (id,))
        self.mysql.connection.commit()
        cursor.close()

    def update_event(self, id, user_id, name, date, location, mode):
        """
        Actualiza un evento en la base de datos.

        :param id: El ID del evento.
        :param user_id: El ID del usuario que actualiza el evento.
        :param name: El nuevo nombre del evento.
        :param date: La nueva fecha del evento.
        :param location: La nueva ubicación del evento.
        :param mode: El nuevo modo del evento.
        """
        cursor = self.mysql.connection.cursor()
        cursor.execute('UPDATE events SET user_id=%s, name=%s, date=%s, location=%s, mode=%s WHERE id=%s', (user_id, name, date, location, mode, id))
        self.mysql.connection.commit()
        cursor.close()

    def get_user_events(self, user_id):
        """
        Obtiene todos los eventos de un usuario de la base de datos.

        :param user_id: El ID del usuario.
        :return: Una lista de todos los eventos del usuario.
        """
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM events WHERE user_id=%s', (user_id,))
        events = cursor.fetchall()
        cursor.close()
        return events
    