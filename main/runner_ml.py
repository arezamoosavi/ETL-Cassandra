import os
import logging
from pandas import DataFrame
from app.db.cassandra_config import Cassandra

logging.basicConfig(filename='MLlogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")



def pandas_factory(colnames, rows):
    return DataFrame(rows, columns=colnames)





def main():
    """
    Main script that performs the ML
    """
    
    try:
        # c.session.row_factory = pandas_factory
        # c.session.default_fetch_size = 10000000 #needed for large queries, otherwise driver will do pagination. Default is 50000.
        # rows = c.session.execute("""select * from stock""")

        c.session.row_factory = pandas_factory
        c.session.default_fetch_size = None

        query = "SELECT * FROM {}.{};".format(c.key_space, os.getenv('CASSANDRA_TABLE'))
        rows = c.session.execute(query, timeout=None)
        
        df = rows._current_rows
        print(df.head())

        logging.info('Loading data into the tables')
            
    except Exception as e:
        print(e)

    finally:
        logging.info('Closing connection to Cassandra')
        c.session.shutdown()
        c.cluster.shutdown()


if __name__ == "__main__":
    try:
        c = Cassandra()
        
        main()


        exit(1)

    except Exception as e:

        logging.error('Error in ETLRUNNER! {}'.format(e))
        exit(0)