import time
start_time = time.time()

print("s",start_time)


def decorator_time(function):
    def wrapper_function():
        
        function()
        current_time = time.time()
        time_taken = current_time-start_time
        print(time_taken)
    return wrapper_function

@decorator_time
def faster():
    for i in range(1000000):
        pass
    print("faster")


@decorator_time
def slower():
    for i in range(100000000):
        pass
    print("slower")    


faster()
slower()