
def safe_division(a, b):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numbers allowed")
    
    if b == 0:
        raise ZeroDivisionError("Cannot divided by zero")
    
    return a / b
    
    



def use_division(a, b):
    
    try:
        result =  safe_division(a, b)
    except ZeroDivisionError:
        print(f"Could not divide {a} by {b}")
    except TypeError:
        print("Has to be a number")
    else:
        print(f"Result: {result}")
    finally:
        print("Bye bye")



# use_division(6, 3)
use_division(10, 0)
# use_division("3", "2")