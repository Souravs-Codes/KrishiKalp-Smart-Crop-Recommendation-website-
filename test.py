import json

with open("data/crops.json", encoding="utf-8") as f:
    crops = json.load(f)

print(crops["Arhar/Tur"]["harvest"])