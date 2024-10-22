import json

people_string = '''
{
    "people": [
        {
            "name": "Sheldon Cooper",
            "phone": "98712345",
            "emails": ["shelly1@gmail.com", "shelly2@gmail.com"],
            "has_lisense": false
        },
        {
            "name": "Tim Cooper",
            "phone": "987121115",
            "emails": ["timmy1@gmail.com", "timm4@gmail.com"],
            "has_lisense": true
        }
    ]
}
'''

data = json.loads(people_string)  # json string to python object, loads means load string

# for person in data['people']:
#     print(person['emails'])


##Task - remove the phone number and make the python obeject to json object


for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True) # indent function
print(new_string)


