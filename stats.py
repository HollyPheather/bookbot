def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    chars_dict = {}
    for char in text:
        char = char.lower()
        chars_dict[char] = chars_dict.get(char, 0) + 1
    
    return chars_dict


def sort_on(items):
    return items["num"]

# Takes a dictionary, returns a sorted list of dictionarys
# comprised of {"char": "b", "num": 4868}
def sort_char_dict(char_dict):
    characters = [{"char": char, "num": char_dict[char]} for char in char_dict]
    characters.sort(reverse=True, key=sort_on)
    
    return characters