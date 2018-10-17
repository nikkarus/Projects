import csv

path =  r'P:\Nick Jordan\Postgres setup\Data1 Short.csv'

with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open(path + 'UTF8.csv', 'w', newline='') as outfile:
    inputs = csv.reader(infile)
    output = csv.writer(outfile)
    for index, row in enumerate(inputs):
         # Create file with no header
         #if index == 0:
             #continue
        output.writerow(row)