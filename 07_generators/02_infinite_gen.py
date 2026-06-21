#infinte generators
def infinite_gen_example():
    count = 1
    while True:
        yield f"Refill {count}"
        count+=1

user1 = infinite_gen_example() 
print(user1) #<generator object infinite_gen_example at 0x0000015524D36680>

user2 = infinite_gen_example()
print(user2) #<generator object infinite_gen_example at 0x0000015524D35E40>

for _ in range(5):
    print(next(user1))

for _ in range(5):
    print(next(user2))
    
# ouput
# Refill 1
# Refill 2
# Refill 3
# Refill 4
# Refill 5
# Refill 1
# Refill 2
# Refill 3
# Refill 4
# Refill 5
