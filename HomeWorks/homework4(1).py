def square_result(func):
    def wrapper(a,b):
        result = func(a,b)
        return result ** 2
    return wrapper

@square_result
def add(a,b):
    return a + b

@square_result
def sub(a,b):
    return abs(a - b)

print(add(2, 3))
print(sub(6,12))
