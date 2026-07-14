# Exercises - Day 4
# 1
words_one = ['Thirty', 'Days', 'Of', 'Python']
statement_one = ' '.join(words_one)
print(statement_one)

# 2
words_two = ['Coding', 'For', 'All']
statement_two = ' '.join(words_two)
print(statement_two)

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.title())
print(company.capitalize())
print(company.swapcase())


# 9
print(company[0:6])

# 10
print(company.find('Coding'))

# 11
print(company.replace('Coding', 'Python'))

# 12
company_new = "Python For Everyone"
print(company_new.replace('Everyone', 'All'))

# 13
print(company.split(' '))

# 14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# 15
print(company[0])

# 16
last_letter = len(company) - 1
print(company[last_letter]) # print(company[-1])

# 17
print(company[10])

# 18
print(company_new[0] + company_new[7] + company_new[11])

# 19
print(company[0] + company[7] + company[11])

# 20
first_occurence_of_c = company.index('C')
print(first_occurence_of_c)

# 21
first_occurence_of_f = company.index('F')
print(first_occurence_of_f)

# 22
new_word = "Coding For All People"
print(new_word.rfind('l'))

# 23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))

# 24
print(sentence.rindex('because'))

# 25
start = sentence.find('because')
end = sentence.rfind('because') + len('because')
print(sentence[start:end])

# 26
print(sentence.index('because'))

# 27
start = sentence.find('because')
end = sentence.rfind('because') + len('because')
print(sentence[start:end])

# 28
print(company.startswith('Coding'))

# 29
print(company.endswith('coding'))

# 30
str = '   Coding For All      '
print(str.strip())

# 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32
new_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(new_list))

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# 35
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')

# 36
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')