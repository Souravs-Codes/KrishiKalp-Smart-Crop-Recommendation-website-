import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


with open(BASE_DIR / "data" / "crops.json", encoding="utf-8") as f:
    crop_database = json.load(f)


crop_images = {

    "Apple": "apple.jpg",
    "Arcanut (Processed)": "arecanut_processed.jpg",
    "Arecanut": "arecanut.jpg",
    "Arhar/Tur": "arhar.jpg",
    "Ash Gourd": "ash_gourd.jpg",
    "Atcanut (Raw)": "arecanut_raw.jpg",

    "Bajra": "bajra.jpg",
    "Banana": "banana.jpg",
    "Barley": "barley.jpg",
    "Bean": "bean.jpg",
    "Beans & Mutter(Vegetable)": "beans.jpg",
    "Beet Root": "beetroot.jpg",
    "Ber": "ber.jpg",
    "Bhindi": "okra.jpg",
    "Bitter Gourd": "bitter_gourd.jpg",
    "Black pepper": "black_pepper.jpg",
    "Blackgram": "blackgram.jpg",
    "Bottle Gourd": "bottle_gourd.jpg",
    "Brinjal": "brinjal.jpg",

    "Cabbage": "cabbage.jpg",
    "Cardamom": "cardamom.jpg",
    "Carrot": "carrot.jpg",
    "Cashewnut": "cashew.jpg",
    "Cashewnut Processed": "cashew_processed.jpg",
    "Cashewnut Raw": "cashew_raw.jpg",
    "Castor seed": "castor_seed.jpg",
    "Cauliflower": "cauliflower.jpg",
    "Citrus Fruit": "citrus.jpg",
    "Coconut": "coconut.jpg",
    "Coffee": "coffee.jpg",
    "Colocosia": "colocosia.jpg",
    "Cond-spcs other": "spices.jpg",
    "Coriander": "coriander.jpg",
    "Cotton(lint)": "cotton.jpg",
    "Cowpea(Lobia)": "cowpea.jpg",
    "Cucumber": "cucumber.jpg",

    "Drum Stick": "drumstick.jpg",
    "Dry chillies": "dry_chilli.jpg",
    "Dry ginger": "dry_ginger.jpg",
    "Garlic": "garlic.jpg",
    "Ginger": "ginger.jpg",
    "Gram": "gram.jpg",
    "Grapes": "grapes.jpg",
    "Groundnut": "groundnut.jpg",
    "Guar seed": "guar_seed.jpg",

    "Horse-gram": "horse_gram.jpg",
    "Jack Fruit": "jackfruit.jpg",
    "Jobster": "jobster.jpg",
    "Jowar": "jowar.jpg",
    "Jute": "jute.jpg",
    "Jute & mesta": "jute_mesta.jpg",

    "Kapas": "kapas.jpg",
    "Khesari": "khesari.jpg",
    "Korra": "korra.jpg",

    "Lab-Lab": "lablab.jpg",
    "Lemon": "lemon.jpg",
    "Lentil": "lentil.jpg",
    "Linseed": "linseed.jpg",
    "Litchi": "litchi.jpg",

    "Maize": "maize.jpg",
    "Mango": "mango.jpg",
    "Masoor": "masoor.jpg",
    "Mesta": "mesta.jpg",
    "Moong(Green Gram)": "moong.jpg",
    "Moth": "moth.jpg",

    "Niger seed": "niger_seed.jpg",

    "Oilseeds total": "oilseeds.jpg",
    "Onion": "onion.jpg",
    "Orange": "orange.jpg",
    "Other Cereals": "cereals.jpg",
    "Other Cereals & Millets": "millets.jpg",
    "Other Citrus Fruit": "citrus.jpg",
    "Other Fresh Fruits": "fruit.jpg",
    "Other Kharif pulses": "pulses.jpg",
    "Other Rabi pulses": "pulses.jpg",
    "Other Summer Pulses": "pulses.jpg",
    "Other Vegetables": "vegetables.jpg",

    "Paddy": "paddy.jpg",
    "Papaya": "papaya.jpg",
    "Peach": "peach.jpg",
    "Pear": "pear.jpg",
    "Peas  (vegetable)": "peas.jpg",
    "Peas & beans (Pulses)": "peas_beans.jpg",
    "Perilla": "perilla.jpg",
    "Pineapple": "pineapple.jpg",
    "Plums": "plum.jpg",
    "Pome Fruit": "pomefruit.jpg",
    "Pome Granet": "pomegranate.jpg",
    "Potato": "potato.jpg",
    "Pulses total": "pulses.jpg",
    "Pump Kin": "pumpkin.jpg",

    "Ragi": "ragi.jpg",
    "Rajmash Kholar": "rajmash.jpg",
    "Rapeseed &Mustard": "mustard.jpg",
    "Redish": "radish.jpg",
    "Ribed Guard": "ridge_gourd.jpg",
    "Rice": "rice.jpg",
    "Ricebean (nagadal)": "ricebean.jpg",
    "Rubber": "rubber.jpg",

    "Safflower": "safflower.jpg",
    "Samai": "samai.jpg",
    "Sannhamp": "sannhamp.jpg",
    "Sapota": "sapota.jpg",
    "Sesamum": "sesamum.jpg",
    "Small millets": "small_millets.jpg",
    "Snak Guard": "snake_gourd.jpg",
    "Soyabean": "soyabean.jpg",
    "Sugarcane": "sugarcane.jpg",
    "Sunflower": "sunflower.jpg",
    "Sweetpotato": "sweet_potato.jpg",

    "Tapioca": "tapioca.jpg",
    "Tea": "tea.jpg",
    "Tobacco": "tobacco.jpg",
    "Tomato": "tomato.jpg",
    "Total foodgrain": "foodgrain.jpg",
    "Turmeric": "turmeric.jpg",
    "Turnip": "turnip.jpg",

    "Urad": "urad.jpg",

    "Varagu": "varagu.jpg",

    "Water Melon": "watermelon.jpg",
    "Wheat": "wheat.jpg",

    "Yam": "yam.jpg",

    "other fibres": "fibres.jpg",
    "other misc. pulses": "pulses.jpg",
    "other oilseeds": "oilseeds.jpg"

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