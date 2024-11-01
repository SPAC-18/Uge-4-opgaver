import csv
import numpy as np

def my_filter(entry):
    if float(entry[2]) == 1.0:
        return True
    else:
        return False

def csv_generator(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        filtered=filter(my_filter, reader)
        for row in filtered:
            entries = list(map(float, row))
            yield entries[0], entries[1]

def collect_data(generator):
    column1, column2 = [], []

    for entry1, entry2 in generator:
        column1.append(entry1)
        column2.append(entry2)

    return column1, column2

def calculate_statistics(data):
    return np.mean(data), np.std(data)

def calculate_correlation(data1, data2):
    return np.corrcoef(data1, data2)[0, 1]
    
def main():
    # Generer filen med stor_fil_2.py
    file_name = "big_stupid_file.csv"
    
    data_gen = csv_generator(file_name)
    column1, column2 = collect_data(data_gen)
    
    mean1, std1 = calculate_statistics(column1)
    mean2, std2 = calculate_statistics(column2)
    correlation = calculate_correlation(column1, column2)

    print(f"Column 1 - Mean: {mean1}, Standard Deviation: {std1}")
    print(f"Column 2 - Mean: {mean2}, Standard Deviation: {std2}")
    print(f"Correlation between Column 1 and Column 2: {correlation}")

main()