from mysql import connector
from database import DB_CONFIG

class Connection:
    def __enter__(self):
        self.conn = connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)
        return self.conn, self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()