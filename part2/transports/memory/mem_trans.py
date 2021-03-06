# Apache Thrift Memory Transport in Python 

import pickle
from thrift.transport import TTransport

class Trade:
    def __init__(self):
        symbol=""
        price=0.0
        size=0

transport = TTransport.TMemoryBuffer()
trade = Trade()
trade.symbol = "F"
trade.price = 13.10
trade.size = 2500
transport.write(pickle.dumps(trade))

transport.cstringio_buf.seek(0)
bstr = transport.read(4096)
trade_read = pickle.loads(bstr)
print("Trade(%d): %s %d @ %f" % (len(bstr), trade_read.symbol, trade_read.size, trade_read.price))

