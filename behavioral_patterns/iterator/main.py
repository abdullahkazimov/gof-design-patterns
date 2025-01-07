from iterator import WordCollection

word_collection = WordCollection(["a", "b", "c"])

for word in word_collection:
    print(word)

print()

for word in word_collection.get_reverse_iterator():
    print(word)