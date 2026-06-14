# Built in 

def chai_flavor(flavour='masala'):
    """Return the flavour of chai""" # it needs to be the first line of your function
    return flavour

#helpful for debuging
print(chai_flavor.__name__) #name of function
print(chai_flavor.__doc__) #returns the function doc(first line)

help(len)  #to know about any builtin function u can use help
# help(chai_flavor)


#sample example: recommeded way: 
def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message)
    """
    total = chai*10 + samosa*15
    return total,'Thank you for visiting!'

print(generate_bill.__doc__)