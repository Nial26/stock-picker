import unittest
from datetime import datetime

from services.stock_service import StockService
from entities.stock_search_filter import StockSearchFilter
from entities.stock_info import StockInfo

class StockServiceTest(unittest.TestCase):
    
    def test_max_profit_period(self):
        data_rows = [['A', '01-Jan-2012', '100'], ['A', '02-Jan-2012', '95'], ['A', '04-Jan-2012', '100'], ['A', '03-Jan-2012', '96'],
                     ['A', '08-Jan-2012', '8'], ['A', '05-Jan-2012', '0'], ['A', '06-Jan-2012', '3'], ['A', '07-Jan-2012', '5']]
        s = StockService(data_rows)
        stock_search = StockSearchFilter('A', datetime.fromisoformat('2012-01-02'), datetime.fromisoformat('2012-02-01'))
        buy_stock, sell_stock, profit = s.get_max_profit_period(stock_search)
        self.assertEquals(buy_stock, StockInfo('a', datetime.fromisoformat('2012-01-05'), 0.0))
        self.assertEquals(sell_stock, StockInfo('a', datetime.fromisoformat('2012-01-08'), 8.0))
        self.assertEqual(profit, 8)


