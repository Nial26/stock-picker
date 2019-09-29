from datetime import datetime

class StockInfo:
    def __init__(self, name: str, date: datetime, price: float):
        self.name = name
        self.date = date
        self.price = price

    def __eq__(self, value):
        return value.name == self.name and self.date == value.date and self.price == value.price

    def __str__(self):
        return "Name: " + self.name + " Date: " + self.date + " Price: " + self.price

    @staticmethod
    def to_stock_info(data_row: list):
        if len(data_row) != 3:
            raise Exception("Invalid Data Row")
        name, date_str, price = data_row
        try:
            stock_date = datetime.strptime(date_str, "%d-%b-%Y")
        except ValueError:
            raise Exception("Invalid Date Format, Please Use 01-Jan-2013 Like Date format")
        return StockInfo(name.lower(), stock_date, float(price))
        
