import unittest
from src.utils.utils import calculate_average_temperature

class TestUtils(unittest.TestCase):
    def test_calculate_average_temperature(self):
        data = [
            {"temperature": "20"},
            {"temperature": "22"},
            {"temperature": "21"},
            {"temperature": "19"},
        ]
        self.assertAlmostEqual(calculate_average_temperature(data, "temperature"), 20.5)

    def test_empty_column(self):
        data = [{"temperature": ""}, {"temperature": ""}]
        self.assertIsNone(calculate_average_temperature(data, "temperature"))

    def test_missing_column(self):
        data = [{"humidity": "50"}, {"humidity": "60"}]
        self.assertIsNone(calculate_average_temperature(data, "temperature"))

if __name__ == "__main__":
    unittest.main()
