import MySQLdb
from config import DB_CONFIG


class DatabaseManager:
    @staticmethod
    def get_connection():
        return MySQLdb.connect(
            user=DB_CONFIG["USER"],
            password=DB_CONFIG["PASSWORD"],
            host=DB_CONFIG["HOST"],
            database=DB_CONFIG["DATABASE"],
        )

    @staticmethod
    def execute_query(
        query, params=(), fetch_one=False, fetch_all=False, return_last_id=False
    ):
        try:
            connection = DatabaseManager.get_connection()
            cursor = connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute(query, params)
            if return_last_id:
                connection.commit()
                result = cursor.lastrowid
            elif fetch_one:
                result = cursor.fetchone()
            elif fetch_all:
                result = cursor.fetchall()
            else:
                connection.commit()
                result = None

            cursor.close()
            connection.close()
            return result, None
        except Exception as e:
            return None, str(e)
