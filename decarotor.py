

def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("count:", count)
        return func(*args, **kwargs)

    return inner




def logger(func):


    def inner(*args, **kwargs):
        print(f"Runing {func.__name__}")
        return func(*args, **kwargs)

    return inner





@logger
@counter 
def add(a, b):
    return a + b




@counter
def multiply(a, b):
    return a * b




print(add(1, 2))
print(add(3, 4))



print(multiply(2, 3))