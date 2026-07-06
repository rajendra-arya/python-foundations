# raise your own errors/exceptions
def brew_chai(flavour):
    if flavour not in ["masala","ginger","elaichi"]:
        raise ValueError(f"{flavour}: Not Supported Value.")
    print(f"Brewing {flavour} chai...") #if no error it will execute

brew_chai("ginge")

# output
# Traceback (most recent call last):
#   File "04_custom_exceptions.py", line 7, in <module>
#     brew_chai("ginge")
#     ~~~~~~~~~^^^^^^^^^
#   File "04_custom_exceptions.py", line 4, in brew_chai
#     raise ValueError(f"{flavour}: Not Supported Value.")
# ValueError: ginge: Not Supported Value.