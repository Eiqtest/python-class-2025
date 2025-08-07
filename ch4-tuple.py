# Tuple
_tuple = () # Empty tuple
_tuple = (1, 2, 3) # Tuple with three elements
_tuple1 = ("Supachai", "weaekeaw", 34) # Tuple with mixed data types

# accessing tuple elements
# print("First item:", _tuple1[0])  # Accessing the first element
# print("Second item:", _tuple1[1])  # Accessing the second element

# print("length of tuple:", len(_tuple1))  # Length of the tuple

# slicing tuple
print("Sliced tuple (first two elements):", _tuple1[2])  # Slicing the tuple to get elements from index 1 to 2

# Adding items to a tuple
# Tuples are immutable, so we cannot add items directly.
# However, we can concatenate tuples to create a new one. 
_tuple1 = list(_tuple1)  # Convert tuple to list ALL THIS CAN USE TO CHANGE OR ADD
_tuple1.append(20)  # Add a new item to the list
_tuple1.insert(1, "NewItem")  # Insert a new item at index 1
_tuple1[0] = "UpdatedItem"  # Update the first item

_tuple1 = tuple(_tuple1)  # Convert the list back to a tuple
print("Tuple after adding items:", _tuple1)