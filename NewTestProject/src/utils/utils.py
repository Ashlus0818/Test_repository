import os
import matplotlib.pyplot as plt

def file_exists(file_path):
    """Check if a file exists."""
    return os.path.exists(file_path)

def calculate_average_temperature(data, column_name="temperature"):
    """
    Calculate the average of a numeric column in the dataset.
    
    Args:
        data (list[dict]): The list of dictionaries representing the data.
        column_name (str): The column to calculate the average for.
        
    Returns:
        float: The average value of the column.
    """
    try:
        # Extract numeric values from the specified column
        values = [float(row[column_name]) for row in data if row[column_name].strip()]
        
        # Ensure there are valid values
        if not values:
            raise ValueError(f"No valid values found in column '{column_name}'")
        return sum(values) / len(values)
    except KeyError:
        print(f"Error: Column '{column_name}' not found in data.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

def plot_columns(data, x_column, y_column, title="Plot", xlabel=None, ylabel=None):
    """
    Creates a plot using two selected columns from the data.
    
    Args:
        data (list[dict]): List of dictionaries representing the CSV data.
        x_column (str): The column name for the x-axis.
        y_column (str): The column name for the y-axis.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis (defaults to x_column).
        ylabel (str): Label for the y-axis (defaults to y_column).
    """
    try:
        # Extract values for the selected columns
        x_values = [row[x_column] for row in data if x_column in row]
        y_values = [row[y_column] for row in data if y_column in row]

        # Convert y_values to numeric (if possible)
        y_values = [float(y) for y in y_values]

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, marker='o')
        plt.title(title)
        plt.xlabel(xlabel if xlabel else x_column)
        plt.ylabel(ylabel if ylabel else y_column)
        plt.grid(True)
        plt.show()
    except KeyError as e:
        print(f"Error: Column {e} not found in data.")
    except ValueError as e:
        print(f"Error: Invalid data for plotting - {e}.")
