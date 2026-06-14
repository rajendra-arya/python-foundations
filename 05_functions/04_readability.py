def calculate_bills(cups, price_per_cup):
    return cups * price_per_cup


mybill = calculate_bills(1,15)
print(mybill,'Rupees.')

print(f'Order of table 3: {calculate_bills(2,50)} Rupees.')
