# # set
# # empty set
# empty_set = {}

# # int 
# my_set1 = {  1, 2, 3, 4, 5 }
# #string
# my_set2 = { "apple", "banana", "cherry" }
# # mix type
# my_set3 = {"apple", 1, 2.5, True, (1,2,(tuple)),(1,2,3)}

# print("Empty set:", empty_set)
# #list and tuple 
# #Can remove and change value 
# my_set3_1 = {1, 2, 3, "AAA"}
# my_set3_1 = list(my_set3_1)  # Convert set to list
# my_set3_1[3] = "BBB" 
# my_set3_1 = set(my_set3_1)
# print("Set after changing value:", my_set3_1)

# _list = [1,  1 , 2, 3, 4, 4, 5]
# _list = (list(set(_list)))  # Convert list to set to remove duplicates, then back to list
# print("List after removing duplicates:", _list)

# for item in my_set1:
#     print("Item in my_set1:", item)

# # add element to set
# my_set3.add("CCC")
# print (my_set3)

# # remove element from set
# my_set3.remove("CCC")  # Remove an element
# print( my_set3)

# # check if element in set
# if "apple" in my_set2:
#     print("Apple is in my_set2")    
# else:
#     print("Apple is not in my_set2")

# # clear set
# my_set2.clear()  # Clear all elements from the set
# print("my_set2 after clearing:", my_set2)
# # set operations
# # union
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# set_union = set_a.union(set_b)  # Union of two sets
# set_union = set_a | set_b  # Alternative syntax for union
# print("Union of set_a and set_b:", set_union)
# # intersection
# set_intersection = set_a.intersection(set_b)  # Intersection of two sets
# set_intersection = set_a & set_b  # Alternative syntax for intersection
# print("Intersection of set_a and set_b:", set_intersection)
# # difference
# set_difference = set_a.difference(set_b)  # Difference of two sets
# set_difference = set_a - set_b  # Alternative syntax for difference
# print("Difference of set_a from set_b:", set_difference)
# # symmetric difference
# set_symmetric_difference = set_a.symmetric_difference(set_b)  # Symmetric difference of two sets it is opposite of intersection
# set_symmetric_difference = set_a ^ set_b  # Alternative syntax for symmetric difference
# print("Symmetric difference of set_a and set_b:", set_symmetric_difference)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
# A
if "apple" in fruits:
    print("Apple is fruit ")
else:
    print("Apple isn't fruit")
# B
fruits.add("orange")
print(fruits)
# C
more_fruits.append("more fruits")
print (more_fruits)
# D
fruits.remove("banana") 
print(fruits)

