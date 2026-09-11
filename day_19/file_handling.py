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
        return f"File contains {words} words and {len(lines)} lines"

print(read_file('../data/obama_speech.txt'))
print(read_file('../data/michelle_obama_speech.txt'))
print(read_file('../data/donald_speech.txt'))
print(read_file('../data/melina_trump_speech.txt'))

# 2
def most_spoken_languages(filename, limit=10):
    with open(filename, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)
        language_dict = {}

        for country in countries_data:
            for language in country.get('languages', []):
                language_dict[language] = language_dict.get(language, 0) + 1

        sorted_languages = sorted([(count, name) for name, count in language_dict.items()], reverse=True)[:limit]
        return sorted_languages

print(most_spoken_languages(filename='../data/countries_data.json', limit=3))