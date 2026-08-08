from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "lightgbm_tuned_crop_recommender.pkl")
mlb = joblib.load(BASE_DIR / "models" / "multilabel_binarizer.pkl")
print(model.feature_names_in_)

def recommend_crops(input_df):
    prediction = model.predict(input_df)
    return mlb.inverse_transform(prediction)[0]


if __name__ == "__main__":
    sample_input = pd.DataFrame({
        "state_name": ["Andhra Pradesh"],
        "district_name": ["Anantapur"],
        "season": ["Kharif"],
        "Boron": [0.45],
        "Copper": [0.80],
        "Electrical Conductivity": [0.30],
        "Iron": [4.50],
        "Manganese": [3.20],
        "Nitrogen": [280],
        "Organic Carbon": [0.70],
        "Phosphorus": [18],
        "Potassium": [180],
        "Soil Ph": [6.8],
        "Sulphur": [12],
        "Zinc": [0.90],
        "temperature": [28],
        "rainfall": [750],
        "humidity": [70],
        "wind_speed": [10],
        "solar_radiation": [18]
    })

    recommendations = recommend_crops(sample_input)

    print("Recommended Crops:")
    for crop in recommendations:
        print("-", crop)