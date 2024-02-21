import json
with open("tsis 4/json1.py/sample-data.json","r") as file:
    json_string=file.read()
    data = json.loads(json_string)

print("Interface Status" )
print("="*85)
print("DN                                                 Description           Speed    MTU")
print("-"*50 + " " + "-"*21 + " " + "-"*5 + " " + "-"*6) 

for x in data['imdata']:
    print("{}                             {}  {}".format(x['l1PhysIf']['attributes']['dn'],x['l1PhysIf']['attributes']['fecMode'],x['l1PhysIf']['attributes']['mtu'])) 
        
    

