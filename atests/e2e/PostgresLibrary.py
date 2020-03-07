import psycopg2

from robot.api.deco import keyword

class PostgresLibrary:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self.connection = None

    @keyword(name="Connect Postgres")
    def connect_postgres(self, connection_string):
        self.connection = psycopg2.connect(connection_string)

    
    def query_postgres(self, sql_query):
        if not self.connection:
            raise Exception("Try Connect Postgres first.")

        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        query_results = cursor.fetchall()
        columns = [row[0] for row in cursor.description]
        return [{column: value for column, value in zip(columns, row)}
                for row in query_results]

    def disconnect_postgres(self):
        if not self.connection:
            raise Exception("Try Connect Postgres first.")
        self.connection.close()