import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
import csv
import os
import pandas as pd

FILE_NAME = "user_input.csv"

def ensure_csv_exists():
    """Ensures the CSV file exists with the correct headers."""
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Option", "Sentence"])

def select_csv_location():
    """Prompts the user to select a location for the CSV file."""
    global FILE_NAME
    file_path = filedialog.asksaveasfilename(
        title="Select CSV Location",
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")]
    )
    if file_path:
        FILE_NAME = file_path
        ensure_csv_exists()

def create_record(date, option, sentence):
    """Creates a new record in the CSV file."""
    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, option, sentence])

def read_records():
    """Reads all records from the CSV file and returns them as a DataFrame."""
    try:
        return pd.read_csv(FILE_NAME)
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")
        return pd.DataFrame()

def update_record(index, date, option, sentence):
    """Updates a record in the CSV file by index."""
    df = read_records()
    if index < len(df):
        df.loc[index, ["Date", "Option", "Sentence"]] = [date, option, sentence]
        df.to_csv(FILE_NAME, index=False)
    else:
        messagebox.showerror("Error", "Index out of range.")

def delete_record(index):
    """Deletes a record from the CSV file by index."""
    df = read_records()
    if index < len(df):
        df = df.drop(index=index).reset_index(drop=True)
        df.to_csv(FILE_NAME, index=False)
    else:
        messagebox.showerror("Error", "Index out of range.")

def open_popup_create():
    """Opens a popup window to create a new record."""
    popup = tk.Toplevel()
    popup.title("Create Record")
    popup.geometry("400x300")

    tk.Label(popup, text="Select a Date:").pack(pady=10)
    date_picker = DateEntry(popup, width=20, background="darkblue", foreground="white", borderwidth=2)
    date_picker.pack(pady=5)

    tk.Label(popup, text="Select an Option:").pack(pady=10)
    options = ['p1', 'p2', 'p3']
    selected_option = tk.StringVar(value=options[0])
    dropdown = ttk.Combobox(popup, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=5)

    tk.Label(popup, text="Enter a Sentence:").pack(pady=10)
    text_input = tk.Entry(popup, width=50)
    text_input.pack(pady=5)

    def submit_action():
        create_record(date_picker.get(), selected_option.get(), text_input.get())
        messagebox.showinfo("Success", "Record created successfully.")
        popup.destroy()
        refresh_table()

    tk.Button(popup, text="Submit", command=submit_action).pack(pady=20)

def open_popup_update(index):
    """Opens a popup window to update an existing record."""
    df = read_records()
    if index >= len(df):
        messagebox.showerror("Error", "Invalid record selected.")
        return

    popup = tk.Toplevel()
    popup.title("Update Record")
    popup.geometry("400x300")

    tk.Label(popup, text="Select a Date:").pack(pady=10)
    date_picker = DateEntry(popup, width=20, background="darkblue", foreground="white", borderwidth=2)
    date_picker.set_date(df.loc[index, "Date"])
    date_picker.pack(pady=5)

    tk.Label(popup, text="Select an Option:").pack(pady=10)
    options = ['p1', 'p2', 'p3']
    selected_option = tk.StringVar(value=df.loc[index, "Option"])
    dropdown = ttk.Combobox(popup, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=5)

    tk.Label(popup, text="Enter a Sentence:").pack(pady=10)
    text_input = tk.Entry(popup, width=50)
    text_input.insert(0, df.loc[index, "Sentence"])
    text_input.pack(pady=5)

    def submit_action():
        update_record(index, date_picker.get(), selected_option.get(), text_input.get())
        messagebox.showinfo("Success", "Record updated successfully.")
        popup.destroy()
        refresh_table()

    tk.Button(popup, text="Submit", command=submit_action).pack(pady=20)

def refresh_table():
    """Refreshes the data displayed in the table."""
    table.delete(*table.get_children())  # Clear the table
    df = read_records()
    for i, row in df.iterrows():
        table.insert("", "end", values=(row["Date"], row["Option"], row["Sentence"]))

# Create main application window
root = tk.Tk()
root.title("CSV CRUD Operations")
root.geometry("600x400")

# Prompt user to select CSV location
select_csv_location()

# Buttons
tk.Button(root, text="Create Record", command=open_popup_create).pack(pady=10)

tk.Button(root, text="Update Record", command=lambda: on_update()).pack(pady=10)

tk.Button(root, text="Delete Record", command=lambda: on_delete()).pack(pady=10)

# Table
columns = ("Date", "Option", "Sentence")
table = ttk.Treeview(root, columns=columns, show="headings")
table.heading("Date", text="Date")
table.heading("Option", text="Option")
table.heading("Sentence", text="Sentence")
table.pack(fill="both", expand=True)

def on_update():
    """Handles updating the selected record."""
    selected_item = table.selection()
    if selected_item:
        index = table.index(selected_item[0])
        open_popup_update(index)
    else:
        messagebox.showerror("Error", "No record selected.")

def on_delete():
    """Handles deleting the selected record."""
    selected_item = table.selection()
    if selected_item:
        index = table.index(selected_item[0])
        delete_record(index)
        refresh_table()
    else:
        messagebox.showerror("Error", "No record selected.")

# Initial table refresh
refresh_table()

# Run the application
root.mainloop()
