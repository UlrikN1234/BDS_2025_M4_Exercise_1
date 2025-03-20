import requests
import pickle
import pandas as pd
import json


# Loading trained model, label encoder and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("le.pkl", "rb") as f:
    le = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Fetching new penguin data from API
url = "http://130.225.39.127:8000/new_penguin/"
response = requests.get(url)
data = response.json()

# Making prediction
features = [[
    data["bill_length_mm"],
    data["bill_depth_mm"],
    data["flipper_length_mm"],
    data["body_mass_g"]
]]

# Applying scaling
features_scaled = scaler.transform(features)

# Making prediction
predicted_species = model.predict(features_scaled)[0]
species = le.inverse_transform([predicted_species])[0]

#Save the prediction as JSON so we can gather data over time
penguin_prediction = {
    "datetime": data["datetime"],
    "bill_length_mm": data["bill_length_mm"],
    "bill_depth_mm": data["bill_depth_mm"],
    "flipper_length_mm": data["flipper_length_mm"],
    "body_mass_g": data["body_mass_g"],
    "predicted_species": species
}

# Saving updated predictions to JSON  
with open("penguin_prediction.json", "w") as f:
    json.dump(penguin_prediction, f, indent=4)

print("Prediction made and saved to database successfully. Prediction: {penguin_prediction}")