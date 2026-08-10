# Exercises: Day 12
# Exercises: Level 1
import string, random

# 1
def random_user_id():
    char_pool = string.ascii_letters + string.digits
    final_user_id = ""

    for _ in range(6):
        random_char = random.choice(char_pool)
        final_user_id += random_char
    return final_user_id

print(random_user_id())

# 2
def user_id_gen_by_user():
    num_of_characters = int(input("What's the number of characters per id? "))
    number_of_id_generated = int(input("What's the number of id to be generated? "))
    character_pool = string.ascii_letters + string.digits
    final_user_id = []

    for _ in range(number_of_id_generated):
        current_id = ""
        for _ in range(num_of_characters):
            random_char = random.choice(character_pool)
            current_id += random_char
        final_user_id.append(current_id)
    return "\n".join(final_user_id)

print(user_id_gen_by_user())

# 3
def rgb_color_gen():
    r, g, b = random.choices(range(0,255), k=3)
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())

# Exercises: Level 2
# 1
def list_of_hexa_colors(n_hexa):
    char_pool = string.digits + string.ascii_lowercase[:6]
    hexa_lst = []

    for _ in range(n_hexa):
        current_hexa_color = ""
        hexa_color = random.choices(char_pool, k=6)
        for hexa_char in hexa_color:
            current_hexa_color += hexa_char
        hexa_lst.append(f"#{current_hexa_color}")

    return hexa_lst

print(list_of_hexa_colors(2))


# 2
def list_of_rgb_colors(n_rgb):
    rgb_lst = []
    for _ in range(n_rgb):
        r, g, b = random.choices(range(0,256), k=3) # 256 cause random.choices stops at the 255 (number before the last number in that range)
        rgb_lst.append(f"rgb({r}, {g}, {b})")
    return rgb_lst

print(list_of_rgb_colors(2))

# 3
def generate_colors(color, num):
    if 'hexa' in color:
        return list_of_hexa_colors(num)
    elif 'rgb' in color:
        return list_of_rgb_colors(num)
    else:
        return "Incorrect parameter"

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

# Exercises: Level 3
# 1
def shuffle_list(lst):
    shuffled_list = lst.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

print(shuffle_list(['apple', 'mango', 'berry', 'orange', 'grape']))

# 2
def seven_random_numbers():
    array = set()
    array_of_nums = []

    while len(array) < 7:
        array.add(random.randint(0,9))

    for num in array:
        array_of_nums.append(num)

    return array_of_nums
    # OR return random.sample(range(10), 7)

print(seven_random_numbers())