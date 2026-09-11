# Exercises: Day 19
import json
import sys

sys.path.append("../data")
# Exercises: Level 1
# 1
def read_file(filename):
    words = 0
    with open(filename, 'r') as f:
        lines = f.readlines()

        words = sum(len(line.split()) for line in lines)
        return f"The file contains {words} words and {len(lines)} lines"

print(read_file('../data/obama_speech.txt'))
print(read_file('../data/michelle_obama_speech.txt'))
print(read_file('../data/donald_speech.txt'))
print(read_file('../data/melina_trump_speech.txt'))

# 2