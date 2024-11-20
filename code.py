from flask import Flask, request, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'csvFile' not in request.files:
        return "No file part", 400
    
    file = request.files['csvFile']
    
    if file.filename == '':
        return "No selected file", 400
    
    # Save the file temporarily
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Read the CSV file using pandas
    try:
        data = pd.read_csv(file_path)
        print(data.head())  # Optional: Print the first few rows for debugging

        # Generate a plot (Example: line plot for the first two columns)
        plt.figure(figsize=(10, 6))
        plt.plot(data.iloc[:, 0], data.iloc[:, 1], marker='o', label="Data Plot")
        plt.title("CSV Data Visualization")
        plt.xlabel(data.columns[0])
        plt.ylabel(data.columns[1])
        plt.legend()
        
        # Save the plot as an image
        plot_path = os.path.join('static', 'plot.png')
        plt.savefig(plot_path)

        return render_template('index.html', plot_url=plot_path)  # Send the plot URL back to the frontend
    
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
