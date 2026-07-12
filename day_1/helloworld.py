# Exercise: level 2
# 2
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

# 3
print('Prosper')
print('Barnabas')
print('Nigeria')
print('I am enjoying 30 days of python')

# 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'python', 'Finland']))
print(type('Prosper'))
print(type('Barnabas'))
print(type('Nigeria'))

# Exercise: level 3
# 1
print(type(10)) # Integer
print(type(9.8)) # float
print(type(4 - 4j)) # complex
print(type(['Asabeneh', 'python', 'Finland'])) # list
print(type('Prosper')) # string
print(type(('earth', 'space'))) # tuple
print(type({2, 3, 5, 6})) # set

print(type({
'firstName':'Prosper',
'lastName':'Barnabas',
})) # dictionary

# 2 - Euclidean distance between the points (2, 3) and (10, 8)
p1 = 2
p2 = 10
q1 = 3
q2 = 8

d = ((p1 - q1)* (p1 - q1) + (p2 - q2)*(p2 - q2))**0.5
print(d)