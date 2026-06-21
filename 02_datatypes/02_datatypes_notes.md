## Datatypes

## mutable and immutable
- no. are mutbale 
- 2  or 12 both are mutable
- id(2) -> id of no. means the memory id is immutable


## Dataypes:
1. Numbers : integers 
- +,-,/ are same
- /  with decimal
- // before decimal
- 1_000 -> same as 1000 , python supports redablility more so it ignores _ in 1_000
- % for remainder

2. boolean
- automatic upcast the value in arthmetic operation( False becomes 0 and True becomes 1)
- bool(0) -> False, 0, null, none also give False rest all True
- bool('hi') -> True

3. Real numbers => use library like Fractions , decimal

   - 95.5 - 95.499999999999 =  9.947598300641403e-13
   - when u need to deal with higher no. there are packages for precisions
   - sys.float_info #it will give float info ur system can go for ,depends on your system hardware
   - while dealing with fractions u can these popular packages which will display more digits afre decimal
    - `from fractions import Fraction`
    - `from decimal import Decimal`
   - used by scientist 
   
4. complex number  (2+3j) - use library Fractions


# Strings - immutable

1. core
   "any text"
   - its immutable - once memory ref is done it cant be changed
2. indexing : air -> 0=a,1=i,2=r
3. slicing
   - - last no is not inclusive

   a. [first:last:step]
   b: name = "rajendra"
   ```
   [0:] -> rajendra
   [0:7] -> rajendr #as 7th is a and its last no.
   [::2] -> 'rjnr' #skips 1 alphabet, default is 1 which is normal rajendra
   [::-1] -> ardnejar #reverse the string
   ``` 
4. encoding-decoding sepcial charcter like tilda
- use utf-8,16,32 for encoding and decoding special character
- useful for diffrenet lang like japanses,medarian etc
- we use encode/decode method for desired string
- name.encode("utf-8")
- name.decode("utf-8") #for desplaying



# Tuples - immutable
`x = ("a","b","c")`
- upacking tuple in variable
(c,d,e ) = x 

- variable assigning
`var1 , var2 = 1, 2` #no need to (1,2)
#output -> var=1 , var=2

- variable swaping
`var1 , var2 = var2 , var1`
#output -> var=2 , var=1

- membership testing
   - it's case sensitve
   - `in` works with tuple (like include in js)
`print(f'Does x has a? {'a' in x}')`
#output Does x has a? True


# Mutable

# List
1. List (Array in other lang)
ingredients = ['water','milk','black tea']
water - 0 position
water - 1 position

2. List methods
- .append('sugar') -> add at the end 
- .remove('milk') -> remove specific item
- .pop() ->remove last item, and returns it.
- .insert(index,'content') -> places the content in that index and pushes the current index content in index+1 position
-  chai_ingredients.extend(spice_options) -> merge two list, add the extended list at the end
- .reverse() -> reverse whole list(items order inverse), can't do directy in print startment as its mutable
- .sort() -> sort alphabetlically in the list
- .max(Listname) -> return max item
- .min(Listname) -> return min item

### Operator  Overloading
- `+` it just concatinating list with operator
   - `list1 = ['1','2']`
   -  `list2 = ['3']`
   - `final_list = list1 + list2`
   -  #output ['1','2','3']

- `*`
   - `['hot']*2`
   - `['hot', 'hot']`
   - `['hot','cold']*2`
   - `['hot', 'cold', 'hot', 'cold']`

- `from operator import itemgetter` : we can bring operation like operator overlading using it

> Question : convert a string into a List?

`raw_spice_data = ['CINNAMON'] `
good but then u have 1 element in the list, 
we want a list of just this string.
'CINNAMON'
the solution is bytearray 

3. **bytearray()**
- its a method bytearray(b'string')
- returns a new array of bytes.
- mutable sequence of integers 0-256
- u cant use method same way like list
- `raw_spice_data = bytearray(b"CINNAMON")`
- `raw_spice_data = raw_spice_data.replace(b'CINNA', b'CARD')`
   -  #this will assign new byte array in the var
- `print(f'Bytes: {raw_spice_data}')`
- #output Bytes: bytearray(b'CARDMON')



# Set
`essential_spices = {'cardmom','ginger','cinnamon'}`

- this is one way to write a set, there are other ways as well but this one is easy.
- known for uniqueness
- same as sets in maths, intersection, union etc
- everything should be unique
- if merge two set it will only take unique values

>| -> union(pipe operator) all unique values
`set1 | set2`


> & -> common values
`set1 & set2`


>`-` (minus) -> keeps items only in belongs to one set , removes the common items 
`set1 - set2`

- membership test
   - we use in opertor here
print(f"is 'cloves' in optional spices?{'cloves' in optional_spices}")


#### **frozenset** 
- working wise same as set
- useful in building immutable unordered collection of unique elements.



# Dictonary
- when u need a customized index use dictonary
- syntax(3 ways)
   - ```x_dict = dict(key1='value1', key2='value2')`

   - ```y_dict = {}
   - y_dict['key1'] = 'value1'
   - y_dict['key2'] = 'value2'``
 
   - z_dict = {key1:'value1', key2:'value2'}

-  x_dict['key1'] -> get value -
- delete item -> del x_dict['key1']
- 'key2' in x_dict -> membership testing
- x_dict.keys() -> get all keys
- x_dict.values() -> get all values
- x_dict.items() -> get all pair in each tuple
- x_dict.popitem() ->remove last item(key-value pair)

- x_dict.update(z_dict) -> to z_dict items after x_dict , basically merging

- handling unavailable keys in the dict?
   -  x_dict['note'] -> it wil crash the application
   -  safe code 
   .get -> works like ternary operator
   x_dict.get['desiredkey','fallback/default value']
   `x_dict.get['note','No note'] `
   if note key not present returns no note
- all methods we studied in set can be applied in the dict as well.


# Advance Datatypes: (u need import these modudle)
1. datetime
2. time
3. calendar
4. timedelta - delta means time differnce
6. arrow
   `import arrow`
   `brew_time = arrrow.utcnow()`-> gives utc time
   `brew_time.to('Europe/Rome') `-> converts into that time zone
7. dateutil
8. collections 
   - this is a big thing in python
   - u can check in its doc
   - `from collection import namedtuple`
   - `chaiProfile = namedtuple("chaiProfile", ['flavour','aroma'])` -> give name to tuple
   - it's built on basic things like strings, array
   - it's used in special usecases

