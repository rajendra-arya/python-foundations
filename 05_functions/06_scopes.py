# Learning local,global,enclosing scopes

def serve_chai():
    chai_type = "Masala" #local scope
    print(f'Inside(local) function: {chai_type}')

chai_type = "lemon" #global scope
serve_chai()
print(f'Outside(global) function: {chai_type}')

print('-'*50) #---------------------------------------


def chai_counter():
    chai_order = 'lemon' #enclosing scope
    def print_order():
        chai_order = 'ginger' #local scope
        print('Inner: ', chai_order)
    print_order()
    print('Outer: ',chai_order)

chai_order = 'masala'
chai_counter()
print('Global: ', chai_order)