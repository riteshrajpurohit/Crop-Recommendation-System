# Crop Recommendation System

A Flask-based machine learning project that recommends the most suitable crop from soil and weather inputs. The app uses a trained Random Forest classifier, while `load_crop_data.py` provides a complete data inspection, cleaning, preprocessing, and model comparison report.

## Table of Contents

- [Overview](#overview)
- [Project Highlights](#project-highlights)
- [Dataset and Data Check](#dataset-and-data-check)
- [Load Data Script Output](#load-data-script-output)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Web App Usage](#web-app-usage)
- [Technologies Used](#technologies-used)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

## Overview

This project helps users predict the best crop for given agricultural conditions. The model uses seven features:

| Feature     | Meaning                          |
| ----------- | -------------------------------- |
| N           | Nitrogen content in soil         |
| P           | Phosphorus content in soil       |
| K           | Potassium content in soil        |
| pH          | Soil acidity or alkalinity level |
| temperature | Average temperature              |
| humidity    | Relative humidity                |
| rainfall    | Rainfall amount                  |

The backend trains a machine learning model on the crop dataset, and the web interface accepts user inputs to generate a recommendation instantly.

## Project Highlights

| Area               | Details                                      |
| ------------------ | -------------------------------------------- |
| Model              | Random Forest Classifier                     |
| Input Features     | N, P, K, pH, temperature, humidity, rainfall |
| Data Scaling       | StandardScaler                               |
| Training Split     | 80 percent train, 20 percent test            |
| Validation Metrics | Accuracy and weighted F1-score               |
| Web Interface      | Flask + HTML template                        |

## Dataset and Data Check

The dataset file is `Crop_recommendation.csv`. The cleaning script checks for missing values, duplicate rows, and data consistency before training.

### Schema

| Column       | Type    | Role    |
| ------------ | ------- | ------- |
| N            | Numeric | Feature |
| P            | Numeric | Feature |
| K            | Numeric | Feature |
| pH           | Numeric | Feature |
| temperature  | Numeric | Feature |
| humidity     | Numeric | Feature |
| rainfall     | Numeric | Feature |
| label / crop | Text    | Target  |

## Load Data Script Output

Running `python3 load_crop_data.py` produced the following result.

### Data Quality Summary

| Check                                | Result |
| ------------------------------------ | ------ |
| Total missing values before cleaning | 0      |
| Duplicate rows before cleaning       | 0      |
| Total missing values after cleaning  | 0      |
| Duplicate rows after cleaning        | 0      |

### First 5 Rows of the Cleaned Dataset

| Row | N   | P   | K   | temperature | humidity  | pH       | rainfall   | label |
| --- | --- | --- | --- | ----------- | --------- | -------- | ---------- | ----- |
| 0   | 90  | 42  | 43  | 20.879744   | 82.002744 | 6.502985 | 202.935536 | rice  |
| 1   | 85  | 58  | 41  | 21.770462   | 80.319644 | 7.038096 | 226.655537 | rice  |
| 2   | 60  | 55  | 44  | 23.004459   | 82.320763 | 7.840207 | 263.964248 | rice  |
| 3   | 74  | 35  | 40  | 26.491096   | 80.158363 | 6.980401 | 242.864034 | rice  |
| 4   | 78  | 42  | 42  | 20.130175   | 81.604873 | 7.628473 | 262.717340 | rice  |

### Feature Matrix Preview

| Row | N   | P   | K   | pH       | temperature | humidity  | rainfall   |
| --- | --- | --- | --- | -------- | ----------- | --------- | ---------- |
| 0   | 90  | 42  | 43  | 6.502985 | 20.879744   | 82.002744 | 202.935536 |
| 1   | 85  | 58  | 41  | 7.038096 | 21.770462   | 80.319644 | 226.655537 |
| 2   | 60  | 55  | 44  | 7.840207 | 23.004459   | 82.320763 | 263.964248 |
| 3   | 74  | 35  | 40  | 6.980401 | 26.491096   | 80.158363 | 242.864034 |
| 4   | 78  | 42  | 42  | 7.628473 | 20.130175   | 81.604873 | 262.717340 |

### Normalized Feature Matrix Preview

| Row | N        | P         | K         | pH       | temperature | humidity | rainfall |
| --- | -------- | --------- | --------- | -------- | ----------- | -------- | -------- |
| 0   | 1.068797 | -0.344551 | -0.101688 | 0.043302 | -0.935587   | 0.472666 | 1.810361 |
| 1   | 0.933329 | 0.140616  | -0.141185 | 0.734873 | -0.759646   | 0.397051 | 2.242058 |
| 2   | 0.255986 | 0.049647  | -0.081939 | 1.771510 | -0.515898   | 0.486954 | 2.921066 |
| 3   | 0.635298 | -0.556811 | -0.160933 | 0.660308 | 0.172807    | 0.389805 | 2.537048 |
| 4   | 0.743673 | -0.344551 | -0.121436 | 1.497868 | -1.083647   | 0.454792 | 2.898373 |

### Target Vector Preview

| Row | label |
| --- | ----- |
| 0   | rice  |
| 1   | rice  |
| 2   | rice  |
| 3   | rice  |
| 4   | rice  |

### Train-Test Split

| Split   | Shape     |
| ------- | --------- |
| X_train | (1760, 7) |
| X_test  | (440, 7)  |
| y_train | (1760,)   |
| y_test  | (440,)    |

### Trained Models

| Model         |
| ------------- |
| svm           |
| knn           |
| random_forest |

### Model Comparison

| Model         | Accuracy | Weighted F1-score |
| ------------- | -------- | ----------------- |
| random_forest | 0.995455 | 0.995452          |
| svm           | 0.984091 | 0.984038          |
| knn           | 0.979545 | 0.979283          |

## Project Structure

```text
Crop Recommendation System/
├── app.py
├── load_crop_data.py
├── Crop_recommendation.csv
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

| File                    | Purpose                                                            |
| ----------------------- | ------------------------------------------------------------------ |
| app.py                  | Flask app, model training, and crop prediction endpoint            |
| load_crop_data.py       | Data cleaning, preprocessing, scaling, and model comparison script |
| Crop_recommendation.csv | Dataset used for training and evaluation                           |
| requirements.txt        | Python dependencies                                                |
| templates/index.html    | Frontend page for user input and prediction display                |

## Folder Structure Setup

If you want to recreate this project from scratch, use the same structure below:

```text
Crop Recommendation System/
├── app.py
├── load_crop_data.py
├── Crop_recommendation.csv
├── requirements.txt
├── README.md
└── templates/
	└── index.html
```

### What Each Folder or File Does

| Path                    | Purpose                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| app.py                  | Runs the Flask web application and serves the prediction form                                        |
| load_crop_data.py       | Loads the dataset, cleans it, scales features, trains multiple models, and prints evaluation results |
| Crop_recommendation.csv | Main dataset used for training and comparison                                                        |
| requirements.txt        | Contains the Python packages needed by the project                                                   |
| README.md               | Project documentation and setup guide                                                                |
| templates/              | Flask template directory required for HTML pages                                                     |
| templates/index.html    | Main frontend page shown in the browser                                                              |

### Recommended Setup Flow

| Step | Action                                                 |
| ---- | ------------------------------------------------------ |
| 1    | Create the project folder                              |
| 2    | Add `app.py` and `load_crop_data.py` to the root       |
| 3    | Place `Crop_recommendation.csv` in the root directory  |
| 4    | Create `templates/` and keep `index.html` inside it    |
| 5    | Add dependency names to `requirements.txt`             |
| 6    | Run `python3 load_crop_data.py` to verify data loading |
| 7    | Run `python app.py` to start the web app               |

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd "Crop Recommendation System"
```

### 2. Create a virtual environment

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

### Run the web app

```bash
python app.py
```

Then open:

- http://127.0.0.1:5000
- http://localhost:5000

### Run the data loading and model comparison script

```bash
python3 load_crop_data.py
```

This prints the cleaning summary, dataset previews, train-test split shapes, trained model names, and evaluation table.

## How It Works

| Step | Description                                                    |
| ---- | -------------------------------------------------------------- |
| 1    | Load the CSV dataset                                           |
| 2    | Standardize the schema and target column                       |
| 3    | Remove missing values and duplicates                           |
| 4    | Split into features and target                                 |
| 5    | Normalize features with StandardScaler                         |
| 6    | Split data into training and testing sets                      |
| 7    | Train SVM, KNN, and Random Forest models                       |
| 8    | Compare model performance using accuracy and weighted F1-score |
| 9    | Use the trained model in the Flask app for predictions         |

### Prediction flow in the web app

| Stage      | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| User input | User enters N, P, K, pH, temperature, humidity, and rainfall |
| Validation | The app checks that all fields are numeric                   |
| Scaling    | Inputs are transformed using the trained StandardScaler      |
| Prediction | Random Forest returns the most suitable crop                 |
| Result     | The crop name is displayed on the page                       |

## Web App Usage

| Field       | Example Value | Notes                         |
| ----------- | ------------- | ----------------------------- |
| N           | 90            | Nitrogen in soil              |
| P           | 42            | Phosphorus in soil            |
| K           | 43            | Potassium in soil             |
| pH          | 6.5           | Soil pH level                 |
| temperature | 25.5          | Temperature in degree Celsius |
| humidity    | 70            | Relative humidity percentage  |
| rainfall    | 20.0          | Rainfall amount               |

Example input:

| Parameter   | Value |
| ----------- | ----- |
| N           | 90    |
| P           | 42    |
| K           | 43    |
| pH          | 6.5   |
| temperature | 25.5  |
| humidity    | 70    |
| rainfall    | 200.0 |

Expected output:

| Result                 |
| ---------------------- |
| Recommended Crop: Rice |

## Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Core programming language           |
| Flask        | Web application framework           |
| pandas       | Data loading and preprocessing      |
| scikit-learn | ML models, scaling, and evaluation  |
| HTML/CSS     | Frontend page structure and styling |
| Jinja2       | Template rendering in Flask         |

## Troubleshooting

| Issue                         | Fix                                                      |
| ----------------------------- | -------------------------------------------------------- |
| ModuleNotFoundError for Flask | Run `pip install -r requirements.txt`                    |
| CSV file not found            | Confirm `Crop_recommendation.csv` is in the project root |
| Port 5000 already in use      | Stop the process using the port or change the app port   |
| Invalid numeric values        | Enter numbers only in all input fields                   |

## Future Improvements

| Improvement                 | Benefit                             |
| --------------------------- | ----------------------------------- |
| Add confidence score        | Show prediction certainty           |
| Save recommendation history | Track previous results              |
| Add charts and analytics    | Make the interface more informative |
| Support more datasets       | Improve flexibility                 |
| Deploy to cloud             | Make the app publicly accessible    |
| Add multilingual support    | Improve usability for more users    |

## License

This project is open-source and can be used for educational or commercial purposes.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a pull request.

- ✅ Real-time crop recommendations
- ✅ Input validation and error handling

---

**Happy Farming! 🌾**

For best recommendations, ensure your input parameters match your actual farm conditions.
