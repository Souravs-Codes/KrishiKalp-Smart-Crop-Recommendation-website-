import json
import joblib

with open("data/crop_requirements.json") as f:
    req = json.load(f)

mlb = joblib.load("models/multilabel_binarizer.pkl")

all_crops = list(mlb.classes_)

missing = []

for crop in all_crops:
    if crop not in req:
        missing.append(crop)

print("Total model crops:", len(all_crops))
print("Covered crops:", len(req))
print("Missing crops:")
print(missing)