import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("CSV Data Loaded Successfully!")
        print(data.head())  # Display first few rows
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 2: Plot the data
def visualize_data(data, x_column, y_column):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data[x_column], data[y_column], marker='o', label=f"{y_column} vs {x_column}")
        plt.title(f"{y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.legend()
        plt.grid()
        plt.show()
    except KeyError:
        print("Error: One of the specified columns does not exist.")
    except Exception as e:
        print(f"An error occurred during visualization: {e}")

# Step 3: Main function to execute the program
def main():
    file_path = input("Enter the path to the CSV file: ")
    data = read_csv(file_path)

    if data is not None:
        print("\nColumns available for plotting:")
        print(data.columns)
        
        x_column = input("Enter the column name for the X-axis: ")
        y_column = input("Enter the column name for the Y-axis: ")
        
        visualize_data(data, x_column, y_column)

if __name__ == "__main__":
    main()
