# Exercises - Day 5
# Exercise : Level 1
# 1
lst = []

# 2
cars = ['saab', 'sedan', 'toyota', 'hyundrai', 'honda', 'lexus']

# 3
print(len(cars))

# 4
print(cars[0])
middle_index = len(cars) // 2
print(cars[middle_index - 1])
print(cars[-1])

# 5
mixed_data_types = ['Prosper', 250, 1.16, False, 'Nigeria']

# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[0])
middle_company = len(it_companies) // 2
print(it_companies[middle_company])
print(it_companies[-1])

# 10
it_companies[0] = 'Meta'
print(it_companies)

# 11
it_companies.append('Netflix')

# 12
it_companies.insert(3, 'Nvidia')

# 13
it_companies[1] = it_companies[1].upper()

# 14
print('#; '.join(it_companies))

# 15
does_ibm_exist = 'IBM' in it_companies
print(does_ibm_exist)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.reverse()
print(it_companies)

# 18
print(it_companies[0:3])

# 19
print(it_companies[-3:])

# 20
middle_it_company = len(it_companies) // 2
print(it_companies[middle_it_company - 1])

# 21
it_companies.remove(it_companies[0])
print(it_companies)

# 22
it_companies.pop(middle_it_company -1)
print(it_companies)

# 23
it_companies.pop()
print(it_companies)

# 24
it_companies.clear()
print(it_companies)

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

# 27
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


# Exercise: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[len(ages) - 1]
print(f'The min age is {min_age} and the max age is {max_age}')
ages.append(19)
ages.append(26)
ages.sort()

median_age = len(ages) // 2
print(ages[median_age])

average_age = sum(ages) / len(ages)
print(average_age)

range_age = max_age - min_age
print(range_age)

min = abs(min_age - average_age)
max = abs(max_age - average_age)
print(min > max)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

middle_country = (len(countries) + 1) // 2
print(countries[middle_country - 1])

first_half = countries[:middle_country]
second_half = countries[middle_country:]
print(first_half)
print(second_half)

list_of_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *rest = list_of_countries
print(first_country)
print(second_country)
print(third_country)
print(rest)

min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

