from functools import wraps

def authorize(func):
    #This function separates the authorization logic from the access granting logic so different authorization methods can easily be added without touching the access granting code.
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        authorized_roles = ['admin', 'superuser']
        if user_role in authorized_roles:
            print(f"Access granted to user with role: {user_role}")
            return func(*args, **kwargs)
        else:
            print(f"Access denied for user with role: {user_role}")
            return None
    return wrapper

@authorize
def sensitive_function(data):
    print(f"Processing sensitive data: {data}")
    return "Sensitive data processed."

# Example usage
sensitive_function('admin', 'Top Secret Information')
sensitive_function('guest', 'Top Secret Information')