import re

# Exercises: Day 18
# Exercises: Level 1
# 1

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

frequency_counter = {}
for word in re.split(' ', paragraph.replace('.', '')):
    frequency_counter[word] = frequency_counter.get(word, 0) + 1

frequency_list = [(count, word) for word, count in frequency_counter.items()]
frequency_list.sort(key=lambda x: x[0], reverse=True)

print(frequency_list)
print(f"The most frequent word is {frequency_list[0][1]} with a frequency of {frequency_list[0][0]}")

# 2
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
distance = int(points[-1]) - int(points[0])
print(distance)

# Exercises: Level 2
# 1
def is_valid_variable(text):
    return bool(re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', text))

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

# Exercises: Level 3
# 1
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

reg_pattern = r'[^A-Za-z0-9 ]'
def clean_text(sentence):
    return re.sub(reg_pattern, '', sentence)

cleaned_text = clean_text(sentence)
# print(clean_text(sentence))
print(cleaned_text)

def most_frequent_words(cleaned_text):
    frequency_count = {}
    for word in re.split(' ', cleaned_text):
        frequency_count[word] = frequency_count.get(word, 0) + 1

    sorted_most_frequent = sorted([(count, word) for word, count in frequency_count.items()], key=lambda x:x[0], reverse=True)[:3]
    return sorted_most_frequent

print(most_frequent_words(cleaned_text))