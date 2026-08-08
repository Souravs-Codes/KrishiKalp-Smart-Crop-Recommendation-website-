import json
from pathlib import Path

# Path to your crops.json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

file_path = BASE_DIR / "crops.json"

# Load JSON
with open(file_path, "r", encoding="utf-8") as f:
    crops = json.load(f)


harvest_data = {

    "Apple": "Harvest after 150-180 days when fruits develop proper color and size.",
    "Banana": "Harvest after 9-12 months when fruits become mature and rounded.",
    "Rice": "Harvest after 100-150 days when grains become golden and dry.",
    "Paddy": "Harvest after 120-150 days when grains mature.",
    "Wheat": "Harvest after 120-150 days when grains become hard and golden.",
    "Maize": "Harvest after 80-120 days when kernels become mature.",
    
    "Groundnut": "Harvest after 90-130 days when leaves turn yellow and pods mature.",
    "Cowpea(Lobia)": "Harvest after 60-90 days when pods become mature.",
    "Gram": "Harvest after 120-150 days when pods dry completely.",
    "Blackgram": "Harvest after 70-90 days when pods turn black.",
    "Moong(Green Gram)": "Harvest after 60-90 days when pods mature.",
    "Urad": "Harvest after 70-90 days when pods become black.",
    
    "Cotton(lint)": "Harvest after 150-180 days when cotton bolls open.",
    "Sugarcane": "Harvest after 10-18 months when stalks mature.",
    "Soyabean": "Harvest after 90-120 days when leaves turn yellow.",
    "Sunflower": "Harvest after 90-120 days when flower heads turn brown.",
    "Sesamum": "Harvest after 90-120 days when capsules turn yellow.",
    
    "Tomato": "Harvest after 60-90 days when fruits become fully colored.",
    "Potato": "Harvest after 90-120 days when leaves dry.",
    "Onion": "Harvest after 100-150 days when tops fall down.",
    "Carrot": "Harvest after 70-90 days when roots reach proper size.",
    "Cabbage": "Harvest after 90-120 days when heads become firm.",
    
    "Mango": "Harvest after 100-150 days after flowering when fruits mature.",
    "Grapes": "Harvest after 120-150 days when berries reach sweetness.",
    "Papaya": "Harvest after 9-12 months when fruits show yellow color.",
    "Pineapple": "Harvest after 18-24 months when fruits mature.",
    
    "Tea": "Harvest young leaves regularly throughout the growing season.",
    "Coffee": "Harvest after 8-12 months when berries turn red.",
    "Coconut": "Harvest after 11-12 months when nuts mature.",
    
    "Ragi": "Harvest after 100-120 days when ears become brown.",
    "Bajra": "Harvest after 75-100 days when grains mature.",
    "Jowar": "Harvest after 100-120 days when grains become hard.",
    "Barley": "Harvest after 120-150 days when grains mature.",
    
    "Ginger": "Harvest after 8-10 months when leaves dry.",
    "Turmeric": "Harvest after 7-10 months when leaves turn yellow.",
    "Garlic": "Harvest after 5-6 months when leaves dry.",
    "Arhar/Tur": "Harvest after 150-180 days when pods become mature and dry.",

"Arhar": "Harvest after 150-180 days when pods become dry.",

"Rice": "Harvest after 100-150 days when grains become golden and dry.",

"Paddy": "Harvest after 120-150 days when grains mature.",

"Wheat": "Harvest after 120-150 days when grains become hard and golden.",

"Barley": "Harvest after 120-150 days when grains mature.",

"Maize": "Harvest after 80-120 days when kernels become mature.",

"Bajra": "Harvest after 75-100 days when grains mature.",

"Jowar": "Harvest after 100-120 days when grains become hard.",

"Ragi": "Harvest after 100-120 days when ears become brown.",

"Korra": "Harvest after 90-120 days when grains mature.",

"Samai": "Harvest after 90-120 days when grains mature.",

"Varagu": "Harvest after 90-120 days when grains mature.",

"Small millets": "Harvest after 70-120 days depending on variety.",

"Other Cereals": "Harvest after 90-150 days depending on crop variety.",

"Other Cereals & Millets": "Harvest after 90-120 days depending on variety.",

"Total foodgrain": "Harvest period varies between 90-150 days depending on crop.",


"Gram": "Harvest after 120-150 days when pods dry completely.",

"Masoor": "Harvest after 110-130 days when pods mature.",

"Lentil": "Harvest after 100-120 days when plants turn yellow.",

"Moong(Green Gram)": "Harvest after 60-90 days when pods mature.",

"Blackgram": "Harvest after 70-90 days when pods turn black.",

"Urad": "Harvest after 70-90 days when pods become black.",

"Moth": "Harvest after 90-120 days when pods dry.",

"Horse-gram": "Harvest after 120-150 days when pods mature.",

"Rajmash Kholar": "Harvest after 90-120 days when pods dry.",

"Ricebean (nagadal)": "Harvest after 90-120 days when pods mature.",

"Khesari": "Harvest after 120-150 days when pods dry.",

"Other Kharif pulses": "Harvest after 90-120 days depending on variety.",

"Other Rabi pulses": "Harvest after 100-150 days depending on variety.",

"Other Summer Pulses": "Harvest after 60-90 days depending on variety.",

"Pulses total": "Harvest period varies between 60-150 days depending on pulse crop.",

"Peas & beans (Pulses)": "Harvest after 70-100 days when pods mature.",

"Peas  (vegetable)": "Harvest after 60-90 days when pods are tender."
    
}


# Update only harvest field
for crop, details in crops.items():

    if crop in harvest_data:
        details["harvest"] = harvest_data[crop]


# Save updated JSON
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(crops, f, indent=4, ensure_ascii=False)


print("Harvest information updated successfully!")