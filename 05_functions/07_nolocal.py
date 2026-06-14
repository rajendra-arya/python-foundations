# def outer_function():
#     msg1 = 'Enclsoing Scope'
#     def inner_function():
#         nonlocal msg1
#         msg1 = 'Local Scope'

#     inner_function()
#     print('Msg 1:',msg1)

# outer_function()

def update_order():
    chai_type = 'Elaichi'
    def kitchen():
        nonlocal chai_type
        chai_type = 'kesar'
    kitchen()
    print('After kitchen update chai type:', chai_type)

update_order()

