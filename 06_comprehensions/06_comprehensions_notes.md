# Comprehensions
 **Concise way to create dataypes** (list, set, dictonary, generators) in python 
**using one line**.

- Use:
    - filter items
    - transform : usd -> rupped
    - create new collection
    - flatten nested structure

- puprose:
    - cleaner code
    - faster execution

## Types of Comprehensions
    1. List
    2. Set
    3. Dictonary
    4. Generator (not a datatype)

##  List Comprehensions []

1. `[expression for item in iterable if condition]`
    expression : 
        - for loop current item(if if condition not given u get all values in the list)
        - its the final return value f
                
    sytnax: 
    ```py
        # [expression item in iterable if condition]
        iced_tea = [current_item for current_item in menu if 'iced' in current_item.lower()]
    ```
<!-- 2. if + else (At the FRONT) = Replace
    - Keeps all items, but changes them. The new list is the same length.
    - Syntax: [ item if 'iced' in item else 'Hot' for item in menu ]
    - read more -->


## Set Comprehensions {}
- returns unique values
- syntax : `{expression item for item in iterable}`
    - #if condition is optional
    - expression : its the final return value
        - its the final return value from the condition start from loop and see where is final result

-example : iterating from dictonary to get unique values
    ```py
    #iterating from dictonary to get unique values

    favorite_chais = ['Green Tea', 'Masala Tea', 'Elaichi Tea', 'Green Tea', 'Lemon Tea','Masala Tea']
    #set comp

        unique_tea= {tea for tea in favorite_chais} #if condition is optional
        # {'Elaichi Tea', 'Lemon Tea', 'Green Tea', 'Masala Tea'}


        sorted_unique_tea = {tea for tea in sorted(favorite_chais)} #sorted returns a sorted list
        # {'Green Tea', 'Masala Tea', 'Elaichi Tea', 'Lemon Tea'}

        # unique_tea_len_gt10 = {tea for tea in favorite_chais if len(tea)>10} #if condition is optional
        # {'Elaichi Tea'}

        print(favorite_chais)
        print(sorted_unique_tea)
    ```

- example of nested comp : remember first var is the final output
    - ```py
        ##nested comp
        # find all unique spices from the recipes

        recipes  = {"Masala Chai":["ginger","cardamom","clove"],
                    "Elaichi Chai": ["cardamom","milk"],
                    "Spicy Chai": ["ginger","black pepper","clove"]}

        #Spice :final output
        unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
        print(unique_spices)

        # this has reduced this much code
        # unique_spices = set() 
        # for ingredients in recipes.values():
        #     for spice in ingredients:
        #         unique_spices.add(spice)

    ```


## Dictonary Comprehensions {}
- same as set but difference is how we store the final output value.
- we store the expression in key-value pair
- sytanx : `key:value for key,vlaue in iterable.items()`
- example : convert inr to usd
```py 
    tea_prices_inr = {"Masala Tea":40,
                    "Green Tea":50,
                    "Lemon Tea":200}

    tea_prices_inr = {key: f"₹ {round(value/90,2)}" for key, value in tea_prices_inr.items()}

    print(tea_prices_inr)
    # {'Masala Tea': '₹ 0.44', 'Green Tea': '₹ 0.56', 'Lemon Tea': '₹ 2.22'}
```

## Generator Comprehensions () for Memory Optimization

- used entirely for saving the memory.
- it gives constant flow of items as you require them
    - means gives value one by one in a stream rather than like list comp []
- difference :
    1. list : [x for x in items]
        - make entire list in memory
        - [5, 10, 12, 6, 4, 24, 44, 8, 17]
    2. generator : (x for x in items)
        - <generator object <genexpr> at 0x000002957DD8B440>
        - gives constant flow of item
        - more like a stream , give one item at a time
        - useful for further processing like sum() filter operation

- example:

    ```py
        daily_sales = [5, 10, 12, 6, 4, 24, 44, 8, 17]

        # find daily sales > 5
        total_cups = [sale for sale in daily_sales if sale>5] #returns complete list
        total_cups_gen = sum(sale for sale in daily_sales) # returns value one by one
        print(daily_sales)
        print(total_cups) #[10, 12, 6, 24, 44, 8, 17]
        print(total_cups_gen)  #130
    ```

<!-- make proper note , for generator too -->