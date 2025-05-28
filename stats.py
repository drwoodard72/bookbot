def get_word_count(text):
    return len(text.split())

def get_num_words(text):
    return f"{get_word_count(text)} words found in the document"


def get_num_characters(text):
    chars = {}
    for c in text:
        if c.lower() in chars:
            chars[c.lower()] += 1
        else:
            chars[c.lower()] = 1

    return chars

def sort_func(dict):
    return dict["num"]

def get_sorted_char_counts(chars):
    results = []

    for char in chars:
        results.append({"char":char,"num":chars[char]})
    
    results.sort(key=sort_func, reverse=True)
    return results
