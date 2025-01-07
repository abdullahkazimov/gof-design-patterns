class WordIterator:
    def __init__(self, words, reverse=False):
        self.words = words
        self.is_reverse = reverse
        self.position = -1 if reverse else 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.is_reverse:
            if self.position >= -len(self.words):
                val = self.words[self.position]
                self.position -= 1
                return val
            else:
                raise StopIteration
        else:
            if self.position < len(self.words):
                val = self.words[self.position]
                self.position += 1
                return val
            else:
                raise StopIteration


class WordCollection:
    def __init__(self, words):
        self.words = words

    def __iter__(self):
        return WordIterator(self.words)

    def get_reverse_iterator(self):
        return WordIterator(self.words, True)