from src.model_inference import predict_price

def test_prediction():
    sample = {
        "area": 1200,
        "bedrooms": 3,
        "bathrooms": 2,
        "age": 5,
        "location": "CityCenter",
        "property_type": "Apartment"
    }
    price = predict_price(sample)
    assert price > 0
