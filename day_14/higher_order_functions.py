# Exercises: Day 14
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1
# 1
"""
All three are built-in functions in python.
map is a way to manipulate a given iterable using a function for it. map(function, iterable). returns an iterable
filter returns values based on which passed a certain criteria defined in the function. filter(function, iterable). returns an iterable
reduce function is a way to manipulate data to produce a result not an iterable. reduce(function, iterable). requires from functools import reduce.
"""

# 2

# 3
# map
cubed_numbers = map(lambda x: x ** 3, numbers)
print(list(cubed_numbers))

# filter
odd_numbers = filter(lambda x: x%2 != 0, numbers)
print(list(odd_numbers))
# how to go about filtering for prime numbers logical step only.

# reduce
def sum_nums(x, y):
    return x + y

sum_of_nums = reduce(sum_nums, numbers)
print(sum_of_nums)

# 4
for country in countries:
    print(country)

# 5
for name in names:
    print(name)

# 6
for number in numbers:
    print(number)

# Exercises: Level 2
# 1
uppercase_countries = map(lambda x: x.upper(), countries)
print(list(uppercase_countries))

# 2
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))

# 3
uppercase_names = map(lambda x: x.upper(), names)
print(list(uppercase_names))

# 4
contains_land = filter(lambda x: 'land' in x, countries)
print(list(contains_land))

# 5
six_character_countries = filter(lambda x: len(x) == 6, countries)
print(list(six_character_countries))

# 6
six_character_or_more_countries = filter(lambda x: len(x) >= 6, countries)
print(list(six_character_or_more_countries))

# 7
countries_starting_with_E = filter(lambda x: x.startswith('E'), countries)
print(list(countries_starting_with_E))

# 8


# 9
lst = ['numbers', 1, 4, 5, 'joure']
get_string_lists = filter(lambda x: type(x) == str, lst)
print(list(get_string_lists))

# 10
sum_of_all_nums = reduce(lambda x, y: x + y, numbers)
print(sum_of_all_nums)

# 11
north_european_countries = reduce(lambda x, y: f"{x}, {y}", countries)
print(north_european_countries + " are north European countries")

# 12
from countries import COUNTRIES
# countries that contains 'land'
countries_that_contains_land = filter(lambda x: 'land' in x, COUNTRIES)
print(list(countries_that_contains_land))
# countries that contains 'ia'
countries_that_contains_ia = filter(lambda x: 'ia' in x, COUNTRIES)
print(list(countries_that_contains_ia))
# countries that contains 'island'
countries_that_contains_island = filter(lambda x: 'Island' in x, COUNTRIES)
print(list(countries_that_contains_island))
# countries that contains 'stan'
countries_that_contains_stan = filter(lambda x: 'stan' in x, COUNTRIES)
print(list(countries_that_contains_stan))

# 13
def letters_of_countries(countries):
    letter_dict = {}
    for country in countries:
        if country[0] not in letter_dict:
            letter_dict[country[0]] = 1
        else:
            letter_dict[country[0]] += 1
    return letter_dict

print(letters_of_countries(COUNTRIES))

# 14
def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(COUNTRIES))

# 15
def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(COUNTRIES))

# Exercises: Level 3
# 1
from countries_data import COUNTRIES_DATA

def countries_by_name(countries):
    countries_by_name_lst = []
    for country in countries:
        countries_by_name_lst.append(country["name"])

    return countries_by_name_lst

print(countries_by_name(COUNTRIES_DATA))

def countries_by_capital(countries):
    countries_by_capital_lst = []
    for country in countries:
        countries_by_capital_lst.append(country["capital"])

    return countries_by_capital_lst

print(countries_by_capital(COUNTRIES_DATA))

def countries_by_population(countries):
    countries_by_population_lst = []
    for country in countries:
        countries_by_population_lst.append(country["population"])

    return countries_by_population_lst

print(countries_by_population(COUNTRIES_DATA))

# 2

# 3
def most_populated_countries