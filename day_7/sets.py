# Exercises - Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise : Level 1
# 1
print(len(it_companies))

# 2
it_companies.add('Twitter')
print(it_companies)

# 3
it_companies.update(['Uber', 'Paga'])
print(it_companies)

# 4
it_companies.remove('Uber')
print(it_companies)

# 5
# it_companies.remove('Flutterwave') - remove flags an error if the item is not in the set.
# it_companies.discard('Flutterwave') - discard won't flag an erro if the item is not in the set.

# Exercises: Level 2
# 1
print(A.union(B))

# 2
print(A.intersection(B))

# 3
print(A.issubset(B))

# 4
print(A.isdisjoint(B))

# 5
print(A.union(B))
print(B.union(A))

# 6
print(A.symmetric_difference(B))

# 7
del A
del B

# Exercises: Level 3
# 1
age_st = set(age)
print(age_st)
print(len(age) > len(age_st)) # the list is bigger cause sets doesn't allow for duplicates

# 2
# string is a data type used to hold text. it is usually enclosed in '' or ""
# list is a collection data type that can be modified and ordered. it allows for duplicates and it is in this form ['item1', 'item2']
# tuple is a collection data type that is ordered and cannot be modified. it allows for duplicates and in this form ('item1', 'item2')
# set is a collection data type that is unordered and cannot be modified but can accept new items. doesn't allows for duplicates and it is in this form {'item1', 'item2'}

# 3
sentence = 'I am a teacher and I love to inspire and teach people.'
words_lst = sentence.split(' ')
words_st = set(words_lst)
print(len(words_st))