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
                                    "(Date timestamp" \
                                    ", Open float" \
                                    ", High float" \
                                    ", Low float" \
                                    ", Close float" \
                                    ", Volume float" \
                                    ", Ex_Dividend float" \
                                    ", Split_Ratio float" \
                                    ", Adj_Open float" \
                                    ", Adj_High float" \
                                    ", Adj_Low float" \
                                    ", Adj_Close float" \
                                    ", Adj_Volume float" \
                                    ", PRIMARY KEY (Date))"
        logging.info('Creating stock table in Cassandra')

        c.session.execute(create_appointments_table)

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