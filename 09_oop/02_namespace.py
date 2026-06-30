class Chai:
    origin = "India"

print(Chai.origin) #India

#adding new property in the class from outside
Chai.is_hot = True
print(Chai.is_hot) #True


# creating obj from class chai
masala = Chai() #<__main__.Chai object at 0x0000021F4EB96F90>
print(masala) # print chai class obj refrence
print(f'Masala {masala.origin}')
print(f'Masala {masala.is_hot}')
# Masala India
# Masala True

#modifing default value
masala.is_hot = False

print(f'Masala {masala.origin}')
print(f'Masala {masala.is_hot}')

# Masala India
# Masala False

#each namespace has its own namespace, which doesnt affect other obj by default

# adding one more prop in the the obj
masala.flavour = "Masala"
print(masala.flavour)
#Masala