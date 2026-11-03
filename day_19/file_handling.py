# Exercises: Day 19
import json, sys, re

sys.path.append("../data")


# Exercises: Level 1
# 1
def read_file(filename):
    words = 0
    with open(filename, "r") as f:
        lines = f.readlines()

        words = sum(len(line.split()) for line in lines)
        return f"File contains {words} words and {len(lines)} lines"


print(read_file("../data/obama_speech.txt"))
print(read_file("../data/michelle_obama_speech.txt"))
print(read_file("../data/donald_speech.txt"))
print(read_file("../data/melina_trump_speech.txt"))


# 2
def most_spoken_languages(filename, limit=10):
    with open(filename, "r", encoding="utf-8") as file:
        countries_data = json.load(file)
        language_dict = {}

        for country in countries_data:
            for language in country.get("languages", []):
                language_dict[language] = language_dict.get(language, 0) + 1

        sorted_languages = sorted(
            [(count, name) for name, count in language_dict.items()], reverse=True
        )[:limit]
        return sorted_languages


print(most_spoken_languages(filename="../data/countries_data.json", limit=3))


# 3
def most_populated_countries(filename, limit=10):
    with open(filename, "r", encoding="utf-8") as file:
        countries_data = json.load(file)
        population_dict = {}

        for country in countries_data:
            name = country["name"]
            population = country["population"]
            population_dict[name] = population

        sort_population = sorted(
            population_dict.items(), key=lambda x: x[1], reverse=True
        )
        sorted_population = [
            {"country": name, "population": f"{add:,}"} for name, add in sort_population
        ][:limit]
        return sorted_population


print(most_populated_countries(filename="../data/countries_data.json"))


# Exercises: Level 2
# 1


# 2
def find_most_common_words(filepath: str, num_of_words: int) -> list[tuple]:
    words_dict = {}
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        clean_text = re.sub(r"[^A-Za-z0-9 ]", "", text).split()

    for word in clean_text:
        words_dict[word] = words_dict.get(word, 0) + 1

    return sorted([(count, word) for word, count in words_dict.items()], reverse=True)[
        :num_of_words
    ]


# 3
print(find_most_common_words("../data/obama_speech.txt", 10))
print(find_most_common_words("../data/michelle_obama_speech.txt", 10))
print(find_most_common_words("../data/donald_speech.txt", 10))
print(find_most_common_words("../data/melina_trump_speech.txt", 10))


# 4
print()


# 5
def most_repeated_words(filepath: str, limit: int):
    word_dict = {}
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        clean_text = re.sub(r"[^A-Za-z0-9 ]", "", text).split()

    for word in clean_text:
        word_dict[word] = word_dict.get(word, 0) + 1

    return sorted([(count, word) for word, count in word_dict.items()], reverse=True)[
        :limit
    ]


print(most_repeated_words("../data/romeo_and_juliet.txt", 10))

# 6
