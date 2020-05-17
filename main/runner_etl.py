import logging
from app.etl.prepare_data import df
from app.db.cassandra_config import Cassandra

logging.basicConfig(filename='ETLlogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


def main():
    """
    Main script that performs the ETL
    """
    
    try:
        logging.info('Loading data into the tables')
        query_insert_stockss = "INSERT INTO stock " \
                                "(date, open, high, low, close, volume, ex_dividend, split_ratio, adj_open, adj_high, adj_low, adj_close, adj_volume) " \
                                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        prepared_stocks = c.session.prepare(query_insert_stockss)
        
        for index, row in df.iterrows():
            c.session.execute(prepared_stocks
                            , (row['date']
                               , row['open']
                               , row['high']
                               , row['low']
                               , row['close']
                               , row['volume']
                               , row['ex_dividend']
                               , row['split_ratio']
                               , row['adj_open']
                               , row['adj_high']
                               , row['adj_low']
                               , row['adj_close']
                               , row['adj_volume']),  timeout=None)
            
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