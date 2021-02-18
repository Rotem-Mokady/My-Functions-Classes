import json
f = open("example.txt", 'r').readline()
print(json.loads(f))