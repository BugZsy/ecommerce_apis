import psycopg2
from psycopg2.extensions import Binary
class database_connection():
    conn = psycopg2.connect(database = 'DATABASE',user = 'postgres',password = '123456789',host = 'Localhost',port = '5432')
    def create_cursor(self):
        cursor = database_connection.conn.cursor()
        return cursor