def count_words(file_contents):
    words = file_contents.split()
    return len(words)
    
def character_count(file_contents):
    file_contents = file_contents.lower()
    char_count = {}
    for char in file_contents:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on_num(item_dict):
    return item_dict["num"]

def sort_on(char_count):
    ordered_list = []
    for char, count in char_count.items():
        ordered_list.append({"char": char, "num": count})
    ordered_list.sort(key=sort_on_num, reverse=True)
    return ordered_list