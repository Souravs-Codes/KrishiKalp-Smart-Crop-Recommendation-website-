import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


with open(BASE_DIR / "data" / "crops.json", encoding="utf-8") as f:
    crop_database = json.load(f)


crop_images = {

    "Apple": "apple.jpg",
    "Banana": "banana.jpg",
    "Beans & Mutter(Vegetable)": "beans.jpg",
    "Beet Root": "beetroot.jpg",
    "Bhindi": "okra.jpg",
    "Bitter Gourd": "bitter_gourd.jpg",
    "Bottle Gourd": "bottle_gourd.jpg",
    "Brinjal": "brinjal.jpg",
    "Cabbage": "cabbage.jpg",
    "Carrot": "carrot.jpg",
    "Cashewnut": "cashew.jpg",
    "Cauliflower": "cauliflower.jpg",
    "Citrus Fruit": "citrus.jpg",
    "Coconut": "coconut.jpg",
    "Coriander": "coriander.jpg",
    "Cucumber": "cucumber.jpg",
    "Drum Stick": "drumstick.jpg",
    "Dry chillies": "dry_chilli.jpg",
    "Dry ginger": "dry_ginger.jpg",
    "Garlic": "garlic.jpg",
    "Ginger": "ginger.jpg",
    "Grapes": "grapes.jpg",
    "Jack Fruit": "jackfruit.jpg",
    "Lab-Lab": "lablab.jpg",
    "Mango": "mango.jpg",
    "Onion": "onion.jpg",
    "Orange": "orange.jpg",
    "Other Citrus Fruit": "citrus.jpg",
    "Other Fresh Fruits": "fruit.jpg",
    "Other Vegetables": "vegetables.jpg",
    "Papaya": "papaya.jpg",
    "Peach": "peach.jpg",
    "Pear": "pear.jpg",
    "Pineapple": "pineapple.jpg",
    "Plums": "plum.jpg",
    "Pome Fruit": "pomefruit.jpg",
    "Pome Granet": "pomegranate.jpg",
    "Potato": "potato.jpg",
    "Pump Kin": "pumpkin.jpg",
    "Redish": "radish.jpg",
    "Snak Guard": "snake_gourd.jpg",
    "Sugarcane": "sugarcane.jpg",
    "Sweet potato": "sweet_potato.jpg",
    "Tapioca": "tapioca.jpg",
    "Tobacco": "tobacco.jpg",
    "Tomato": "tomato.jpg",
    "Turmeric": "turmeric.jpg",
    "Turnip": "turnip.jpg",
    "Water Melon": "watermelon.jpg",
    "Cowpea(Lobia)": "cowpea.jpg",
    "Gram": "gram.jpg",
    "Horse-gram": "horse_gram.jpg"

}


def get_crop_details(crop_name):

    details = crop_database.get(
        crop_name,
        {
            "description": "Information not available.",
            "soil": "-",
            "season": "-",
            "water": "-",
            "harvest": "-"
        }
    )

    # Add image information
    details["image"] = crop_images.get(
        crop_name,
        "default.jpg"
    )

    return details