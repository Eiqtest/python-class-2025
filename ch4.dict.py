# Define simple 
person = {
    "Name": "Eiq",
    "Age": 18
}
print(person)
print("Name:", person["Name"])
print("Age:", person["Age"])

for key, value in person.items():
    print(key, ":", value)

person["job"] = "data science"
print(person)

person["age"] = 20
person["city"] = "New York"
print (person)

del person["job"]
if "name" in person:
    print("name exist in list") 

dict1 = {"a":1, "b":2, "c":3}
dict2 = {"d":4, "e":5}

#m merging two dict
dict1.update(dict2)
print(dict1)

#nested dict
student = {
    "person1":{
    "name": "alice",
    "age": 25
    },
    "person2":{
    "name" : "John",
    "age" : 28
    },
    "person3":{
    "name" : "David",
    "age" : 21
    }
}
for person in student.values():
    print("name:", person["name"], "age:",person["age"])
