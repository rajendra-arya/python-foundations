def pure(water):
    return water*10
        
total = 100

#impure function which not recommended
def impure(water):
    global total
    total+=water
    return total
    

# print(pure(5))
# print(impure(5))


#recursive function

# def pour_chai(cups):
#     print(cups)
#     if cups==0:
#         print('All cups served!')
#         return #exits the function avoid RecursionError: maximum recursion depth exceeded -1 -2...
#     pour_chai(cups-1)

# pour_chai(3)


def pour_chai(cups):
    print(cups)
    if cups==0:
        return 'All cups served!'
    return pour_chai(cups-1)

print(pour_chai(3))

#lambdas or anonymous function

chai_types = ['kadak','lemon','masala','milk','masala']
# chai_menu = filter(lambda type: type=='masala',chai_types) #returns a filter iterator object (a reference), not a list of values.
chai_menu = list(filter(lambda type: type!='masala',chai_types)) #  # filter-> true refrence-> convert to list
print(chai_menu)


