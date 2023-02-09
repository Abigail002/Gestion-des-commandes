from msilib import Table
from multiprocessing import connection
from config import db
import enum
from sqlalchemy import Column, Enum, MetaData

class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

t = (
    'Order_status', MetaData(),
    Column('value', Enum(MyEnum))
)

connection.execute(t.insert(), {"value": MyEnum.two})
assert connection.scalar(t.select()) is MyEnum.two
    