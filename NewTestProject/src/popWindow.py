import tkinter as tk
from tkinter import filedialog

def select_csv_file():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Specify the initial directory
    initial_directory = "C:/Users"  # Change this to your desired directory
    
    # Show a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(
        title="Select a CSV File",
        initialdir=initial_directory,
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    
    # Print the selected file path (or process it as needed)
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")
    
    return file_path

# Call the function
selected_file = select_csv_file()
