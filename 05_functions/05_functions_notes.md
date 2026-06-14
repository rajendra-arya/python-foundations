# Functions (`def`)
- just a wrapper to wrap your code
- syntax
    
    ```py
    #defination
    def function_name(parameter1, parameter2):
        #function body
        return something #optional

    #call
    function_name(argument1,argument2)
    ```
- helps in : 
    1. Reducing code duplication()
    2. Splitting complex tasks
    3. Hiding implementation details
    4. improving the readablity
    5. improving traceability
    - all prg details in 01-05 in function dir

    40,41

    ## Scopes and Name Resolution
    1. Local - inside a function, the inner most
    2. Enclosing - from outer(parent) function if nested
    3. global - Top level script, u can access it anywhere
    4. Built in - Predefined keywords and functions

    Take it like a society(all public service) as global scope and differnt house as local scope. One house cant access another house, but all house can access all society public services.
    ai example:
    🏢 Built-in: Government laws. Every person in the country can use them.
    🏡 Global: The neighborhood park. Every house in the society can use it.
    👨‍👩‍👧 Enclosing: The parent's room. Only family members inside that house can use it.
    🧒 Local: A child's diary. Only that specific child can read it.

    ```py
    # 1. Built-in (print)
    x = "Global"  # 2. Global Scope

    def outer():
        x = "Enclosing"  # 3. Enclosing Scope
        def inner():
            x = "Local"  # 4. Local Scope
            print(x)
        inner()

    outer()

    ```

## nonlocal and global Scopes : for modification
1. `nonlocal` 

    - to modifiy the outer(just above/nearset enclosing) function inside local scope. Not the global scope.
    - it looks for just above the function noting ahead.
    - u can access just above in your function i.e encolosing scope.
    ```py
    def outer_function():
    msg1 = 'Enclsoing Scope'
    def inner_function():
        nonlocal msg1
        msg1 = 'Local Scope'

    inner_function()
    print('Msg 1:',msg1)

    outer_function()
    #Output : Msg 1: Local Scope
    ```
2. `global` 
    - to modify the global scope var
    - be extra extra caution in updating global var, as it can break the code.
    - u might break someone code who is dependent on the global scope vars thats y lot of people avoid using global.
    - it can be useful in some cases.
    - u can access global var from anywhere in your file present in global space.
    
    ```py
    chai_type = 'Plain'

    def front_desk():
        def kitchen():
            global chai_type
            chai_type = 'Irani'
        kitchen()

    front_desk()
    print('Final global chai:', chai_type)
    #Final global chai: Irani
    ```



## Handling arguments in Functions
- be careful about whats mutabable (Lists, Sets, Dictionaries, User-Defined Classes) and whats not.
    ```py
        chai = [1,2,3] #list i.e mutable
        def edit_chai(cup):
        cup[1] = 42 #original will also change by this
        edit_chai(chai) #[1, 42, 3]
        print(chai) #[1, 42, 3]
    ```
1. positional args
    - when we know position of function parameters we use this
    - ```py
        def make_chai(tea,milk, sugar):
        print(f'Tea: {tea}, Milk: {milk}, Sugar: {sugar}')

        make_chai("Darjeeling","Yes", "Low")
        #output
        #Tea: Darjeeling, Milk: Yes, Sugar: Low
    ```

2. keyword argument 
    - when u unsure about the position of the arg, we use param_name=value aka keyword=argument 
    - order doesn't matter 
        - we don't care about the params positions/order in arguments, we can swap any parms.
     - ```py
        def make_chai(tea,milk, sugar):
        print(f'Tea: {tea}, Milk: {milk}, Sugar: {sugar}')

        make_chai(tea="Great", sugar="Medium", milk="No")
        #output
        #Tea: Great, Milk: No, Sugar: Medium
    ```

3. agrs and kargs(key value args) mixture
    - *arg : all args will be in tuple
    - **karg : all args will be in dictionary(key value)
    - Rule : positional first, then keywords
        - Positional arguments can never come after a keyword argument.

    - ```py
        def special_chai(*ingredients, **extras):
        print("Ingredients", ingredients)
        print("Extras", extras)
        
        special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="yes") #some params have name some doesn't
        
        # Output : 
        # Ingredients ('Cinnamon', 'Cardmom')
        # Extras {'sweetner': 'Honey', 'foam': 'yes'}

        special_chai("Cinnamon", city="Delhi", age=30) : This works (positional first, then keywords) 
        special_chai(name="Alice", 30, city="Delhi") : This crashes with a SyntaxError (positional after keyword)
    ```

     
4. default value in argument 
    - default value : `def chai(name='jhon doe'):`
    - default value of string works well
    - when using array as default value it has catch aka default trap
    ```py
    ## prodution tips  #default value
        # def chai_order(order=[]):
        #     order.append("Masala")
        #     print(order)

    #scenario running twice
        # chai_order() #['Masala']
        # chai_order() #['Masala', 'Masala']

    #fix
    def chai_order(order=None):
        if order is None:
            order = []
        print(order)

    chai_order() #[]
    chai_order() #[]
    ```


## Handling multiple return
1. return Nothing
    - it implicitly returns `None`
    - ```py
        def idle_chai():
            pass
        
        print(idle_chai())
    ```

2. return one Value
    ```py
    def sold_cups():
    return 120

    print(sold_cups()) # Output : 120
    total = sold_cups()
    print(total) #Output : 120
    ```


3. early return from a function
    - once return is written next line won't run, as it act as finishing line.
    - ```py
        def chai_status(cups_left):
            if cups_left ==0:
                return 'Sorry chai over!'
            return "Chai is ready"
            print('after return message') #it won't be executed i.e return early

        print(chai_status(0)) #output : Sorry chai over!
        print(chai_status(10)) #output : Chai is ready
    ```


4. returns multiple values
    - returns miltiple values by unpacking in same no. of var
        - 
        ```py
        def chai_report():
            return 100,20 #sold , remaning

        chai_report() # nothing will be printed

        sold , remaining = chai_report()
        print(f'Sold: {sold}, Remaing: {remaining}')
        #Output -> Sold: 100, Remaing: 20
        ```

    - unpacking error can cause when return values not equal to unpacking values
        1. fix1 : use _ to ignore all not required values
            - `sold , remaining , _ = chai_report()`
            - it jst means i know but i never gonna use them, used by exp dev lot
        2. add extra unpacking variable
            - `sold , remaining , _ = chai_report()`

    ```py
    #1
    def chai_report():
        return 100,20,39 #sold , remaning, unpaid

    chai_report() # nothing will be printed

    sold , remaining , _ = chai_report()
    print(f'Sold: {sold}, Remaing: {remaining}')
    #Output -> Sold: 100, Remaing: 20
    
    #2
    def chai_report():
        return 100,20,39 #sold , remaning, upaid

    chai_report() # nothing will be printed

    sold , remaining , not_paid = chai_report()
    print(f'Sold: {sold}, Remaing: {remaining}')
    #Output -> Sold: 100, Remaing: 20
    ```

    ## Types of fuctions
    1. Pure vs Impure
        1. Pure : normal function which doesn't modify global var
        2. impure : function which modifies global var
        ```py
        def pure(water):
            return water*10
        
        total = 100

        #not recommended , as it can lead to conflicts
        def impure(water):
            global total 
            total+=water #this is the impurity
            return total
        ```
    
    2. Recursive functions
        - a function that call itself
        - ```py
            def pour_chai(cups):
                print(cups)
                if cups==0:
                    return 'All cups served!'
                return pour_chai(cups-1)

            print(pour_chai(3))
            ```
        - `return` #exits the function avoid RecursionError: maximum recursion depth exceeded -1 -2...
            - ```py
                def pour_chai(cups):
                    print(cups)
                    if cups==0:
                        print('All cups served!')
                        return #exits the function avoid RecursionError: maximum recursion depth exceeded -1 -2...
                    pour_chai(cups-1)
            ```
        
    3. lambdas (Anonymous) functions
        - a function without a name
        - used when we won't use a function anywhere else
        - standard name : anonymous function
        - syntax : 
            - `lamba i: i='value'` #i=current value
        - ```py
            chai_types = ['kadak','lemon','masala','milk','masala']
            chai_menu = list(filter(lambda type: type!='masala',chai_types)) #filter-> refrence-> convert to list
            print(chai_menu)
            ```

        - method notes: 
            - `filter`(function,iterable) 
                - Returns true values.
                - Returns a filter iterator object (a reference), not a `list` of values.
                - Holds a REFERENCE (an iterator object), not values, to save memory.
                - Can be converted to any datatype.


            - `list()` ->
                - Converts an existing iterable (string, tuple, dict, or filter) into a new list.
                - It takes out the data (unpacks the reference).
                - Example: list('abc') turns into ['a', 'b', 'c'].

## Built-in function
- Python built-in functions are predefined functions that are always available in the global namespace, 
- meaning you can - use them instantly without importing external modules or writing extra code 
- go through built-in function from [official url](https://docs.python.org/3/library/functions.html)

- basic example :
    ```py 
    def func_name():
    pass```
- 
### Documenting a function
 - __ : dunder(short of 'double under'score)
    - purpose:
    - eg. __doc__ : dunder doc for fetching documentation of a function
    - ```py
    #helpful for debuging
    print(chai_flavor.__name__) #name of function
    print(chai_flavor.__doc__) #returns the function doc(first line)

    help(len)  #to know about any builtin function u can use help
    # help(chai_flavor)
    ```
- sample example: recomended way 
```py
    def generate_bill(chai=0, samosa=0):
        """
        Calculate the total bill for chai and samosa

        :param chai: Number of chai cups (10 rupees each)
        :param samosa: Number of samosa (15 rupees each)
        :return: (total amount, thank you message)
        """
        total = chai*10 + samosa*15
        return total,'Thank you for visiting!'

print(generate_bill.__doc__)

- add built method function overview
``` 


## Imports , Modules and  Init
1. all import
    `import filename.py`
2. named import
    `from filename import func_name`
    `from filename import func_name1, func_name2`

3. relative import
    - from . current direct
    - from .. parent(1 dir back) directory
    - `from .foldername import`
    - `from ..parentfoldername import`
not recomended :
    `from masala_chai import *` #we don't what its bringing

### __init__.py

- we dont write anything in this file , presence of this file converts the folder(eg. recipe folder) into python module
- it can also contain intialization code, but thats optional
- it just for python internal architecture but after python >= 3.3 it's also obselete.
- check chai_business folder
```py
#all import 
# import recipes.flavours #folder.filename #fetching whole book

# print(recipes.flavours.elaichi_chai()) 

#named import
from recipes.flavours import elaichi_chai, masala_chai
print(elaichi_chai())

#relative import .
from .recipes.flavours import masala_chai

#avoid this 
from recipes import *
# https://stackoverflow.com/questions/37139786/is-init-py-not-required-for-packages-in-python-3-3
```
- It is true that Python 3.3+ supports Implicit Namespace Packages that allows it to create a package without an __init__.py file. This is called a namespace package in contrast to a regular package which does have an __init__.py file (empty or not empty).

- However, creating a namespace package should ONLY be done if there is a need for it. For most use cases and developers out there, this doesn't apply so you should stick with EMPTY __init__.py files regardless.

