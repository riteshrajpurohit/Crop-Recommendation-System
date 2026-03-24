from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

FEATURE_COLUMNS = ["N", "P", "K", "pH", "temperature", "humidity", "rainfall"]
TARGET_COLUMN = "crop"
PLACEHOLDER_EXAMPLES = {
    "N": "e.g. 90 (Nitrogen)",
    "P": "e.g. 42 (Phosphorus)",
    "K": "e.g. 43 (Potassium)",
    "pH": "e.g. 6.5 (range 0-7)",
    "temperature": "e.g. 25.5 °C",
    "humidity": "e.g. 70 %",
    "rainfall": "e.g. 20.0 cm",
}


class CropRecommendationService:
    def __init__(self, csv_path: Path) -> None:
        self.csv_path = csv_path
        self.scaler = StandardScaler()
        self.model = RandomForestClassifier(random_state=42)
        self._train_model()

    def _load_and_prepare_data(self) -> tuple[pd.DataFrame, pd.Series]:
        data = pd.read_csv(self.csv_path)

        if "ph" in data.columns and "pH" not in data.columns:
            data = data.rename(columns={"ph": "pH"})

        target_column = "label" if "label" in data.columns else TARGET_COLUMN
        data = data.dropna().drop_duplicates()

        X = data[FEATURE_COLUMNS]
        y = data[target_column]
        return X, y

    def _train_model(self) -> None:
        X, y = self._load_and_prepare_data()
        X_train, _, y_train, _ = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y,
        )
        X_train_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_train_scaled, y_train)

    def predict(self, values: dict[str, float]) -> str:
        input_df = pd.DataFrame([values], columns=FEATURE_COLUMNS)
        input_scaled = self.scaler.transform(input_df)
        prediction = self.model.predict(input_scaled)
        return str(prediction[0])


csv_file = Path(__file__).parent / "Crop_recommendation.csv"
service = CropRecommendationService(csv_file)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    form_values = {column: "" for column in FEATURE_COLUMNS}

    if request.method == "POST":
        try:
            for column in FEATURE_COLUMNS:
                form_values[column] = request.form.get(column, "").strip()

            input_values = {column: float(form_values[column]) for column in FEATURE_COLUMNS}
            prediction = service.predict(input_values)
        except ValueError:
            error = "Please enter valid numeric values for all fields."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        values=form_values,
        feature_columns=FEATURE_COLUMNS,
        placeholders=PLACEHOLDER_EXAMPLES,
    )


if __name__ == "__main__":
    app.run(debug=True)
