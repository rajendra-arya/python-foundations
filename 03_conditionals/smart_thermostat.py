device_status = 'active'
temp = 38


if device_status == 'active':
    if temp > 35:
        print('High temperature alert!')
    else:
        print('Temperature is normal.') 
else:
    print('Device is offline.')




# if device_status == 'active':
#     pass
# else:
#     print('Device is offline')