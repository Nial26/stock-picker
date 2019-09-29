import unittest
from entities.stock_info import StockInfo
from datetime import datetime

class TestStockInfo(unittest.TestCase):

    def test_creation_of_stock_info_from_data_row(self):
        data_row = ["ABC", "01-JAN-2013", "20.345"]
        stock = StockInfo.to_stock_info(data_row)
        self.assertEqual(stock, StockInfo("abc", datetime.fromisoformat("2013-01-01"), 20.345))