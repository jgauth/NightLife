import psycopg2, logging, datetime

# Logs

NIGHTLIFE_LOG = "../logs/nightlife.log"
LOG_TIME = datetime.datetime.now

# Our database credentials

# HOST = "nightlife-db.crtru8tqdhdu.us-west-2.rds.amazonaws.com" 
# PORT = "5432" 
# USER = "CIS422"
# DBNAME = "nightlifeDBd"
# PASSWORD = "Bnh8wMiz3J9Fpz9!j#*N16lgq8NDf%K#"
CONNECT_TIMEOUT = "5"

HOST = "db" 
PORT = "5432" 
USER = "john"
DBNAME = "john"
PASSWORD = "johnpassword"

conn_str = "dbname='%s' user='%s' host='%s' password='%s'" % (
    DBNAME, USER, HOST, PASSWORD, CONNECT_TIMEOUT)


class SqlParser:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def init(self):
        '''
        Set up logs, initialize database connection
        '''
        # logging.basicConfig(filename=NIGHTLIFE_LOG, level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logging.info("SQL Parser session initialized")
        # logging.error("SQL Parser session initialized")

        try:
            self.connection = psycopg2.connect(conn_str)
            self.cursor = self.connection.cursor()
            # logging.info("Established database connection")
            return True
        except (Exception, NameError, psycopg2.DatabaseError) as error:
            # logging.error("Connection to database failed: %s", error)
            return False

    def reset_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS events")
        self.cursor.execute("""
        CREATE TABLE events (
            id SERIAL PRIMARY KEY, 
            location GEOMETRY(Point) NOT NULL, 
            address VARCHAR(256) NOT NULL,
            name VARCHAR(64) NOT NULL,
            host VARCHAR(64) NOT NULL,
            time_start TIMESTAMP NOT NULL,
            time_end TIMESTAMP NOT NULL,
            theme VARCHAR(64),
            description VARCHAR(256)
            )""")
        self.connection.commit()

    def insert_event(self, lat, long, address, name, host, time_start, time_end, theme='NULL', description='NULL'):
        """
        lat, long - float
        address, name, host, time_start, time_end, theme, description - string 
        """
        self.cursor.execute("""
        INSERT INTO events (location, address, name, host, time_start, time_end, theme, description) VALUES (
            ST_GeomFromText('POINT({} {})'), #lat/long
            '{}', #address
            '{}', #name
            '{}', #host
            '{}', #time_start
            '{}', #time_end
            '{}', #theme
            '{}', #description
        )""".format(lat, long, address, name, host, time_start, time_end, theme='NULL', description='NULL'))

    def get_events_json(self):
