# No duplicates / elements are unique
# mutable
# unordered
# heterogeneous     can store multiple data type


my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

s1 = {1,4,5,2,1,9,7,4,1}
print(s1)               #it ensures that there are no duplicates

s2 = set()              #constructor 
print(s2)               # will print a empty set

s3 = set({5,6,7})       #constructor set through tuple
print(s3)


#Add
s = set()

s.add(5)
s.add(13)
s.add(5)        # it doesn't add duplicate values
s.add(12)
print(s)        # prints {13,12,5} which means set is an unordered data type

#Remove

s4 = {3,9,7,4}
print(s4.discard(7))    # removes 7
print(s4)

# removing the element which is not present in the set
'''
s4.remove(12)       # raises an error
print(s4)
'''


#    FROZEN SET an immutable set

fs = frozenset([1,2,3])
print(fs)
print(type(fs))

fs2 = frozenset({1,2,3})
print(fs2)

dict1 = {'fs2':'Vishwa'}
print(dict1)
print(type(dict1))
