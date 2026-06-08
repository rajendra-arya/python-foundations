staff = [('Amit',16),('Jay',12),('Rohit',14),('Rajendra',17)]

for name,age in staff:
    if age<=18:
        print(f'{name} is eligible')
        # break
    
else: #fallback if no condition satifies
    print(f'No one is eligible')

# if one condition satifies then it doesnt come to else loop?