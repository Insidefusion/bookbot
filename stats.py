def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
        
def sort_on(items):
    return items["num"]

def get_sort_chars(nums_char_dict):
    listed_dict = []
    for char in nums_char_dict:
        listed_dict.append({"char": char, "num": nums_char_dict[char]})
    listed_dict.sort(reverse=True, key=sort_on)
    return listed_dict

    
      