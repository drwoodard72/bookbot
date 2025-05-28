def get_num_words(text):
    return f"{len(text.split())} words found in the document"

def get_num_characters(text):
    chars = {}
    for c in text:
        if c.lower() in chars:
            chars[c.lower()] += 1
        else:
            chars[c.lower()] = 1

    return chars
