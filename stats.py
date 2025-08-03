
def get_words_count(text: str) -> int:
    return len(text.split())

def get_number_of_each_char(text: str) -> dict:
    res = {}
    for c in text:
        c = c.lower()
        if not res.get(c):
            res[c] = 1
        else:
            res[c] += 1
    return res

def sort_on(items):
    return items["num"]

def get_sorted_num_of_char(text: str) -> list[dict]:
    char_dict = get_number_of_each_char(text)
    sorted_char_list = [
        {"char": key, "num": value}
        for key, value
        in char_dict.items()
    ]
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list
