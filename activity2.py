import json
import pprint
import json
import pprint

if __name__ == "__main__":
    p1 = { "name":"John", "age":61, "city":"Eugene"}
    p2 = { "name":"Risa", "age":16, "city":"New York"}
    p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
    p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
    list_of_people = [p1, p2, p3, p4]
    json_people=json.dumps(list_of_people)
    json_dict=json.loads(json_people)
    for person in json_dict:
        names=person['name']
        print(names)

