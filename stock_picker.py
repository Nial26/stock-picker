import sys
from datetime import datetime
from statistics import mean, stdev
from typing import Dict, Tuple, Optional


from helpers.csv_utils import CSVFile
import helpers.input_helper as input_helper
from entities.stock_search_filter import StockSearchFilter
from services.stock_service import StockService


def main(file_name: str):

    stock_service = init(file_name)

    want_to_quit = False
    while not want_to_quit:
        mean, stddev, buying_date, selling_date, profit = handle_transaction(stock_service)
        print("Mean: ", mean, "Standard Deviation: ", stddev, "Buy Date: ", buying_date, "Selling Date: ", selling_date, "Profit from Doing the transaction with 100 Stocks: ", profit)
        print("Do you want to Continue: ([y]/n)")
        if input().lower() == "n":
            want_to_quit = True



def init(file_name: str) -> StockService:
    try:
        csv_util = CSVFile(file_name, True)
        csv_util.read_file()
    except FileNotFoundError:
        print("Please pass a fully qualified path name to the CSV file")
        sys.exit(2)

    header = csv_util.get_header()
    if header != ["StockName", "StockData", "StockPrice"]:
        print('Please provide a valid Stock Input File with "StockName", "StockData" and "StockPrice" as headers')
        sys.exit(2)

    data_rows = csv_util.get_data_rows()
    stocks_service = StockService(data_rows)
    return stocks_service
    
def handle_transaction(stocks_service: StockService) -> Tuple[float, Optional[float], datetime.date, datetime.date, float]:
    stock_search_filter = input_helper.get_stock_search_filter(stocks_service.get_unique_stock_names())
    stocks = stocks_service.get_stocks(stock_search_filter)
    stock_prices = [i.price for i in stocks]
    
    m = None
    s = None
    if len(stock_prices) >= 1:
        m = mean([i.price for i in stocks])
    if len(stock_prices) >= 2:
        s = stdev([i.price for i in stocks])
        
    buying_stock_info, sell_stock_info, profit_made = stocks_service.get_max_profit_period(stock_search_filter)

    return (m, s, buying_stock_info.date if buying_stock_info is not None else None, sell_stock_info.date if sell_stock_info is not None else None, profit_made * 100)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass a file as a command line argument")
        sys.exit(2)
    file_name = sys.argv[1]
    main(file_name)
