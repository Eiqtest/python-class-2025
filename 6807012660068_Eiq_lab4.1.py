_Mylist = []

def add_to_list(item):
    "Add an item to the list."
    _Mylist.append(item)
    print(f"Added {item} to the list.")

while True:
    item = input("Enter an item (type 'end' to finish): ")
    if item == "end" or item == "END" or  item == "End":
        print("End of input.")
        break
    add_to_list(item)

print("Your list:", _Mylist)

