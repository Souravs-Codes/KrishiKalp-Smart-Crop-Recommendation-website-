import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "data" / "crops.json", encoding="utf-8") as f:
    crop_database = json.load(f)

def get_crop_details(crop_name):
    return crop_database.get(
        crop_name,
        {
            "description": "Information not available.",
            "soil": "-",
            "season": "-",
            "water": "-",
            "harvest": "-"
        }
    )