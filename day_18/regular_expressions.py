import re

# Exercises: Day 18
# Exercises: Level 1
# 1

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

frequency_counter = {}
for word in re.split(' ', paragraph.replace('.', '')):
    if word not in frequency_counter:
        frequency_counter[word] = 1
    else:
        frequency_counter[word] += 1

frequency_list = sorted(frequency_counter.items(), key=lambda x: x[1], reverse=True)

print(frequency_list)
print(f"The most frequent word is {frequency_list[0][0]} with a frequency of {frequency_list[0][1]}")

# 2
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
distance = int(points[-1]) - int(points[0])
print(distance)

# Exercises: Level 2
# 1


# Exercises: Level 3
# 1
# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# reg_pattern = r'[^A-Za-z0-9]'
# cleaned_sentence = re.sub('@', '', sentence, re.I)
# print(cleaned_sentence)
