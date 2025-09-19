# pass by value
# immutable data types : Numbers, Strings, Tuples -> Pass by Value

num = 5

def modify_num(num):
    num += 1
    print(num)

modify_num(num)

print("Original Num",num)

# Pass by Reference
# mutable data types : lists, dictionary -> Mutuable Data Type

my_list = [1,2,4]

def modify_list(list):
    list.append(5)
    print(list)

print("Before calling fuction",my_list)

modify_list(my_list)

print("After calling function",my_list)