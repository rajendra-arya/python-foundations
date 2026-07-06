chai_menu = {'masala':30,'ginger':40}

# chai_menu["elaichi"] # will cause error and stop the prg(Except)

# handling with try catch
try: 
    chai_menu["elaichi"]  # error prone code
except KeyError: #catches the error
    print("Key doesn't exists")

print("namaste") #runs the prg smoothly while handling error

#output
    # Key doesn't exists
    # namaste

# handling with .get() method
print(chai_menu.get("elaichi", "Doesn't Exists"))
# safely returns None if the key does not exist or returns the msg.
# second argument is custom default message if the item isn't on the menu.

# output - Doesn't Exists