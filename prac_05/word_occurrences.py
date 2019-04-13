text_count = dict()
text = input("Text:")
text = text.split(" ")
for text in text:
    if text in text_count:
        text_count[text] += 1
    else:
        text_count[text] = 1
for key, value in sorted(text_count.items()):
    print(key, ":", value)
