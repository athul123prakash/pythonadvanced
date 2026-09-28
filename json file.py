from os import write

[{"name": "Arun", "age": 23}, {"name": "Amal", "age": 24}]
import json
f=open('data.json','r')
content=json.load(f)
print(content)
f.close()

#write

import json
content=[]