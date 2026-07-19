# Exercises - Day 9
# Exercises: Level 1
# 1
user_age = int(input("Enter your age: "))
missing_years = 18 - user_age
print("You are old enough to learn to drive.") if user_age >= 18 else print(f"You need {missing_years} more years to learn to drive.")

# 2
my_age = int(input("What's my age: "))
years_difference = abs(user_age - my_age)
if my_age < user_age:
    if years_difference == 1:
        print(f"You are {years_difference} year older than me.")
    else:
        print(f"You are {years_difference} years older than me.")
elif my_age > user_age:
    if years_difference == 1:
        print(f"You are {years_difference} year younger than me.")
    else:
        print(f"You are {years_difference} years younger than me.")
else:
    print('We are age mates! Hurray')

# 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is lesser than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2
student_score = int(input("Enter the student score: "))

if student_score >= 90 and student_score <= 100: # if 90 <= student_score <= 100
    print('A')
elif student_score >= 80 and student_score <= 89:
    print('B')
elif student_score >= 70 and student_score <= 79:
    print('C')
elif student_score >= 60 and student_score <= 69:
    print('D')
elif student_score >= 0 and student_score <= 59:
    print('F')
else:
    print('Pls input a number within 0 and 100.')

# 2
user_month = str(input("Enter your preferred month: ").capitalize())

if user_month == "September" or user_month == "October" or user_month == "November": # user_month in ('September' or 'October' or 'November)
    print('Autumn')
elif user_month == "December" or user_month == "January" or user_month == "February":
    print('Winter')
elif user_month == "March" or user_month == "April" or user_month == "May":
    print("Spring")
elif user_month == "June" or user_month == "July" or user_month == "August":
    print("Summer")

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("What is your favorite fruit? ").lower()
if user_fruit not in fruits:
    fruits.append(user_fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')

# Exercises: Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['React', 'Node', 'MongoDB', 'Javascript', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    middle_skill = len(person['skills']) // 2
    print(person['skills'][middle_skill])
    if 'Python' in person['skills']:
        print(f"{person.get('first_name')} has Python skills")


user_skills = set(person['skills'])

if user_skills == {'Javascript', 'React'}:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(user_skills):
    print('He is a back end developer')
elif {'Node', 'React', 'MongoDB'}.issubset(user_skills):
    print('He is a full stack developer')
else:
    print('unknown title')

if person['is_married'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")