menu = [
    'Masala Chai',
    'Iced Lemon Tea',
    'Green Tea',
    'Iced Peach Tea',
    'Ginger Tea'
]

# [expression item in iterable if condition]
iced_tea = [current_item for current_item in menu if 'iced' in current_item.lower()]
print(iced_tea)

masala_tea = [current_item if 'masala' in current_item.lower() else 'not masala' for current_item in menu]
print(masala_tea)



