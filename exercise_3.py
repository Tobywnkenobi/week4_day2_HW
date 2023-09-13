# Exercise #3

# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.
# Hint: Linear Searching will require searching a list for a given number.
"""
linear search alogorithm
arr (list):
l = element to search for
return: index of the element in the list if found, otherwise -1
"""

def linear_search(arr, n):
    for x in range(len(arr)):               #It will have to be O(n).  It has to go through the entire list until it finds it.  The bigger
        if arr[x] == n:                     #the list, the longer it takes.
            return x
    return -1

arr_list = [10,25,36,70,88,95,6324,2158,5874]
srch_for = 88
ans = linear_search(arr_list, srch_for)
print(ans)