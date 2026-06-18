#generator () : get values as a stream

daily_sales = [5, 10, 12, 6, 4, 24, 44, 8, 17]

# find daily sales > 5
total_cups = [sale for sale in daily_sales if sale>5] #returns complete list
total_cups_gen = sum(sale for sale in daily_sales) # returns value one by one
print(daily_sales)
print(total_cups) #[10, 12, 6, 24, 44, 8, 17]
print(total_cups_gen)  #130