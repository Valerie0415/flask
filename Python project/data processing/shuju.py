import csv
with open('E:\Python project\data processing\product_2.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    column = [row['device']['time'] for row in reader]
print column
