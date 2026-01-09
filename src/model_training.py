import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from config.config import MODEL_PATH

def train_models(X_train, X_test, y_train, y_test):

    numeric_features = ["area", "bedrooms", "bathrooms", "age"]
    categorical_features = ["location", "property_type"]

    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ])

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
    }

    best_model = None
    best_score = -1

    for name, model in models.items():
        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipeline.fit(X_train, y_train)
        preds = pipeline.predict(X_test)

        mae = mean_absolute_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        print(f"{name} -> MAE: ₹{mae:,.2f}, R2: {r2:.3f}")

        if r2 > best_score:
            best_score = r2
            best_model = pipeline

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(best_model, f)

    print(" Best model saved")
