""""
Exercise 1 - 

Reverse the list below in-place using an in-place algorithm.
For extra credit: Reverse the strings at the same time.


"""

words = ['this' , 'is', 'a', 'sentence', '.']


print(f"{words =} before")
sorted_list = words.reverse()
print(f"{words = } after\n{sorted_list}")

# def reverse_list(words):
#     words[0], words[1], = words[-1], words[0]
#     return words

# print(words)
