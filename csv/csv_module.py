import csv

with open('employees.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        # each row is a list
        print(row)

data = [
    ['Name', 'Age', 'Country'],
    ['Alice', 30, 'USA'],
    ['Bob', 25, 'Canada'],
    ['Charlie', 35, 'UK']
]

# Open the CSV file for writing
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

# Open the CSV file for reading
with open('example.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # each row is a dictionary        
        print(row['Name'], row['Age'], row['Country'])