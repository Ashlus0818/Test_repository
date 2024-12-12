import csv
import os

class CSVReader:
    def __init__(self, file_name):
        """
        Initialize the CSVReader with the relative file name.
        
        Args:
            file_name (str): File name relative to the project root.
        """
        # Dynamically get the project root directory
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.file_path = os.path.join(project_root, "data", file_name)

    def read_data(self):
        """
        Reads the CSV file and returns the data as a list of dictionaries.
        set encoding='utf-8-sig to solve the Byte Order Mark (BOM) issue
        because the dummy data is set to utf-8 and the first column first row 
        will show \ufeff
        """
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8-sig ') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_column_data(self, column_name):
        """
        Extracts all the data from a specified column.
        
        Args:
            column_name (str): The name of the column to extract.
        
        Returns:
            list: A list of values from the specified column.
        """
        data = self.read_data()
        try:
            # Extract values from the specified column
            return [row[column_name].strip() for row in data if column_name in row]
        except KeyError:
            print(f"Error: Column '{column_name}' not found.")
            return []

