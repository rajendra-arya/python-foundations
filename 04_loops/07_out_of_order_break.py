flavours = ['Ginger','Out of Stock','Lemon','Discontinued']

for flavour in flavours:
    if(flavour == 'Out of Stock'):
        continue
    if(flavour == 'Discountinued'):
        print(f'{flavour} is found.')
        break
    print(f'{flavour} is found.')

print('Out side of the Loop')