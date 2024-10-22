import json

with open('states.json') as f:
    new_data1 = json.load(f)

for state in new_data1['states']:
    del state['abbreviation']


with open('new_states.json','w') as f:
    json.dump(new_data1, f, indent=2)