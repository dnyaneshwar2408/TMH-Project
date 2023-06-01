def separate_sentences(paragraph):
    sentences = []
    sentence = ""
    is_decimal = False

    for char in paragraph:
        sentence += char
        if char in [".", "!", "?"] and not is_decimal:
            sentences.append(sentence.strip())
            sentence = ""
            continue
        if char.isdigit() or (char == "." and not is_decimal):
            is_decimal = True
        else:
            is_decimal = False

    if sentence.strip():
        sentences.append(sentence.strip())

    return sentences

paragraph = "This is the first sentence. This is the second sentence. This is the third sentence. This is an example of a number: 4.5 x 6.7. "

sentences = separate_sentences(paragraph)
for sentence in sentences:
    print(sentence)
