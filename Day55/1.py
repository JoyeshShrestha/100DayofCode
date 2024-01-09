input = eval(input())


def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0],args[1],args[2])
        print(f"It returned: {result}")
        return result
    return wrapper



@logging_decorator
def a_function(a,b,c):
    return a * b * c


result = a_function(input[0], input[1], input[2])
print(result)