# It stores data in key value pair
# It is unordered 
# It is mutable
# key has to be unique
# can keep heterogeneous data
# key has to be immutable
# key can be int / string / boolean / tuple

students_details = {'name':'Vishwa','age':'22','city':'bangalore'}

print(students_details)
print(type(students_details))


dict1 = {1:'Vishwa', 2:'Mohan', True : 'Love'}
print(dict1)
# in python TRUE is 1 and FALSE is 0

dict1 = {3:'Vishwa', 2:'Mohan', True : 'Love'}
print(dict1)

# Dictionary constructor method
dict2 = dict(name='Vishwa', age='mohan')     # dict is used as constructure
print(dict2)
print(type(dict2))


# Access the element of the dictionary

students_details = {'name':'Vishwa','age':'22','city':'bangalore'}

print(students_details['name'])
print(students_details['age'])

# Get the list of keys
print(students_details.keys())

# Get the list of values
print(students_details.values())

# Get the list of all items
print(students_details.items())

# Add elements in the dictionary
students_details = {'name':'Vishwa','age':'22','city':'bangalore'}

# 1)
students_details['country'] = 'India'
print(students_details)

# 2) add from 1 dict to another dict

marks_detail={'English':'100', 'Maths':'70', 'Science':'92'}
students_details.update(marks_detail)
print(students_details)


# Remove elements in the dictionary 

#using key
print(students_details.pop('city'))
print(students_details)

# removes the last element added
print(students_details.popitem())
print(students_details)

# del keyword

del students_details['age']
print(students_details)

# clear method (to empty the dictionary)
students_details.clear()
print(students_details)