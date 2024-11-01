# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#creat dictonary
person = {
    'firstname': 'Chris',
    'lastname': 'Wike',
    'age': 30
}

print(person['firstname'])

#add key value
person['phone'] = '555-555-5555'

print(person)

#get dict keys
print(person.keys())

#get dict values
print(person.values())

#get dict items
print(person.items())

#copy dict
person2 = person.copy()
person2 ['city'] = 'boston'

print(person2)

#remove items
del(person2['age'])

print(person2)

#get length
print(len(person))

#list of dict
people = [
    {'name': 'Marhta', 'age': 24},
    {'name': 'Marhta', 'age': 24}
]

print(people)