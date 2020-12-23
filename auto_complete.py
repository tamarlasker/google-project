import json
from auto_complete_object import AutoCompleteData
data = {}
old_searches = {}
subs_dict = {}


def ignore_punctuation(text):
    text = text.lower()
    res = ""
    for word in text.split(" "):
        for c in word:
            if c.isalpha() or c.isdigit():
                continue
            word = word.replace(c, "")
        res += " " + word
    return res[2:]


def split_text(text):
    return list(f"{i}{j}" for i, j in zip(text[0:-1], text[1:]))


def find_best_matches(text, potential_indexes):
    matches = []
    while len(text):
        for index in potential_indexes:
            if len(matches) > 4:
                return matches
            if text in ignore_punctuation(data[index][0]):
                matches += [index]
        text = text[:-2]
    return matches


def get_indexes_of_results(text, splited_text):
    try:
        res = set.intersection(*[set(subs_dict[sub]) for sub in splited_text])
    except KeyError:
        return []
    return find_best_matches(text, res)


def get_matched_results(text, splited_text):
    results = []
    res_indexes = get_indexes_of_results(text, splited_text)#TODO sort by lexicography order, if there are more than 5 matches
    for index in res_indexes:
        a = AutoCompleteData(data[index][0], data[index][1], data[index][2])
        a.set_score(text)
        results.append(a)
    return results


def search(user_text):
    try:
        return [convert_dict_to_AutoComplete(obj) for obj in old_searches[user_text]]
    except KeyError:
        splited_user_text = split_text(user_text)
        return get_matched_results(user_text, splited_user_text)


def print_autocomplete(obj):
    print(f'{obj.m_sentence} path: {obj.m_path}, score: {obj.m_score}, offset: {obj.m_offset}')


def convert_AutoComplete_to_dict(auto_obj):
    return {'sentence': auto_obj.m_sentence,
            'path': auto_obj.m_path,
            'offset': auto_obj.m_offset,
            'score': auto_obj.m_score,
            }


def convert_dict_to_AutoComplete(dict_):
    return AutoCompleteData(dict_['sentence'], dict_['path'], dict_['offset'], dict_['score'])


def load_data():
    with open("old_searches.json") as file:
        global old_searches
        old_searches = json.load(file)

    with open("substring_dict.json") as file:
        global subs_dict
        subs_dict = json.load(file)

    with open("text_data.json") as file:
        global data
        data = json.load(file)


def auto_complete():
    load_data()
    while True:
        input_ = " "
        print("Welcome to google search!\nwhat do you want to look for? ")
        while True:
            input_ += input()
            if input_[-1] == '#':
                break
            input_ = ignore_punctuation(input_)
            if len(input_) == 1:
                input_ = " " + input_
            five_best_matches = search(input_)
            if five_best_matches == []:
                print("No matched results")
            else:
                for i, obj in enumerate(five_best_matches, 1):
                    print(f"----------------------------\n{i}) ")
                    print_autocomplete(obj)
            old_searches[input_] = [convert_AutoComplete_to_dict(obj) for obj in five_best_matches]

        with open("old_searches.json", 'w') as outfile:
            json.dump(old_searches, outfile)


if __name__ == '__main__':
    auto_complete()

    {
        int
    left = 0;
    int
    right = size - 1;
    int
    min_index = 0;
    int
    max_index = size - 1;

    while (left < max_index | | right > min_index)
        {
        if (prices[left] < prices[min_index])
        {
            min_index = left;
        }

        if (prices[right] > prices[max_index])
        {
        max_index = right;
        }

        if (left < max_index)
        {
        ++left;
        }

        if (right > min_index)
        {
        --right;
        }
        }
        printf("The max profit: %d\n", prices[max_index] - prices[min_index]);
    }

    int
    main()
    {
    int
    arr[] = {5, 2, 13, 1, 999, 7, 1008, 25};
    getMaxInvestment(arr, 8);
    return 1;
}


