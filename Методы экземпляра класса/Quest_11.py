class TextHandler:
    def __init__(self):
        self.lst = []
        self.min_len = float('inf')
        self.max_len = 0

    def add_words(self, text):
        words = text.split()
        self.lst.extend(words)
        self.min_len = min(self.min_len, *[len(word) for word in words])
        self.max_len = max(self.max_len, *[len(word) for word in words])

    def get_shortest_words(self):
        return [word for word in self.lst if len(word) == self.min_len]

    def get_longest_words(self):
        return [word for word in self.lst if len(word) == self.max_len]

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())