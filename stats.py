def get_num_words(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def character_count(contents):
    contents = contents.lower()
    my_dict = dict()
    for letter in contents:
        c = 0
        if letter in my_dict:
            #letter already counted
            c = 0
        else:
            for let in contents:
                if letter == let:
                    c += 1
            my_dict[letter] = c
    return my_dict

def dict_to_list_of_dicts(input_dict):
    list_of_dicts = []
    for key, value in input_dict.items():
        list_of_dicts.append({key: value})
    return list_of_dicts

def sort_list_of_dictionaries(list_of_dictionaries):
    return sorted(list_of_dictionaries, key=lambda item: next(iter(item.values())), reverse=True)

def dict_sort(dict):
    
    dict_list = dict_to_list_of_dicts(dict)
    sorted_list = sort_list_of_dictionaries(dict_list)

    return sorted_list
                