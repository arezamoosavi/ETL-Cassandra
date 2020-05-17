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
                                "(Date, Open, High, Low, Close, Volume, Ex_Dividend, Split_Ratio, Adj_Open, Adj_High, Adj_Low, Adj_Close, Adj_Volume) " \
                                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        prepared_stocks = c.session.prepare(query_insert_stockss)
        
        for index, row in df.iterrows():
            c.session.execute(prepared_stocks
                            , (row['Date']
                               , row['Open']
                               , row['High']
                               , row['Low']
                               , row['Close']
                               , row['Volume']
                               , row['Ex_Dividend']
                               , row['Split_Ratio']
                               , row['Adj_Open']
                               , row['Adj_High']
                               , row['Adj_Low']
                               , row['Adj_Close']
                               , row['Adj_Volume']),  timeout=None)
            
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