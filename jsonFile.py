import json
a = 1
while a > 0:

    mylist = {
        "people": [
            {
                "name": input('name: '),
                "age": int(input('age: ')),
                "weight": int(input('weight: '))
            }
            
        ]
    }
    data_string = json.dumps(mylist, indent=4)
    with open('general\mylist.json', 'a') as f:
        f.write(data_string)