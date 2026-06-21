#send() : getting values in generators
def chai_customer():
    print("Welcome!, What Tea would you like to have?")
    order = yield #wait until get the value
    while True:
        print(f'Preparing {order}.')
        order = yield #wait until get the value

stall = chai_customer()
next(stall) #starting the generator

stall.send('Masala Chai')
stall.send('Lemon Tea')