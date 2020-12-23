import glob
import json
from string import ascii_lowercase
from collections import defaultdict

text_data = [] #list of touples
substring_dict = defaultdict(list) #dict for substrings as keys, and indexes of lines as values.


def insert_text_data_to_file():
    json_object = json.dumps(text_data, indent=4)
    with open("text_data.json", 'w') as outfile:
        outfile.write(json_object)


def insert_substring_dict_to_file():
    json_object = json.dumps(substring_dict, indent=4)
    with open("substring_dict.json", 'w') as outfile:
        outfile.write(json_object)


def add_to_substring_dict(line):
    index = len(text_data)-1
    for letter1 in list(ascii_lowercase)+[" "]:
        for letter2 in list(ascii_lowercase)+[" "]:
            if f"{letter1}{letter2}" in line:
                substring_dict[f"{letter1}{letter2}"].append(index)


def init_data():
    files = glob.glob("C:/Users/RENT/Desktop/בוטקמפ/GOOGLE/**/*.txt", recursive=True)

    for f in files:
        with open(f, "r", encoding="utf8") as file:
            for offset, line in enumerate(file, 1):
                if line == "\n":
                    continue
                text_data.append((line, f, offset))
                add_to_substring_dict(line)


def init():
    init_data()
    insert_substring_dict_to_file()
    insert_text_data_to_file()


if __name__ == '__main__':
    init()



