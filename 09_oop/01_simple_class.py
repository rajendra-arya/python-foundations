# 1. Defining Blueprints (Classes)
class ChaiClass:
    pass

class CoffeeClass:
    pass

#prints type
print(type(ChaiClass)) 
#<class 'type'>

#print the class blueprint 
print(ChaiClass) 
#<class '__main__.ChaiClass'>

#Creating obj/instance
ginger_tea = ChaiClass()

#prints the specific instance (the individual cup of tea)
print(ginger_tea) 
#__main__.ChaiClass object at 0x000001BCD97B6F90>

#tells i am obj of ChaiClass or what blueprint created you
print(type(ginger_tea)) 
#<class '__main__.ChaiClass'>

#check class
print('obj of Chai Class : ',type(ginger_tea) is ChaiClass)
print('obj of Chai Class : ',type(ginger_tea) is CoffeeClass)

# The standard Python way to check an object's type
print(isinstance(ginger_tea, ChaiClass))    # Output: True
print(isinstance(ginger_tea, CoffeeClass))  # Output: False


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# # 1. Defining Minimal Blueprints (Classes)
# class ChaiClass:
#     pass

# class CoffeeClass:
#     pass


# # 2. Inspecting Classes (Classes are objects of the master factory 'type')
# # Output: <class 'type'> -> Confirms ChaiClass itself is a class object
# print(type(ChaiClass)) 

# # Output: <class '__main__.ChaiClass'> -> Prints the class blueprint definition namespace
# print(ChaiClass) 


# # 3. Instantiation (Creating an instance/object from a class)
# # ginger_tea is an individual instance allocated in memory
# ginger_tea = ChaiClass()


# # 4. Inspecting Instances
# # Output: <__main__.ChaiClass object at 0x000001BCD97B6F90> -> Prints individual memory address
# print(ginger_tea) 

# # Output: <class '__main__.ChaiClass'> -> Queries the instance for its creator blueprint
# print(type(ginger_tea)) 


# # 5. Type Identity Verification (Using the 'is' operator for exact memory matching)
# # Returns True: The instance's type matches the ChaiClass blueprint identity exactly
# print('obj of Chai Class : ', type(ginger_tea) is ChaiClass)

# # Returns False: CoffeeClass is a completely separate blueprint identity in memory
# print('obj of Chai Class : ', type(ginger_tea) is CoffeeClass)


# # 6. Recommended Reference Standard: Using isinstance()
# # Note: Use isinstance() instead of 'type() is' because it supports inheritance checks
# print('Best Practice Check:', isinstance(ginger_tea, ChaiClass))  # Returns True
