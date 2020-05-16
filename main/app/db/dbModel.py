import os
from uuid import uuid4
from datetime import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns


class Stock(Model):
    __keyspace__ = os.getenv('CASSANDRA_KEY_SPACE')
    __table_name__ = 'stock'

    id = columns.Integer(primary_key=True)
    Date = columns.Date()
    Open = columns.Float()
    High = columns.Float()
    Low = columns.Float()
    Close = columns.Float()
    Volume = columns.Float()
    Ex_Dividend = columns.Float()
    Split_Ratio = columns.Float()
    Adj_Open = columns.Float()
    Adj_High = columns.Float()
    Adj_Low = columns.Float()
    Adj_Close = columns.Float()
    Adj_Volume = columns.Float()
    