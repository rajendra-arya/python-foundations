begining of processing the data

# Conditionals 

## if

```py
if boolvar
    `print('if bollean value True, u will see me!')
```

- `input("texts")` -> take input, returns in string
    - .lower -> tolower case the input


## == 
```py
snack = input('Enter your snack:').lower()

if snack == 'samosa' or snack =='cookies':
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f'Sorry not available')
```

## `if elif else` -> multiple if
```py
if bvar:
    print('see me if bvar True')
elif bvar:
    print('see me if bvar True') 
else:
    print('default value / if nothing is True') 
```

## nested if 
pass ->  run without warning, handy when writting inner if later

```py
if device_status == 'active':
    if temp > 35:
        print('High temperature alert!')
    else:
        print('Temperature is normal.') 
else:
    print('Device is offline.')

```

## Ternary opertion
`type('content')` -> to check the datatype, think it as a wrapper
`int(your desired var/input)` -> convert to num if its a int(not even float) else it gonna give error. think it as a wrapper too.
`py int.input('enter no:')` -> convert numerical string into number.
if i enter rajendra it will give error

```py
# if order_amt > 300:
#     delivery_fee=0
# else:
#     delivery_fee=50
```
- what should go inside the var wihout lot of code?
- **simple way using ternary opeator we can do all above in one line**
- just in assigning time we can use ternary opertor
`delivery_fee = 0 if order_amt>300 else 50`
- assign 0 if condition satifies else assign 50


> What if there are too many if else conditons?

## match-case-case _:
- used when u have lot of if else conditions
- its clean way to write el if
- the boolean var gets input from input and matches the case
- the default case/fallback case is `case _:`

```py
seat_type = input('Enter seat type ( General / Sleeper / AC / Luxury): ').lower()


match seat_type:
    case 'general':
        print('General - Cheapest option, no reservation.')
    case 'sleeper':
        print('Sleeper - No AC, beds available.')
    case 'ac':
        print('AC - Air Conditioned, comfy ride.')
    case 'luxury':
        print('Luxury - Premium seats with meals.')
    case _:
        print('Invalid seat type.')
```

