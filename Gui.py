import tkinter as tk
from tkinter import messagebox
import subprocess
import Main


def run_excel_creation():
    try:
        nbr_pilots = int(entry_pilots.get())
        special_pilots = int(entry_special.get())
        nbr_groups = int(entry_groups.get())
        nbr_races = int(entry_races.get())

        Main.main(nbr_pilots,
            special_pilots,
            nbr_groups,
            nbr_races)

        messagebox.showinfo("Success", "Excel sheet created successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# Window setup
root = tk.Tk()
root.title("Excel Sheet Creator")
root.geometry("400x200")  # Force a visible starting size
root.resizable(False, False)

# Labels and entries with padding
tk.Label(root, text="Number of Pilots:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_pilots = tk.Entry(root)
entry_pilots.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Special Pilots:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_special = tk.Entry(root)
entry_special.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Number of Groups:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_groups = tk.Entry(root)
entry_groups.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Number of Races:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_races = tk.Entry(root)
entry_races.grid(row=3, column=1, padx=5, pady=5)

# Button
tk.Button(root, text="Generate Excel", command=run_excel_creation).grid(
    row=4, columnspan=2, pady=10
)

root.mainloop()
