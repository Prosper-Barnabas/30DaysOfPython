# Exercises: Day 14
import sys
sys.path.append("../data")

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
"""
Higher order functions are functions that can take in a function as an argument.
closure is nesting a function inside another function and then returning the inner function
Decorators are a way to use a function to add more properties to another function.
"""

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
countries_uppercase = map(lambda x: x.capitalize(), filter(lambda x: 'land' not in x, countries))
print(list(countries_uppercase))

# 9
lst = ['numbers', 1, 4, 5, 'joure']
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

print(get_string_lists(lst))

# 10
sum_of_all_nums = reduce(lambda x, y: x + y, numbers)
print(sum_of_all_nums)

# 11
north_european_countries = reduce(lambda x, y: f"{x}, and {y}" if y == countries[-1] else f"{x}, {y}", countries)
print(north_european_countries + " are north European countries")

# 12
from countries import countries

def categorize_countries(pattern, countries):
    return list(filter(lambda x: pattern in x, countries))

print(categorize_countries('land', countries))
print(categorize_countries('ia', countries))
print(categorize_countries('Island', countries))
print(categorize_countries('stan', countries))

# 13
def letters_of_countries(countries):
    letter_dict = {}
    for country in countries:
        if country[0] not in letter_dict:
            letter_dict[country[0]] = 1
        else:
            letter_dict[country[0]] += 1
    return letter_dict

print(letters_of_countries(countries))

# 14
def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(countries))

# 15
def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(countries))

# Exercises: Level 3
# 1
from countries_data import countries_data

def countries_by_name(countries):
    countries_by_name_lst = []
    for country in countries:
        countries_by_name_lst.append(country["name"])

    return countries_by_name_lst

print(countries_by_name(countries_data))

def countries_by_capital(countries):
    countries_by_capital_lst = []
    for country in countries:
        countries_by_capital_lst.append(country["capital"])

    return countries_by_capital_lst

print(countries_by_capital(countries_data))

def countries_by_population(countries):
    countries_by_population_lst = []
    for country in countries:
        countries_by_population_lst.append(country["population"])

    return countries_by_population_lst

print(countries_by_population(countries_data))

def languages_by_location(countries):
    language_dict = {}

    for country in countries:
        for language in country.get("languages", []):
            language_dict[language] = language_dict.get(language, 0) + 1

    return [{lang: n} for lang, n in sorted(language_dict.items(), key=lambda item: item[1], reverse=True)][:10]


print(languages_by_location(countries_data))

def most_populated_countries(countries):
    population_dict = {}

    for country in countries:
        if country["name"] not in population_dict:
            population_dict[country["name"]] = country["population"]

    sorted_most_populated_countries = sorted(population_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    sorted_10_most_populated_countries = [(name, f"{pop:,}") for name, pop in sorted_most_populated_countries]
    return sorted_10_most_populated_countries

print(most_populated_countries(countries_data))
