# Tuples are immutable
# they are ordered, in sequence, and can contain different types of data

tup1 = (3,6,1,9,10)
print(type(tup1))
print(tup1)

# using constructor tuple can be made by list, string or tuple

t1 = tuple([1,2,3])         # tuple through list
print(t1)

t2 = tuple("Vishwa")        # tuple through string
t3 = tuple(t1)              # tuple through tuple

print(t2)
print(t3)

# tuple for a single element

t = (35,)               # comma(,) is necessary for tuple with single element
print(type(t))

fruits = ('apple', 'mango', 'banana', 'apple', 'mango', 'apple','strawberry')
print(fruits.count('apple'))            #counts apple in tuple
print(fruits.count('jackfruit'))        #gives 0 as it is not present in the tuple
print("Count : ",len(fruits))
print(fruits.index('banana'))           #gives index

print(len(fruits))                      #prints length of tulip

#accessing the elements of tuple

print(fruits[3])
print(fruits[-3])

#fruits[3] = 'Jackfruit'      Tuples are immutable so no changes can be made

#slicing
print(fruits[2:7])




