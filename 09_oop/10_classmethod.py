class ChaiOrder:
    def __init__(self, tea_type, sweetness, size ):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['tea_type'],
            data['sweetness'],
            data['size']
        )
    
    @classmethod #modifing intilzation
    def from_string(cls, data): #first argument is cls not self
        tea_type, sweetness, size = data.split(',')
        return cls(tea_type, sweetness, size) #returs cls
    
    @staticmethod
    def welcome(): # doesn't need any argument
        # def is_valid work on it for sm lg md   
        return 'Namaste! How may i help you?'


obj1 = ChaiOrder('masala','low','md')
# print(obj1) #__main__.ChaiOrder object at 0x00000219C2D56F90>
# print(obj1.__dict__) #{'tea_type': 'masala', 'sweetness': 'low', 'size': 'md'}

# order 2
print(ChaiOrder.from_dict({'tea_type':'ginger','sweetness':'medium','size':'sm'}).__dict__)

# print(ChaiOrder.from_string('lemon,low,lg').__dict__) # {'tea_type': 'masala', 'sweetness': 'low', 'size': 'md'}



# print(ChaiOrder.welcome()) #Namaste! How may i help you?
