order_amt = int(input('Enter the order amount:'))
# delivery_fee = 0

# if order_amt > 300:
#     delivery_fee=0
# else:
#     delivery_fee=50

# simple way using ternary opeator
delivery_fee = 0 if order_amt>300 else 50



print(f'delivery fee is: {delivery_fee}')

