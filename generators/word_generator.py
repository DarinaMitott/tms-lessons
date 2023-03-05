def generate_words(text):
    text = [word for word in text.split()]
    for word in text:
        yield word


a = 'pop iop kek'
for x in generate_words(a):
    print(x)
