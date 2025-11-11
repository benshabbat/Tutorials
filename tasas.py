import json

with open("tss.json", "r", encoding="utf-8") as file:
    tasas = json.load(file)
    
print(tasas)    