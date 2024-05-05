

class MySQLDatabase:
    def __init__(self,mysql):
        self.mysql = mysql
        
    def register_user(self,name,email,password):
        cursor = self.mysql.connection.cursor()
        cursor.execute('INSERT INTO users(name,email,password) VALUES(%s,%s,%s)',(name,email,password))
        self.mysql.connection.commit()
        cursor.close()
    
    def autenticate_user(self,email,password):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s',(email,password))
        user = cursor.fetchone()
        cursor.close()
        return user
    
    def create_event(self,user_id,name,date,location,mode):
        cursor = self.mysql.connection.cursor()
        cursor.execute('INSERT INTO events(user_id, name, date, location, mode) VALUES(%s,%s,%s,%s,%s)',(user_id, name, date, location, mode))
        self.mysql.connection.commit()
        cursor.close()
    
    def get_event(self,id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM events WHERE id=%s',(id,))
        event = cursor.fetchone()
        cursor.close()
        return event
    def add_event(self, user_id, name, date, location, mode):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO events(user_id, name, date, location, mode) VALUES(%s, %s, %s, %s, %s)", (user_id, name, date, location, mode))
        self.mysql.connection.commit()
        cur.close()
            
        
    def delete_event(self,id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('DELETE FROM events WHERE id=%s',(id,))
        self.mysql.connection.commit()
        cursor.close()
        
    def update_event(self, id, user_id, name, date, location, mode):
        cursor = self.mysql.connection.cursor()
        cursor.execute('UPDATE events SET user_id=%s, name=%s, date=%s, location=%s, mode=%s WHERE id=%s', (user_id, name, date, location, mode, id))
        self.mysql.connection.commit()
        cursor.close()

    def get_user_events(self,user_id):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM events WHERE user_id=%s',(user_id,))
        events = cursor.fetchall()
        cursor.close()
        return events
    