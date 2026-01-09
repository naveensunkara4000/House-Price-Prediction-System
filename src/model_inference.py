import pickle
import pandas as pd
from config.config import MODEL_PATH

def predict_price(input_data):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    df = pd.DataFrame([input_data])
    return model.predict(df)[0]
