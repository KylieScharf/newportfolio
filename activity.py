import json
import pprint
import json
import pprint

import json
import pprint

if __name__ == "__main__":
    student_list = ['pam','rob','joe','greg','bob','amy','matt']
    print(student_list[2:5])
    print(student_list[:-5])
    print(student_list[5:])
    print(student_list[:])
    if 'rob' in student_list:
        print("we found rob")
    else:
        print("we didn't find rob")

if __name__ == "__main__":
    nlist = [10, 11, 12, 13, 14, 15]
    print([item for item in reversed(nlist)])
    for i in range(len(nlist)):
        print(nlist[i])
    if 23 in nlist:
        print("Yes, 10 is in the numbers list")
    else:
        print("no")
    dict_person = {"name":"Joe", "age":61, "city":"San Diego"}
    print(dict_person['name'])
    print(dict_person.get('name'))
    print("Keys: ")
    for key in dict_person:
        print(key)
    print("Function Keys(): ")
    for key in dict_person.keys():#same thing as above
        print(key)
    print("Values: ")#gets the values out
    for key in dict_person:
        print(dict_person[key])
    print("Function Values(): ")#also gets the values
    for value in dict_person.values():
        print(value)
    print("Function Items(tuple): ")
    for pair in dict_person.items():#gets the pairs
        print(pair)

if __name__ == "__main__":
    p1 = { "name":"John", "age":61, "city":"Eugene"}
    p2 = { "name":"Risa", "age":16, "city":"New York"}
    p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
    p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
    # a list of dictionaries
    list_of_people = [p1, p2, p3, p4]
    for item in list_of_people:
        print(item)#print each person on its own line
    print(list_of_people[:])#print each person
    dict_people = {'people': list_of_people}
    #dict_people = {}
    #i = 0
    #for person in list_of_people:
        #i += 1
        #key = "P" + str(i)
        #dict_people[key] = person

    print("List to Dictionary of people")
    print(type(dict_people))
    print(dict_people)
    print("** Dumps - Python to JSON String**")
    json_people = json.dumps(list_of_people)
    print("JSON People #1")
    print(type(json_people))
    print(json_people)
    json_print = json.dumps(list_of_people, indent=4, separators=("*", " = "))# to get it to print nicely you can add optional parameters to the json.dumps function to add an indent and to change the seperators
    print(json_print)
    print("** Loads - JSON to Python Dict**")
    python_list = json.loads(json_people)
    print(python_list)
    # to list
    print(type(python_list))
    names = []
    for person in python_list:
       names.append(person['name'])
    #names = [person['name'] for person in python_dict] this is equivalent to above
    print("Names of people to list: " + str(names))
    json_print2 = json.dumps(names, indent=4, separators=("$", "="))
    print(json_print2)

