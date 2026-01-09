import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_prepare_data(path):
    df = pd.read_csv(path)

    # Normalize column names (very important)
    df.columns = df.columns.str.strip().str.lower()

    if "price" not in df.columns:
        raise ValueError("Target column 'price' not found in dataset")

    X = df.drop("price", axis=1)
    y = df["price"]

    return train_test_split(X, y, test_size=0.2, random_state=42)
