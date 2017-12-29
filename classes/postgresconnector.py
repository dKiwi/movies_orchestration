import psycopg2


class PostgresConnector:
    def __init__(self, host, user, password, db, query):
        self.hostname = host
        self.username = user
        self.password = password
        self.database = db
        self.query = query
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(host=self.hostname,
                                     user=self.username,
                                     password=self.password,
                                     dbname=self.database)

    def disconnect(self):
        if self.conn:
            self.conn.close()


class PostgresSelector(PostgresConnector):
    @property
    def selected(self):
        if self.query[:6].lower() == 'select':
            self.connect()
            cur = self.conn.cursor()
            cur.execute(self.query)
            values = cur.fetchall()
            self.disconnect()
            return values
        else:
            raise Exception("Not a select statement")


class PostgresInserter(PostgresConnector):
    def insert(self):
        if self.query[:6].lower() == 'insert':
            self.connect()
            cur = self.conn.cursor()
            cur.execute(self.query)
            self.conn.commit()
            self.disconnect()
        else:
            raise Exception("Not an insert statement")
