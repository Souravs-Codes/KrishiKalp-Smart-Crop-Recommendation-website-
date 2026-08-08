import json
import joblib


# Load all crop classes from model
mlb = joblib.load("models/multilabel_binarizer.pkl")

crops = mlb.classes_


crop_database = {}


for crop in crops:

    crop_database[crop] = {

        "description": f"{crop} is an agricultural crop recommended based on soil and climatic conditions.",

        "soil": "Suitable soil conditions vary depending on region.",

        "season": "Depends on cultivation region.",

        "water": "Moderate water requirement.",

        "harvest": "Varies according to crop variety."

    }


with open(
    "data/crops.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        crop_database,
        f,
        indent=4,
        ensure_ascii=False
    )


print(
    "Created database for",
    len(crops),
    "crops"
)