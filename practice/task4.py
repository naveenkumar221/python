# PRACTICE PROBLEMS (Lists & Tuples)
# 1. Add all elements of a list.
list=[1,2,3,4,5,6,7,8,9,10]
print(sum(list))
# 2. Find max and min in a list.
list=[1,2,3,4,5,6,7,8,9,10]
print(max(list))
print(min(list))
# 3. Count even and odd numbers in a list.
list=[1,2,3,4,5,6,7,8,9,10]
even=sum(1 for x in list if x%2==0)
odd=len(list)-even
print(even,odd)
# 4. Reverse a list without using reverse().
list=[1,2,3,4,5,6,7,8,9,10]
print(list[::-1])
# 5. Remove duplicates from list.
li=[1,2,3,4,5,6,7,8,9,10,4,6,2,8,9,2,3,4,5]
list1=[]
for item in li:
    if item not in list1:
        list1.append(item)
print(list1)

# 6. Sort a list of strings by length.
name=["apple", "banana", "kiwi", "grape"]
name.sort(key=len)
print(name)
# 7. Find the second largest number in the list.
try:
    del list
except:
    pass
lst = [10, 20, 40, 50,12,32,30]
unique = list(set(lst))
unique.sort()
print("Second Largest:", unique[-2])

# 8. Find sum of all nested list elements.
nested = [[1, 2], [3, 4], [5]]
total = sum(sum(sublist) for sublist in nested)
print("Total Sum:", total)
# 9. Check if two lists are equal.
a = [1, 2, 3]
b = [1, 2, 3]
print("Equal:", a == b)

# 10. Merge two lists and sort them.
a = [3, 1, 4]
b = [2, 5]
merged = sorted(a + b)
print("Merged & Sorted:", merged)

# 11. Convert tuple to list and back.
t = (1, 2, 3)
lst = list(t)
t2 = tuple(lst)
print("List:", lst)
print("Tuple:", t2)

# 12. Check if the tuple contains a value.
# 13. Unpack a tuple into variables
# 14. Create a list of squares using comprehension.
# 15. Count how many times a number appears in a list.
# 16. Find index of element in tuple.
# 17. Slice a tuple from index 1 to 3.
# 18. Replace element in list with another.
# 19. Filter only strings from mixed lists.
# 20. Take input of the list from the user and print sum.

