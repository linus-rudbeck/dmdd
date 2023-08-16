import csv
import random

NUMBER_OF_ROWS = 20

with open('product_data.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['product_id', 'product_name', 'product_price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(NUMBER_OF_ROWS):
        product_name = f"Product {i + 1}"
        # product_price = (i+1) * 100
        product_price = random.randint(10, 1000)


        writer.writerow({
            'product_id': i + 1,
            'product_name': product_name,
            'product_price': product_price
        })