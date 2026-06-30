# Accessing the Base Class
class BaseChai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# Adding more property in the base class

# Approch 1: Code duplication 
# class GingerChai(BaseChai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_ #code repetition
#         self.strength = strength #code repetition
#         self.spice_level = spice_level

# obj = GingerChai('s','strong','light')
# print(obj.spice_level) #output: light


# Approch 2: Explicit Call
# class GingerChai(BaseChai):
#     def __init__(self, type_, strength, spice_level):
#         BaseChai.__init__(self,type_, strength) #explicitly calling the constructor of the inhereted class
#         self.spice_level = spice_level

# obj = GingerChai('s','strong','light')
# print(obj.spice_level) #output: light


# Approch 3: Super (most preferred)
class GingerChai(BaseChai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength) #calling the base call using super()
        self.spice_level = spice_level #adding additional propeties

obj = GingerChai('s','strong','light')
print(obj.spice_level) #output: light