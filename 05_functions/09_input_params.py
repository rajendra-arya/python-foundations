#simplee argument example
# chai = "Ginger"

# def prep_chai(order):
#     print("Preparing", order)

# prep_chai(chai) #Ginger
# print(chai) #Ginger

# -----------------------

chai = [1,2,3] #list i.e mutable

def edit_chai(cup):
    cup[1] = 42 #original will also change by this

edit_chai(chai) #[1, 42, 3]
print(chai) #[1, 42, 3]

# -------
# args and keyword args

def make_chai(tea,milk, sugar):
    print(f'Tea: {tea}, Milk: {milk}, Sugar: {sugar}')

make_chai("Darjeeling","Yes", "Low") #positional arg (we know the position of it)
make_chai(tea="Great", sugar="Medium", milk="No") #keyward arg : when u unsure about the position of the arg,we don't care about the params order
#output
#Tea: Darjeeling, Milk: Yes, Sugar: Low
#Tea: Great, Milk: No, Sugar: Medium


#--------
# agrs and kargs(key value args) mixture
# *arg : all args will be in tuple
# **karg : all args will be in dictionary(key value)

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)
    
special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="yes") #some params have name some doesn't
# Output : 
# Ingredients ('Cinnamon', 'Cardmom')
# Extras {'sweetner': 'Honey', 'foam': 'yes'}



## prodution tips  #default value
# - default value of empty array [] has catch aka default trap
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

#scenario running twice
# chai_order() #['Masala']
# chai_order() #['Masala', 'Masala']

#fix
def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order() #[]
chai_order() #[]