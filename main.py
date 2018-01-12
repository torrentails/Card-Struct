#!/usr/bin/python3

import csv

if __name__ == "__main__":
    exit()

class _G():
    def __init__(self):
        self.current_card = 0
        self.headers = None
        self.data = []

g = _G()

def _readcsv(filepath):
    with open(filepath, newline='') as csvfile:
        #dialect = csv.Sniffer().sniff(csvfile.read(1024))
        #csvfile.seek(0)
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        if not has_header:
            raise(ValueError("Data file must have a header line."))
        reader = csv.DictReader(csvfile)
        lst = []
        for row in reader:
            lst.append(row)
        return reader.fieldnames, lst

def datafile(filepath):
    log.debug(f"{}")
    headers, data = _readcsv(filepath)
    if g.headers:
        if g.headers != set(headers):
            log.error(f"Data file not contain the same fields as \
                previously loaded data. Check the data file or use \
                secondary_datafile(filepath) instead.\n{filepath}")

def secondary_datafile(filepath):
    pass

class card:
    def __init_subclass__(cls, i=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if i:
            for key, meth in i.__dict__.items():
                if not key.startswith('_'):
                    setattr(cls, key, meth)
