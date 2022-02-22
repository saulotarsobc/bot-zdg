import csv


def setCsv(fileName, data ):
    with open(f'{fileName}.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
