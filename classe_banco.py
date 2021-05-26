import mysql.connector

class UsaBanco:
    def __init__(self, config):
        self.config = config
        
    def __enter__(self):
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, ext_value, ext_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()