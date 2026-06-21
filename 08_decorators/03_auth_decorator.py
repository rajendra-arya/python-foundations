from functools import wraps

def require_admin(func):
    wraps(func)
    def wrapper(userrole):
        if(userrole != 'admin'):
            print('Access denied: Admins only')
            return None  #We use return None to explicitly signal that a function intentionally ended without a valid result
        else:
            return func(userrole)
    return wrapper

@require_admin
def access_inventory(role):
    print('Access granted to Inventory.')

access_inventory('user') #Access denied: Admins only
access_inventory('admin')