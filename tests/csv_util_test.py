import unittest
import csv_utils
import os

class TestCSVMethods(unittest.TestCase):

    def test_reading_csv(self):
        file_path = os.getcwd() + "/tests/res/csv_test.csv"
        csv_util = csv_utils.CSVFile(file_path, True)
        csv_util.read_file()
        header = csv_util.get_header()
        data_rows = csv_util.get_data_rows()
        self.assertEqual(header, ['a', 'b', 'c'])
        self.assertEqual(data_rows, [['1', '2', '3'], ['4', '5', '6']])

    def test_reading_csv_file_implicitly(self):
        file_path = os.getcwd() + "/tests/res/csv_test.csv"
        csv_util = csv_utils.CSVFile(file_path, True)
        self.assertEqual(csv_util.get_header(), ['a', 'b', 'c'])
        self.assertEqual(csv_util.get_data_rows(), [['1', '2', '3'], ['4', '5', '6']])
        
    def test_reading_csv_with_pipe_delimiter(self):
        file_path = os.getcwd() + "/tests/res/csv_with_pipe_delimiter.csv"
        csv_util = csv_utils.CSVFile(file_path, False, "|")
        self.assertEqual(csv_util.get_header(), [])
        self.assertEqual(csv_util.get_data_rows(), [['1', '2', '3'], ['4', '5', 'a'], ['z', 'y', 'a']])


if __name__ == "__main__":
    unittest.main()