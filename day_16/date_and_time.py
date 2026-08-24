# Exercises: Day 16
from datetime import datetime

# 1
now = datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp())

# 2
print(now.strftime("%m/%d/%Y, %H:%M:%S"))

# 3
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# 4
new_year = datetime(2027, 1, 1)
t1 = new_year - now
print(t1)

# 5
past_date = datetime(1970, 1, 1)
t2 = now - past_date
print(t2)

# 6
# to add timestamp to my activities
def createdAt():
    return f"User created a task at :{datetime.now().strftime('%H:%M:%S')}"

print(createdAt())