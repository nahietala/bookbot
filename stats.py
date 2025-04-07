def word_count(filepath):
    total = 0
    with open(filepath) as f:
        file_to_string = f.read()
        list_of_strings = file_to_string.split()
        for i in list_of_strings:
            total += 1
    return total

def characters(filepath):
    char_dict = {}
    with open(filepath) as f:
        file_to_string = f.read()
        string_lower = file_to_string.lower()
        for character in string_lower:
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1
    return char_dict

def sort_chars(char_dict):
    sorted_chars = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        sorted_chars.append(char_info)
    
    def sort_on(dict):
        return dict["count"]
    
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars

    