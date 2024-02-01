import csv
import json
csv_file_path = 'C:/Users/Akshat Singh/Desktop/detxfinal.csv'
data = []
encoding='ISO-8859-1'

with open(csv_file_path, mode='r', encoding=encoding) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)
print(data)