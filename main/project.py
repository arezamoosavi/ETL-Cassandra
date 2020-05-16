import logging
from db.cassandra_config import Cassandra
from db.dbModel import Stock

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
