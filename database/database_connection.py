import pymysql
from pymysql.err import MySQLError

# function database connection
def get_database_connection():
    try:
        db = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            db='laroussi_database'
        )
        cursor = db.cursor()
        return db, cursor
    except MySQLError as e:
        print(f"Database connection failed: {e}")
        return None, None
