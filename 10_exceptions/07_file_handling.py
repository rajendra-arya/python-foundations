
# Traditional way
file = open("order_traditional.txt", "w")   #opens file or create if not exists and give ref to the var

try:   
    file.write("Masala Chai -- 2 cups \n--> created using Traditional approach.") # write on that file (its error prone syntax)
finally:
    file.close #close and remove the file from the memmory

# Output: it will create a file(order_traditional.txt) with it's contents



# Modern way
with open("order_modern.txt", "w") as file: #open the file in write mode give ref to var file.
    file.write("Ginger Tea -- 4 cups\n--> created using Modern approach.") # write on that file

# Output: it will also create a file(order_traditional.txt) with it's contents


