from flask import Flask, render_template, request, jsonify
import pandas as pd

from utils.crop_info import get_crop_details
from utils.predict import recommend_crops


# Load dataset only once
dataset = pd.read_csv("data/processed/master_dataset.csv")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/states")
def get_states():

    states = sorted(
        dataset["state_name"].dropna().unique().tolist()
    )

    return jsonify(states)


@app.route("/api/districts/<state>")
def get_districts(state):

    districts = (
        dataset[dataset["state_name"] == state]
        ["district_name"]
        .dropna()
        .unique()
        .tolist()
    )

    districts.sort()

    return jsonify(districts)


@app.route("/predict")
def predict():

    states = sorted(
        dataset["state_name"]
        .dropna()
        .unique()
        .tolist()
    )

    return render_template(
        "predict.html",
        states=states
    )


@app.route("/recommend", methods=["POST"])
def recommend():

    data = {
        "state_name": [request.form["state_name"]],
        "district_name": [request.form["district_name"]],
        "season": [request.form["season"]],
        "Boron": [float(request.form["boron"])],
        "Copper": [float(request.form["copper"])],
        "Electrical Conductivity": [float(request.form["electrical_conductivity"])],
        "Iron": [float(request.form["iron"])],
        "Manganese": [float(request.form["manganese"])],
        "Nitrogen": [float(request.form["nitrogen"])],
        "Organic Carbon": [float(request.form["organic_carbon"])],
        "Phosphorus": [float(request.form["phosphorus"])],
        "Potassium": [float(request.form["potassium"])],
        "Soil Ph": [float(request.form["soil_ph"])],
        "Sulphur": [float(request.form["sulphur"])],
        "Zinc": [float(request.form["zinc"])],
        "temperature": [float(request.form["temperature"])],
        "rainfall": [float(request.form["rainfall"])],
        "humidity": [float(request.form["humidity"])],
        "wind_speed": [float(request.form["wind_speed"])],
        "solar_radiation": [float(request.form["solar_radiation"])]
    }


    input_df = pd.DataFrame(data)


    recommendations = recommend_crops(input_df)

    top_crops = recommendations[:3]


    crop_details = []

    for crop in top_crops:
        crop_details.append({
            "name": crop,
            "info": get_crop_details(
                crop,
                input_df
            )
        })


    return render_template(
        "result.html",
        crops=crop_details,
        state=data["state_name"][0],
        district=data["district_name"][0]
    )


if __name__ == "__main__":
    app.run(debug=True)