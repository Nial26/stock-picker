import sys

from stock_search_filter import StockSearchFilter
from datetime import datetime

_GET_STOCK_NAME_MSG = "Please enter a Valid Stock Name: "
_WRONG_STOCK_NAME_RETRY_MSG = "This Stock Name is not present in the CSV File, Please enter one of the following Stock Names, which are present in the file: "
_DO_YOU_WANT_TO_CONTINUE = "Do you want to Continue? ([y]/n)"
_FROM_DATE_MSG = "From Which Date do you want to Start [Enter Date in format: 01-Jan-2019]: "
_TO_DATE_MSG = "Till Which Date do you want to Analyse [Enter Date in format: 01-Jan-2019]: "

def get_stock_search_filter(valid_stock_names: set) -> StockSearchFilter:
    """
    Handles all the messy details of getting the input from the User.
    Handles details like nagging the user until valid input, retry etc.
    """
    stock_name = _get_stock_name(valid_stock_names) # At this point we have a valid stock name
    from_date, to_date = _get_period()  # We have a valid from date
    return StockSearchFilter(stock_name, from_date, to_date)


def _get_stock_name(valid_stock_names: set):
    """
    Handles all the messy details of bugging the user until we get a valid stock name.
    Ideally should suggest the most approporiate Stock Symbols depending on the previous input, but for now
    spills it's guts out and shows all the valid symbol.
    """
    want_to_exit = False
    while not want_to_exit:
        print(_GET_STOCK_NAME_MSG)
        stock_name = input().lower()
        if stock_name not in valid_stock_names:
            print(_WRONG_STOCK_NAME_RETRY_MSG)
            print(valid_stock_names)
            print(_DO_YOU_WANT_TO_CONTINUE)
            if input().lower() == "n":
                want_to_exit = True
                sys.exit(0)
        else:
            return stock_name


def _get_period():
    from_date = _get_date(_FROM_DATE_MSG)
    to_date = _get_date(_TO_DATE_MSG)
    return (from_date, to_date)


def _get_date(msg: str):
    """
    Keeps on asking until we get a valid date, or the user wants to quite
    Might want to support auto-detecting the format eventually
    """
    want_to_exit = False
    while not want_to_exit:
        print(msg)
        date_str = input().lower()
        try:
            date = datetime.strptime(date_str, "%d-%b-%Y")
            return date
        except ValueError:
            print(
                "Date format was Invalid!! Please Enter date in DD-MON-YYYY [01-Jan-2019] Format")
            print(_DO_YOU_WANT_TO_CONTINUE)
            if input().lower() == "n":
                sys.exit(0)
