#generators:
# normal function
def func_example():
    return ["Cup 1", "Cup 2","Cup 3"] 
print(func_example())  #stores in memory
#['Cup 1', 'Cup 2', 'Cup 3']


# generators
def gen_example():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

print(gen_example())  # gives refrence of object in the memory
# <generator object gen_example at 0x0000023381EA5BC0>


print(next(gen_example())) #Cup 1
print(next(gen_example())) #Cup 1

cups = gen_example()
print(cups)


print(next(cups)) #Cup 1
print(next(cups)) #Cup 2
print(next(cups)) #Cup 3
print(next(cups)) #Error : StopIteration: error exceeded the total yield