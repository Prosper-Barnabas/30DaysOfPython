# Exercises - Day 8
# 1
dog = {}

# 2
dog['name'] = 'Bingo'
dog['color'] = 'Brown'
dog['breed'] = 'Caucassian'
dog['legs'] = 3
dog['age'] = 13

print(dog)

# 3
student = {
    'first_name':'Bob',
    'last_name':'Robin',
    'gender':'Male',
    'age':18,
    'marital_status':'single',
    'skills':['python', 'Web3', 'baking'],
    'country':'Greece',
    'city':'Athens',
    'address': {
        'street_name':'Beverly Hills, Blick Road',
        'zipcode':'10001'
    }
}
print(student)

# 4
print(len(student))

# 5
print(type(student['skills']))
print(student.get('skills'))

# 6
student['skills'].append('skating') # student['skills'].extend(['skating', 'skydiving'])
print(student['skills'])

# 7
keys = list(student.keys())
print(keys)

# 8
values = list(student.values())
print(values)

# 9
student_tp = list(student.items())
print(student_tp)

# 10
del student['address']
print(student)

# 11
del dog