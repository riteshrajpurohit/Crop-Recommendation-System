import argparse
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def clean_data(data: pd.DataFrame, missing_strategy: str = "mean") -> pd.DataFrame:
    missing_counts = data.isnull().sum()
    total_missing = int(missing_counts.sum())
    print(f"Total missing values before cleaning: {total_missing}")

    if total_missing > 0:
        print("Missing values by column:")
        print(missing_counts[missing_counts > 0])

    if missing_strategy == "mean":
        numeric_columns = data.select_dtypes(include="number").columns
        data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
        data = data.dropna()
    elif missing_strategy == "drop":
        data = data.dropna()
    else:
        raise ValueError("missing_strategy must be either 'mean' or 'drop'.")

    duplicate_count = int(data.duplicated().sum())
    print(f"Duplicate rows before cleaning: {duplicate_count}")
    if duplicate_count > 0:
        data = data.drop_duplicates()

    print(f"Total missing values after cleaning: {int(data.isnull().sum().sum())}")
    print(f"Duplicate rows after cleaning: {int(data.duplicated().sum())}")
    return data


def split_features_target(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    if "ph" in data.columns and "pH" not in data.columns:
        data = data.rename(columns={"ph": "pH"})

    target_column = "crop" if "crop" in data.columns else "label"
    feature_columns = ["N", "P", "K", "pH", "temperature", "humidity", "rainfall"]

    missing_columns = [column for column in feature_columns + [target_column] if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    X = data[feature_columns]
    y = data[target_column]
    return X, y


def normalize_features(X: pd.DataFrame) -> tuple[pd.DataFrame, StandardScaler]:
    scaler = StandardScaler()
    X_scaled_array = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled_array, columns=X.columns, index=X.index)
    return X_scaled, scaler


def split_train_test(
    X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )
    return X_train, X_test, y_train, y_test


def train_models(X_train: pd.DataFrame, y_train: pd.Series) -> dict[str, object]:
    models: dict[str, object] = {
        "svm": SVC(),
        "knn": KNeighborsClassifier(),
        "random_forest": RandomForestClassifier(random_state=42),
    }

    for model in models.values():
        model.fit(X_train, y_train)

    return models


def evaluate_models(
    models: dict[str, object], X_test: pd.DataFrame, y_test: pd.Series
) -> pd.DataFrame:
    rows = []
    for model_name, model in models.items():
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        f1 = f1_score(y_test, predictions, average="weighted")
        rows.append({"model": model_name, "accuracy": accuracy, "f1_score": f1})

    comparison = pd.DataFrame(rows).sort_values(by="accuracy", ascending=False).reset_index(drop=True)
    return comparison


def main() -> None:
    parser = argparse.ArgumentParser(description="Load and clean crop recommendation dataset.")
    parser.add_argument(
        "--missing-strategy",
        choices=["mean", "drop"],
        default="mean",
        help="How to handle missing values: fill numeric with mean or drop rows.",
    )
    args = parser.parse_args()

    csv_path = Path(__file__).parent / "Crop_recommendation.csv"
    data = pd.read_csv(csv_path)
    cleaned_data = clean_data(data, missing_strategy=args.missing_strategy)
    X, y = split_features_target(cleaned_data)
    X_scaled, _ = normalize_features(X)
    X_train, X_test, y_train, y_test = split_train_test(X_scaled, y, test_size=0.2)
    models = train_models(X_train, y_train)
    comparison = evaluate_models(models, X_test, y_test)

    print("\nFirst 5 rows of the cleaned crop dataset:\n")
    print(cleaned_data.head())
    print("\nFeature matrix (X) preview:\n")
    print(X.head())
    print("\nNormalized feature matrix (X_scaled) preview:\n")
    print(X_scaled.head())
    print("\nTarget vector (y) preview:\n")
    print(y.head())
    print("\nTrain-test split:")
    print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}, y_test shape: {y_test.shape}")
    print("\nTrained models:")
    print(list(models.keys()))
    print("\nModel comparison (accuracy and weighted F1-score):")
    print(comparison.to_string(index=False))


if __name__ == "__main__":
    main()
