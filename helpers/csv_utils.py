
class CSVFile:


    def __init__(self, file_name: str, has_header: bool, delimiter: str = ","):
        self.file_name = file_name
        self.delimiter = delimiter
        self.has_header = has_header
        self.header = []
        self.data_rows = []
        self.is_file_read = False

    def read_file(self):
        with open(self.file_name) as f:
            if self.has_header:
                self.header = [i.strip() for i in f.readline().split(self.delimiter)]
            for line in f:
                self.data_rows.append([i.strip() for i in line.split(self.delimiter)])
        self.is_file_read = True
    
    def get_header(self):
        if self.is_file_read:
            return self.header
        else:
            self.read_file()
            return self.get_header()

    def get_data_rows(self):
        if self.is_file_read:
            return self.data_rows
        else:
            self.read_file()
            return self.get_data_rows()

