import csv
with open('filename.csv') as csv_file:
    new = csv.DictReader(csv_file)
    for row in new:
        print(row['expected row'])
