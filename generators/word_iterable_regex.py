import re
class WordIterable:
    def __init__(self, text):
        self.text = re.findall(r'[a-z]+', text, re.I)

    def __iter__(self):
        self.new_word = 0
        return self

    def __next__(self):
        if self.new_word >= len(self.text):
            raise StopIteration
        result = self.text[self.new_word]
        self.new_word += 1
        return result


a = 'lol= top rop. rip*111'
for i in WordIterable(a):
    print(i)
