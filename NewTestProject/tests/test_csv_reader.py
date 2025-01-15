#write tests for your CSVReader in the tests/ folder:

import unittest
from src.utils.csv_reader import CSVReader

class TestCSVReader(unittest.TestCase):
    def test_read_data(self):
        reader = CSVReader("test_file.csv")
        data = reader.read_data()
        self.assertIsInstance(data, list)

    def test_filter_data(self):
        reader = CSVReader("test_file.csv")
        filtered_data = reader.filter_data("Category", "Electronics")
        self.assertTrue(all(row["Category"] == "Electronics" for row in filtered_data))

if __name__ == "__main__":
    unittest.main()
