import sys
import os

from utils.csv_reader import CSVReader
from utils.utils import calculate_average_temperature
from utils.utils import plot_columns

#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

def main():
    csv_reader = CSVReader("dummy_data.csv")
    
    # Read all data
    data = csv_reader.read_data()
    print("\nAll Data:\n", data)

    # Get all values in the specific column
    temperature = csv_reader.get_column_data("Temperature")
    print("\nTemperature:\n"+ "\n".join(temperature))

    # Calculate the average temperature
    average_temperature = calculate_average_temperature(data, column_name="Temperature")
    if average_temperature is not None:
        print(f"\nThe average temperature is {average_temperature:.2f}\n")

    # Plot the data using two selected columns
    plot_columns(data, x_column="Date", y_column="FlowRate", title="FlowRate Over Date")

if __name__ == "__main__":
    main()
