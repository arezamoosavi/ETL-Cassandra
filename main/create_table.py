import logging
from app.db.cassandra_config import Cassandra


logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


def main():

    try:
        table_list = ['stock',]

        for table in table_list:
            drop_table = 'DROP TABLE IF EXISTS {table}'.format(table=table)
            c.session.execute(drop_table)

        create_appointments_table = "CREATE TABLE IF NOT EXISTS stock "\
                                    "(date timestamp" \
                                    ", open float" \
                                    ", high float" \
                                    ", low float" \
                                    ", close float" \
                                    ", volume float" \
                                    ", ex_dividend float" \
                                    ", split_ratio float" \
                                    ", adj_open float" \
                                    ", adj_high float" \
                                    ", adj_low float" \
                                    ", adj_close float" \
                                    ", adj_volume float" \
                                    ", PRIMARY KEY (date))"
                                    
        logging.info('Creating stock table in Cassandra')

        c.session.execute(create_appointments_table,  timeout=None)

        print("T","A"*8)

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

        logging.error('Error! {}'.format(e))
        exit(0)