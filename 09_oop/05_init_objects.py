class ChaiOrder:
    #Runs automatically to set up(initalize) object data
    def __init__(self, type_, size):
        self.type = type_  # type is reserved keyword that's y _
        self.size = size #self contains the reference of current instance
    
    # Method to read instance data using self
    def summary(self):
        return f"{self.size} ml of {self.type} chai."


order_1 = ChaiOrder('Masala', 150)
print(order_1.summary())

order_2 = ChaiOrder('Lemon', 100)
print(order_2.summary())