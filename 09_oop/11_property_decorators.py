class TeaLeaf:
    def __init__(self, age):
        self._age = age #its python convention to use _ as prefix for hiding the value
                        #_ means this property should not to be read directly 
                        #python knows this and treat this as "age" only

    @property #getter
    def age(self): #python knows this and treat this as "age" only
        return self._age + 2
    
    @age.setter #setter #py make it a decorator automatically
    def age(self, age):
        if (1<=age<=5):
            self._age = age
        else:
            raise ValueError("Tea Leaf age must be between 1 to 5 years.")
            
#getting value
leaf = TeaLeaf(3)
print(leaf.age)

#setting value
leaf.age = 11
print(leaf.age)