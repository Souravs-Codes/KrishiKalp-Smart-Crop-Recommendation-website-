import joblib

mlb = joblib.load("models/multilabel_binarizer.pkl")

print("Total crops:", len(mlb.classes_))

print(list(mlb.classes_))