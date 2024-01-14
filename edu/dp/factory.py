import json
import pandas as pd

class FileParser:
    def parse(self, file_path):
        pass

class CSVFileParser(FileParser):
    def parse(self, file_path):
        return pd.read_csv(file_path)

class JSONFileParser(FileParser):
    def parse(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)

class FileParserFactory:
    def create_parser(self, file_path):
        if file_path.endswith(".csv"):
            return CSVFileParser()
        elif file_path.endswith(".json"):
            return JSONFileParser()
        else:
            raise ValueError("Unsupported file format")

# Usage
file_path = "data.csv"
parser_factory = FileParserFactory()
parser = parser_factory.create_parser(file_path)
data = parser.parse(file_path)