import os
import sys

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.data_preprocessing import load_and_prepare_data
from src.model_training import train_models
from src.model_evaluation import business_insights

def main():
    X_train, X_test, y_train, y_test = load_and_prepare_data("data/house_prices.csv")
    train_models(X_train, X_test, y_train, y_test)
    business_insights()

if __name__ == "__main__":
    main()
