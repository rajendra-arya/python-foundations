# creating custom exception class
class OutOfIngreidents(Exception):
    pass

def make_chai(sugar, milk):
    if sugar==0 or milk==0:
        raise OutOfIngreidents(f'Missing Milk or Sugar')
    print('Preparing Chai...')

make_chai(1,1) # Preparing Chai...

make_chai(1,0)

# Traceback (most recent call last):
#   File "05_custom_exception_2.py", line 9, in <module>
#     chai(1,0)
#     ~~~~^^^^^
#   File "05_custom_exception_2.py", line 6, in chai
#     raise OutOfIngreidents(f'Missing Milk or Sugar')
# OutOfIngreidents: Missing Milk or Sugar