# Loops

> Remeber range() is never inclusive i.e last item is not inclusive.
    - `range(start,end)`,-> start to end-1
    - `range(end)`  -> 0 to end-1

> enumerate()

# 1. for
- used for iterating items known number of times.
- requires a sequence of a fixed, predetermined length to iterate over.
- `for` loop is optimized for repeating code a known number of times.


- ```py
    for item in iterable:
        # Code block to execute
        print(item)
    ```

## with range
```py
for token in range(10):
    print(f'Serving chai to Token #{token}')
```

## with list
```py 
orders = ['rajendra','aman','shubham', 'rohit']

for name in orders:
    print(f'Order ready for {name}.') 
```

##  with enumerate(iterable,start=0)
-  returns index and item in a tuple form for a list
-  default -> `enumerate(iterable,start=0)`
    - [(0, 'Green'), (1, 'Lemon'), (2, 'Spiced'), (3, 'Mint')]
- `enumerate(iterable,start=3)`
    - [(3, 'Green'), (4, 'Lemon'), (5, 'Spiced'), (6, 'Mint')]
- It returns a lazy memory-saving object that generates (counter, item) tuples one at a time when asked.

```py
#demo
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# list(enumerate(seasons))

menu = ["Green", "Lemon", "Spiced", "Mint"]

for  idx,item in enumerate(menu,start=1):
    print(f'{idx}: {item}')

#output
#1: Green #2: Lemon #3: Spiced #4: Mint
```

## with zip()
- to combine two or more list
- `zip(iterables)` 
- `zip(a, b, strict=False)` (default) Truncates to the shortest length. Discards extra items.
- `zip(a, b, strict=True)` Enforces equal item counts.Raises ValueError
- `itertools.zip_longest(a, b)` Extends to match the longest length.Fills gaps with None. 
- Iterate over several iterables in parallel, producing tuples with an item from each one.

```py
names = ['raj','sanjay','allu','rashmika']
bills = [100,20,55,88]

for name,bill in zip(names,bills):
    print(f'{name} paid {bill}.')
```




# 2. while
> `for` loop is optimized for repeating code a known number of times, while a `while` loop is designed to repeat code indefinitely until a specific condition changes.**
- intialization
- while(conditioncheck)
   - runs until condition fails
   - update

```py
temp=40
while(temp < 100):
    temp+=15
    print(f'temp is {temp}')

print('Tea is ready to boil!')
```

# continue -break
- `continue` -  used for skiping the current loop(iteration)
- `break` - used for breaking out complete loop, i.e abort

# 3. for-else
- The Core Rule -> 
    - No Break → else runs.
    - Hit Break → else is skipped.
- fallback logic.
- if loop didn't `break`(break condition not satified) then only else will run .
- eg.searching prg
- why use it? 
    - It removes the need for temporary flag variables (like found = False) when searching for items in a list.
 
```py
staff = [('Amit',16),('Jay',12),('Rohit',14),('Rajendra',17)]

for x,y in list:
    if(x>18):
        break: # Skips else completely
else:
    print('No one is eligible') # Runs only if no break happened
```
# if one condition satifies then it doesn't come to else loop?
no, if one break condition satifies then it won't run the else loop.

> a=2 : assignement | a=2+2 : expression returns a value 

# Walrus := 
- assiging expression on the go to the variable
- traditional way 
    - `a = 20+20`
    - `if a==40: print("its 40")`
- walrus way -> `if a:=20+20:print("its 40")`
- the variable can be used same as other var
- Needs Parentheses: Use if (a := 20+20) == 40: so Python evaluates math before assignment.
- Scope Persists: Variable a stays alive and usable even after the if block ends.
- Best for Loops: Great for while line := file.read(): to read and check data at once.
- Saves CPU: Stops double-running heavy functions inside list comprehensions.
- Readability Rule: Never use it on standalone lines; use standard = unless it saves space.

```py
# a = 20+20
# if a==40: print("its 40")
# if a:=20+20:print("its 40")

#run once to check
# flavors = ['ginger','lemon','mint']
# if (requested:=input('Enter your size: ')) in flavors:
#     print(f'{requested} is available.')
# else:
#     print(f'{requested} not available.')


#endless loop until available size user enters
# available_size = ['sm','md','xl']
# while((requested_size := input('Enter your size: ')) not in available_size):
#     print(f'{requested_size} is not available. Please try other sizes.')

# print(f'{requested_size} is available.')

```



## dict instead of ifelse or match
- use dict instead of repeted cases (if or match)
- this is done in production codes, following is the example of a scalable code

```py
# process user and give discounts based on provided dicounts.
users = [
    {"id":1,"total":480,"cupon":"P20"},
    {"id":2,"total":150,"cupon":"F20"},
    {"id":3,"total":80,"cupon":"P50"},
    ]

#we can use if else or match too but more recommened way by dictionary

#disount given percent and flat/fixed(exact money) value
discounts = {
    "P20" : (0.2,0),
    "F20" : (0,20),
    "P50" : (0.5,0)
}

for user in users:
    percent , fixed = discounts.get(user['cupon'],(0,0)) #(9,0 is default value)
    discount = user['total'] * percent + fixed
    print(f"id {user['id']} paid {user['total']} and got next vist discount of {discount} rupees.") 

```