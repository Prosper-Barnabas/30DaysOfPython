# Exercises - Day 6
# Exercise : Level 1

# 1
tpl = ()

# 2
brothers = ('Jake', 'John', 'Jayden')
sisters = ('Alice', 'Mona')

# 3
siblings = brothers + sisters
print(siblings)

# 4
print(len(siblings))

# 5
family_members = list(siblings)
family_members.insert(0, 'Bari')
family_members.insert(1, 'Elsa')

print(family_members)

# Exercise : Level 2
# 1
first, second, *siblings_lst = family_members
parents = [first, second]
print(parents)
print(siblings_lst)

# 2
fruits = ('banana', 'orange', 'apple', 'watermelon')
vegetables = ('okra', 'spinach', 'waterleaf')
animal_products = ('milk', 'hides')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3
food_stuff_lt = list(food_stuff_tp)

# 4
length = len(food_stuff_lt)
mid = length // 2

if length % 2 == 0:
    print(food_stuff_lt[mid-1:mid+1])
else:
    print(food_stuff_lt[mid:mid+1])


# 5
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6
del food_stuff_tp

# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)