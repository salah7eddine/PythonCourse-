# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'mizo',
    'last_name': 'Abousaid',
    'age': 25
}

# Use constructor
person2 = dict(first_name='mery', last_name="Abousaid")
print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add Key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict keys
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Settat'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))
print(person)

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'kevin', 'age': 25}
]

print(people[1]['name'])

