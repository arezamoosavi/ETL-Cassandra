import logging
from app.db.cassandra_config import Cassandra
from app.db.dbModel import Stock

#loging
logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


try:
    cassandra = Cassandra()
    cassandra.sync_table(database=Stock)

    logging.info('Connedted to Cassandra')

    obj = Stock.objects.all()
    print(list(obj))
    exit(1)

except Exception as e:

    logging.error('Error! {}'.format(e))
    exit(0)
