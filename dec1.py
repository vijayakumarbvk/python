def smart(func):
    def inner(a,b):
        print("Im going to divide")
        if b == 0:
            print("Number is zero")
            return 
        return func(a,b)
    return inner

@smart
def divide(a,b):
    return a/b

print(divide(5,5))
