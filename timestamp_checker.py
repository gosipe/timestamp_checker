import tkinter as tk
import numpy as np
from tkinter import filedialog
import matplotlib.pyplot as plt

# Function to browse and load a text file --specifically designed for MOSEQ recordings with timestamp text files
def load_file():
    # Open file dialog to select a text file
    file_path = filedialog.askopenfilename(
        #title="Select a Text File",
        #filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            # Read lines and extract the first value before a space and 0
            timestamps = [line.split()[0] for line in file.readlines() if line.split()[0] != '0']
            print("Timestamps loaded:", timestamps)
        return timestamps
    else:
        print("No file selected.")
        return None

# Create a simple GUI to trigger file browsing
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    timestamps = load_file()
    print(np.shape(timestamps))
    if timestamps:
        # Convert timestamps to numeric values if possible
        try:
            numeric_timestamps = [float(ts) for ts in timestamps]
            plt.figure(figsize=(10, 6))
            plt.plot(numeric_timestamps, linestyle='-', color='k')
            plt.title("Timestamps Plot")
            plt.xlabel("Index")
            plt.ylabel("Timestamp Value")
            plt.grid(True)
            plt.show(block=False)
        except ValueError:
            print("Timestamps contain non-numeric values and cannot be plotted.")
    # Calculate the differences between consecutive timestamps
    differences = np.diff(numeric_timestamps)
    
    # Plot the differences
    plt.figure(figsize=(10, 6))
    plt.plot(differences, linestyle='-', color='k')
    plt.title("Differences Between Consecutive Timestamps")
    plt.xlabel("Index")
    plt.ylabel("Difference Value")
    plt.grid(True)
    plt.show()
