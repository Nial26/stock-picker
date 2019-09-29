from stock_info import StockInfo
from stock_search_filter import StockSearchFilter
from typing import Dict, List, Set, Union

class StockService:
    def __init__(self, data_rows: list):
        self.stocks = self.convert_to_stocks(data_rows)
    
    def convert_to_stocks(self, data_rows: list) -> Dict[str, List[StockInfo]]:
        stocks = {}
        for row in data_rows:
            try:
                s = StockInfo.to_stock_info(row)
                stocks.setdefault(s.name, []).append(s)
            except Exception as e:
                print("Data Row ", row, " had this issue ", e, " so skipping...")
        return stocks

    def get_stocks(self, stock_search_filter: StockSearchFilter = None) -> Union[Dict[str, List[StockInfo]],List[StockInfo]] :
        if stock_search_filter == None:
            return self.stocks
        else:
            stocks_with_given_name = self.stocks[stock_search_filter.stock_name]
            to_return = []
            for stock in stocks_with_given_name:
                if stock.date >= stock_search_filter.from_date and stock.date < stock_search_filter.to_date:
                    to_return.append(stock)
            return to_return

    def get_unique_stock_names(self) -> Set[str]:
        return self.stocks.keys()
