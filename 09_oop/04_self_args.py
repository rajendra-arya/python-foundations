class Chaicup:
    size = 150 #ml

    def describe(self):
        # return print(f'A chai cup of {self.size} ml.') # print display and retrun none (remember)
        return f'A chai cup of {self.size} ml.'
    

cup_obj = Chaicup()
print(cup_obj.describe()) # passes the cup obj to self argument automatically

# print(Chaicup.describe()) # trigger error as it needs context 
# TypeError: Chaicup.describe() missing 1 required positional argument: 'self'

print(Chaicup.describe(cup_obj)) 


cup2_obj = Chaicup()
cup2_obj.size = 50
print(cup2_obj.describe())
print(Chaicup.describe(cup2_obj))