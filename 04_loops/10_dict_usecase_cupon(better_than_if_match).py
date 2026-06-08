# process user and give discounts based on dicounts.
users = [
    {"id":1,"total":480,"cupon":"P20"},
    {"id":2,"total":150,"cupon":"F20"},
    {"id":3,"total":80,"cupon":"P50"},
    ]

#we can use if else or match too but dict is more simple and scalable.

#disount contains discount(percent) and flat/fixed(exact money) value
discounts = {
    "P20" : (0.2,0),
    "F20" : (0,20),
    "P50" : (0.5,0)
}

for user in users:
    percent , fixed = discounts.get(user['cupon'],(0,0))
    discount = user['total'] * percent + fixed
    print(f"id {user['id']} paid {user['total']} and got next vist discount of {discount} rupees.") 

