def serve_chai(flavour):
    try: #error prone code inside
        print(f"Preparing {flavour} chai order...")
        if flavour == 'unknown':
            raise ValueError("Sorry! Flavour Not Avaiable")
    except ValueError as e: # Handle invalid flavour
        print(f"Error : {e}")
    else:   # Run only if no error
        print(f"{flavour} Chai is Served.")
    finally: #run always at the end
        print('Next Order Please!\n')


serve_chai('masala') # runs smoothly
# try -> if condition fails -> else -> finally
serve_chai('unknown') # throw and handles error
# try -> if condition true -> raise error -> catches by except -> finally 


## Output
# masala Chai is Served.
# Next Order Please!

# Preparing unknown chai order...
# Error : Sorry! Flavour Not Avaiable
# Next Order Please!