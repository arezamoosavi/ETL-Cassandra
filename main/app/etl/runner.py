import logging
from .cassandra.cassandra_config import Cassandra
from .cassandra.dbModel import Stock

#loging
logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


# Connect and Sync
cassandra = Cassandra()
cassandra.sync_table(database=Stock)

logging.info('Connedted to Cassandra')

obj = Stock.objects.all()
print(list(obj))

exit()
