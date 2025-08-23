from Project_1 import Stock, Trade, activity, CustomEncoder
from json import JSONEncoder, JSONDecoder,dumps, loads
from datetime import date, datetime
from decimal import Decimal



encoded = dumps(activity, cls=CustomEncoder, indent=2)
print(encoded)

def decode_stock(d):
    # assumes "class": "Stock" is in the dictionary
    # and contains all the required serialized fields needed to re-create the object
    # if working in Python 3.7, we could use date.fromisoformat(d['date']) instead
    s = Stock(d['symbol'], 
              datetime.strptime(d['date'], '%Y-%m-%d').date(), 
              Decimal(d['open']), 
              Decimal(d['high']), 
              Decimal(d['low']), 
              Decimal(d['close']),
              int(d['volume']))
    return s


s = decode_stock({
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "object": "Stock"
    })

type(s), vars(s)

def decode_trade(d):
    # assumes "class": "Trade" is in the dictionary
    # and contains all the required serialized fields needed to re-create the object
    s = Trade(d['symbol'], 
              datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'), 
              d['order'], 
              Decimal(d['price']), 
              int(d['volume']), 
              Decimal(d['commission']))
    return s

t = decode_trade({
      "symbol": "TSLA",
      "timestamp": "2018-11-22T10:05:12",
      "order": "buy",
      "price": "338.25",
      "volume": 100,
      "commission": "9.99",
      "object": "Trade"
    })

type(t), vars(t)

def decode_financials(d):
    object_type = d.get('object', None)
    if object_type == 'Stock':
        return decode_stock(d)
    elif object_type == 'Trade':
        return decode_trade(d)
    return d 

decode_financials({
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "object": "Stock"
    })

class CustomDecoder(JSONDecoder):
    def decode(self, arg):
        data = loads(arg)
        # now we have to recursively look for `Trade` and `Stock` objects
        return self.parse_financials(data)
 
    def parse_financials(self, obj):
        if isinstance(obj, dict):
            obj = decode_financials(obj)
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = self.parse_financials(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.parse_financials(item)
        return obj
    

decoded = loads(encoded, cls=CustomDecoder)

