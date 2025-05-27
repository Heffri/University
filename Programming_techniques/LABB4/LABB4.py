# LABB 4
# Sebastijan Babic
# 2024 - 02 - 12

import matplotlib.pyplot as plt
import math

## UPPGIFT 1 / UPPGIFT 2 / UPPGIFT 3 ##
# UPPGIFT 1 : delade upp batch_means till read_csv_file, calculate_averages, print_results, main


def read_csv_file(filename):
    '''
    Reads through a .csv file and saves data in a list which can be utilized later. 
    Handles ValueError and FileNotFoundError

    Parameters: 
    file (format of .csv) : csv file with 3 values per batch

    Returns:
    Parsed data saved as list
    '''
    data = {}
    try:
        with open(filename, 'r') as file_handle:
            for line in file_handle:
                try:
                    # Using ChatGPT 4.0 Grimoire GPT : 
                    # Using strip to get rid of potential errors due to empty space
                    # Spliting whenever string , comes up due to it being csv
                    # Saves 4 variables based off of format of csv
                    batch, x, y, val = line.strip().split(',')
                    if batch not in data:
                        data[batch] = []
                    data[batch].append((float(x), float(y), float(val))) # Append the data as a tuple to the list
                except ValueError: # UPPGIFT 2
                    # Handles reading fault
                    print(f"Varning: Kunde inte tolka raden '{line.strip()}'. Raden ignoreras.")
        return data
    except FileNotFoundError: # UPPGIFT 2
        print(f"Fel: Kunde inte öppna filen '{filename}'. Kontrollera att filnamnet är korrekt.")
        return None
    


def calculate_averages(data):
    '''
    Calculates the average for each batch based on the condition (x^2 + y^2 <= 1).
    
    Parameters:
    data (dict): The parsed data from the CSV file.
    
    Returns:
    dict: Averages calculated for each batch.
    '''
    averages = {}
    for batch, samples in data.items():
        n, x_sum = 0, 0
        for x, y, val in samples:
            if x**2 + y**2 <= 1:
                x_sum += val
                n += 1
        # Take average of appropriate batch saved in read_csv_file
        if n > 0:
            averages[batch] = x_sum / n
        else: # If average of certain batch outside given region return None
            averages[batch] = None
    return averages


def print_results(averages):
    '''
    Prints the batch and its corresponding average in a formatted output,
    sorted by batch number in ascending order.
    
    Parameters:
    averages (dict): Averages calculated for each batch.
    
    Returns:
    String average of calculated averages
    '''
    print("Batch\tAverage")
    
    # Converts the keys (batches in strings) to integers and sorts, then converts back to strings
    for batch in sorted(averages, key=int): # UPPGIFT 3
        print(f"{batch}\t{averages[batch]}")
        




## UPPGIFT 4 ##
def plot_data(data, filename):
    '''
    Plots data using previously calculated data from calculate_averages and save the plot to new PDF
    
    Parameters:
    data (dict): Parsed data form csv file
    
    Returns: 
    A new PDF plot of the input csv file
    '''
    # Calculate 150 coordinates to draw the circle
    angles = [n / 150 * 2 * math.pi for n in range(151)]
    x_coords = [math.cos(a) for a in angles]
    y_coords = [math.sin(a) for a in angles]

    # Draw the circle
    plt.plot(x_coords, y_coords, 'k')  # 'k' for black circle

    # Plot the data points
    colors = ['r', 'b', 'g', 'c', 'm', 'y', 'k']  # Define a list of colors for different batches
    for idx, (batch, points) in enumerate(data.items()):
        color = colors[idx % len(colors)]  # Cycle through colors /// ChatGPT
        for x, y, val in points:
            plt.plot(x, y, marker='o', color=color)
            plt.text(x, y, str(val), fontsize=6, color=color)

    plt.axis('equal')  # Set axes to be equal, makes the circle appear circular
    plt.title('Plot of Data Points with Unit Circle')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Save the plot to a PDF file
    plt.savefig(filename + ".pdf")
    plt.close()  # Close the plot to free up memory








def main():
    '''
    Main function orchestrating the reading, processing, and printing of CSV data.
    '''
    filename = input('Which csv file should be analyzed? ')
    data = read_csv_file(filename)

    # Check if data is none or not 
    if data is not None: 
        averages = calculate_averages(data)
        print_results(averages)
        plot_data(data, filename.split(',')[0])
        print(f"A plot of the data can be found in {filename.split('.')[0]}.pdf.")
    else: # UPPGIFT 2
        # If no data was analysed due to some error
        print("No data was analyzed due to error in handling of the csv file")
        
        # Necessary due to the potential of AttributeError due to read_csv_file and it returning None due to FileNotFoundError

if __name__ == '__main__':
    main()

    



