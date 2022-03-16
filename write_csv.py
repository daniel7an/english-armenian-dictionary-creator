import csv

def convert_to_csv(rows):
    with open('words.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerows(rows)