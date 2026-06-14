# returns nothing(None) when given nothing
def idle_chai():
    pass

print(idle_chai()) #Output : None

#return one value
def sold_cups():
    return 120

print(sold_cups()) # Output : 120
total = sold_cups()
print(total) #Output : 120


# return early from a function

def chai_status(cups_left):
    if cups_left ==0:
        return 'Sorry chai over!'
    return "Chai is ready"
    print('after return message') #it won't be executed i.e return early

print(chai_status(0)) #output : Sorry chai over!
print(chai_status(10)) #output : Chai is ready



# return multiple value

def chai_report():
    return 100,20 #sold , remaning

chai_report() # nothing will be printed

sold , remaining = chai_report()
print(f'Sold: {sold}, Remaing: {remaining}')


# what if one more value function returns
#unpacking error can cause when return values not equal to unpacking values
    #1.fix1 : use _ to ignore all not required values
            # `sold , remaining , _ = chai_report()`
            # - it jst means i know but i never gonna use them, used by exp dev lot
    #2. add extra unpacking variable
            # `sold , remaining , _ = chai_report()`



def chai_report():
    return 100,20,39 #sold , remaning, unpaid

chai_report() # nothing will be printed

sold , remaining , _ = chai_report()
print(f'Sold: {sold}, Remaing: {remaining}')



def chai_report():
    return 100,20,39 #sold , remaning, upaid

chai_report() # nothing will be printed

sold , remaining , not_paid = chai_report()
print(f'Sold: {sold}, Remaing: {remaining}')

# Sold: 100, Remaing: 20
# Sold: 100, Remaing: 20
# Sold: 100, Remaing: 20