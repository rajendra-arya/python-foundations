# def process_order(item, quantity):
#     try:
#         price = {"masala":20}[item] #dict[item]: it will check if item exists as the key
#         cost = price * quantity 
#         print(f"Total cost is {cost}")
#     except KeyError:
#         print(f"Sorry that {item} Chai is not on menu")
#     except TypeError: #if mismatch of type
#         print(f"Quantity {quantity} must be in number")
    
# # process_order("ginger",2)
# process_order("masala",'a')  #operator overloading string * int
# #Total cost is aaaaaaaaaaaaaaaaaaaa



## Fixing operator overloading using either way:
# 1. Explicit Type Conversion: convert the quantity int(quantity)
# 2. Explicit Type Checking : check the quantity is int using isinstance() or type() methods and raise type error. 

def process_order(item, quantity):
    try:
        if not isinstance(quantity,int):
            raise TypeError
        
        price = {"masala":20}[item] #dict[item]: it will check if item exists as the key
        cost = price * quantity 
        print(f"Total cost is {cost}. Thank you!")
    except KeyError:
        print(f"Sorry {item} Chai is not on menu.") 
    except TypeError: #if mismatch of type
        print(f"Quantity {quantity} must be in number.")
    
process_order("ginger",2)  #Sorry ginger Chai is not on menu.
process_order("masala",'a') #Quantity a must be in number.
process_order("masala",4) #Total cost is 80. Thank you!
