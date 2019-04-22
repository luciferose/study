import mysql.connector

class CredentialsError(Exception):
    pass

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configguration = config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = mysql.connector.connect(**self.configguration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
