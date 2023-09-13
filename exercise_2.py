"""
Exercise #2

Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
Should output:
{'a': 5,
'abstract': 1,
'an': 3,
'array': 2, ... etc...
"""
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def count_words(a_text):
    words = a_text.lower().split()

    count_words = {}

    for w in words:
        if w in count_words:
            count_words[w] += 1
        else:
            count_words[w] = 1
    return count_words

print(count_words(a_text))
