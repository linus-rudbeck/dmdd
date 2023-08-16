import random
import csv

NUMBER_OF_ROWS = 500

with open('purchase_data.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['purchase_id', 'customer_id', 'product_id', 'purchase_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(NUMBER_OF_ROWS):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        year = random.randint(2010, 2020)

        month = f"0{month}" if month < 10 else month
        day = f"0{day}" if day < 10 else day
        
        purchase_date = f"{year}-{month}-{day}"

        writer.writerow({
            'purchase_id': i + 1,
            'customer_id': random.randint(1, 100),
            'product_id': random.randint(1, 20),
            'purchase_date': purchase_date
        })