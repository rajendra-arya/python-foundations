class Chai:
    temp = "hot"
    stength = "Strong"

cutting = Chai()
print(cutting.temp)

cutting.temp = 'Mild'
print('After changing temp: ', cutting.temp)
print('Original Class temp: ', Chai.temp)

# deleting obj propety using deletion operator(del)
del cutting.temp
print('After del temp from Cutting : ', cutting.temp)  #will fall back to orginal class attribute
#hot

#adding new prop to obj
cutting.cup = 'small'
print('cup size is', cutting.cup)

del cutting.cup

# this will throw errror, as its not in orginal class too so no fallback
# print('cup size is', cutting.cup) 
# > AttributeError: 'Chai' object has no attribute 'cup'