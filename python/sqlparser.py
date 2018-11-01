import psycopg2, logging, datetime

# Logs

NIGHTLIFE_LOG = "../logs/nightlife.log"
LOG_TIME = datetime.datetime.now

# Our database credentials

HOST = "nightlife-db.crtru8tqdhdu.us-west-2.rds.amazonaws.com" 
PORT = "5432" 
USER = "CIS422"
DBNAME = "nightlifeDBd"
PASSWORD = "Bnh8wMiz3J9Fpz9!j#*N16lgq8NDf%K#"
CONNECT_TIMEOUT = "5"


class SqlParser:
    def __init__(self):
        self._connection = None
    def init(self):
        '''
        Set up logs, initialize database connection
        '''
        logging.basicConfig(filename=NIGHTLIFE_LOG, level=logging.INFO)
        logging.basicConfig(filename=NIGHTLIFE_LOG, level=logging.ERROR)
        logging.info(str(LOG_TIME())+": SQL Parser session initialized")
        logging.error(str(LOG_TIME())+": SQL Parser session initialized")

        try:
            connection = psycopg2.connect(dbname=DBNAME, user=USER, host=HOST, password=PASSWORD, connect_timeout=CONNECT_TIMEOUT)
            self._connection = connection
            self._cursor = self._connection.cursor()
            logging.info(str(LOG_TIME())+": Established database connection")
            return True
        except (Exception, NameError, psycopg2.DatabaseError) as error:
            logging.error(str(LOG_TIME())+": Connection to database failed: %s", error)
            return False
        
        


if __name__ == "__main__":
    parser = SqlParser()
    parser.init()