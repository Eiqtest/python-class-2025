# # list
# _list = []
# _list = [1, 2, 3, 4, 5]
# _list = ["a", 20.0, 30, "b", 40] #;ist with mixed date type
# student = ['687012660068', 'Supachai', 'weaekeaw', 'eiqson9904@gmail.com', '18'] # list with student information
# # print("student:", student )
# print("student ID:", student[0]) # print student id
# print("student name:", student[1]) # print student name
# print("student surname:", student[2]) # print student surname
# print("student email:", student[3]) # print student email
# print("student age:", student[4]) # print student age
# print("length of student", len(student)) # print length of student list
# print("Student Fullname:", student[1], student[2]) # print student full name
# adding item to list
_list1 = [1, 2, 3, 4, 5]
_list1.append(10)  # Add 6 to the end of the list
# print("List after appending 10" \
_list1.insert(2, 5)  # Insert 0 at the beginning of the list First number is where to add behind, second number is the value to add
print("List after inserting 5 at index 2:", _list1)

# remove list
_list1.remove(2)  # Remove the first occurrence of 2 from the list
print("List after removing 2:", _list1)
# pop list REMOVE LAST ITEM
_list1.pop()  # Remove the last item from the list
print("List after popping the last item:", _list1)

#  editing item from the list
_list1[0] = 100  # Change the first item to 100
_list1[1] = 200  # Change the second item to 200
print("List after editing first two items:", _list1)

# MULTIPLE ITEM IN THE ;OST
_list2 = [6, 7, 8, 9,] 
_list1.extend(_list2)  # Add all items from _list2 to _list1
print("List after extending with _list2:", _list1)

# sorting list 
_list1.sort()  # Sort the list in ascending order
print("List after sorting:", _list1)
_list1.reverse()  # Reverse the order of the list
print("List after reversing:", _list1)
# copy the lit
a = 3
b = a
_list3 = _list1
print("list 1: ", _list1)
print("list 3: ", _list3)
_list3[0] = 1000  # Change the first item in _list3
print("List 1 after changing list 3:", _list1)  # This will
print('List 3 after changing first item:', _list3)  # This will show the change in _list3
# clear the list
# _list1.clear()  # Clear all items from the list
# print("List after clearing:", _list1)   

# delete the list
# del _list3 
# print("List 3 has been deleted, it no longer exists.")

# checking if item in the list
if 100 in _list1:
    print("100 is in the list.")
else:
    print("100 is not in the list.")

# iterating through the list
for item in _list1:
    print("Item in the list:", item)

for index in range(len(_list1)):
    print(f"Item at index {index}:", _list1[index])