import joblib

mlb = joblib.load("models/multilabel_binarizer.pkl")

print(mlb.classes_)