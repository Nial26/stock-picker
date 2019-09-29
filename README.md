# Stock Picker

## Usage

```bash
python3 stock_picker.py <csv_file_name>
```

## High Level Overview

Folder Structure
```
stock_picker
    ├── README.md
    ├── entities
    │   ├── __init__.py
    │   ├── stock_info.py
    │   └── stock_search_filter.py
    ├── helpers
    │   ├── __init__.py
    │   ├── csv_utils.py
    │   └── input_helper.py
    ├── services
    │   ├── __init__.py
    │   └── stock_service.py
    ├── stock_picker.py
    ├── test_stocks.csv
    └── tests
        ├── csv_util_test.py
        ├── res
        │   ├── csv_test.csv
        │   └── csv_with_pipe_delimiter.csv
        └── stock_info_test.py
```

`stock_picker.py` is more of an orchestrator, which does some basic checks during initialization such as are the no. of arguments correct and so on and then it initializes the `StockService` using the data from the CSV file.
`input_helper.py` takes care of input handling, retries when the input is wrong etc., After reading all the input it returns a `StockSearchFilter`, which is passed on the `StockService#get_stocks`, which return the stock which matches the filter.
This data is then used back in the `stock_picker.py` to calculate interesting stuff on the data
