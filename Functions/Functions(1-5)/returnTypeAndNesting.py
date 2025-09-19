def singleReturn(a, b):
    sum = a + b
    return sum

print(singleReturn(5,7))

def multiReturn(a,b):
    sub = a - b
    mul = a * b
    return sub, mul

print(multiReturn(9,3))

# nested function
def outer():
    print("Hello from the outer")

    def inner():
        print("Hello from the inner")
        
    return inner
    
outer()()

