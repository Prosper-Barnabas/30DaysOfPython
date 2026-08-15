# Exercises: Day 13
# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_list = [num for num in numbers if num <= 0]
print(filtered_list)

# 2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for row in list_of_lists for num in row]
print(flattened_list)

# 3
lst = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0,11)]
print(lst)

print()
# 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for row in countries for country in row ]
print(flattened_countries)

# 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country[0].upper(), 'city': country[1].upper()} for row in countries for country in row]
print(countries_dict)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_names = [f"{name[0]} {name[1]}" for row in names for name in row]
print(concat_names)

# 7
solve_slope = lambda x1, x2, y1, y2 : (y2 - y1) / (x2 - x1)
print(solve_slope(2, 4, 7, 5))

solve_y_intercept = lambda x, y, m: y - (m * x)
print(solve_y_intercept(5, 13, 2))