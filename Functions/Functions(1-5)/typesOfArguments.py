
# Types of Arguments

# Default Argument
def greet(name, message="Good Morning"):    
    print(name, message)

greet("DevOps")     # here 2 arguments are needed but if only one is passed, for a safer side default argument is passed


#  KeyWord Arguments
def gree(name, age, message):
    print(message, name , "Your age is", age)

gree(name="Anurag",age=22,message="Hii")

# Positional Arguments

def add_numbers(x ,y):
    print("x ",x)
    print("y ",y)
    print(x+y)

add_numbers(6,5)


# variable number of arguments

def sum_numbers(*args):     # to make use of variable number of arguments used *args
    print(type(args))
    print(args)

    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_numbers(1,2,3,4,5))


def add_numbers(a,b,*args): # *args should be the last paramaters
    print(a)
    print(b)
    print(args)
    print(*args)

add_numbers(1,2,8,5,9)


def add_numbers(*args,a,b): # *args should be the last paramaters
    print(a)
    print(b)
    print(args)
    print(*args)

add_numbers(1,2,8,5,9,a=87,b=78)


def display_info(**kwargs):                    # kwargs always be the last parameter
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key, "->", value)

display_info(name="CoolDude", age = 99, city="Mumbai")



