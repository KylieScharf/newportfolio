import json

p1 = { "name":"John", "age":61, "city":"Eugene"}
p2 = { "name":"Risa", "age":16, "city":"New York"}
p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]



# turn list to dictionary of people
dict_person = { "name":"Joe", "age":61, "city":"San Diego"}
dict_person1 = {"name":"John", "age":61, "city":"Eugene"}
dict_person2 = {"name":"Risa", "age":16, "city":"New York"}
dict_people3 = {"name":"Ryan", "age":16, "city":"Los Angeles"}
dict_people = {"name":"Shekar", "age":16, "city":"San Francisco"}
print("List to Dictionary of people")
print(type(dict_people))

print(dict_people)
print(dict_person1['name'])
print(dict_person1.get['name'])
print("Keys: ")
for key in dict_person1:
    print(key)

print("Function Keys(): ")
for key in dict_person2.keys():
    print(key)

print("Values: ")
for value in dict_person:
    print(dict_person[value])

print("Function Values(): ")
for value in dict_person.values():
    print(value)

print("Function Items(tuple): ")
for pair in dict_person.items():
    print(pair)

('JSON String**')
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)



print("** Loads - JSON to Python Dict**")
json_dict = json.loads(json_people)
print(json_dict)
# to list
names = [person['name'] for person in json_dict]
print("Names of people to list: p1, p2, p3, p4" + str(names))
print("Names of people: John, Risa, Ryan, Shekar")
# pretty print Names of People