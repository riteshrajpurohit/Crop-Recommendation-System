# 🌾 Crop Recommendation System

An intelligent web-based application that recommends the most suitable crops to grow based on soil and weather parameters using machine learning.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Data Requirements](#data-requirements)
- [Future Improvements](#future-improvements)

---

## 🎯 Overview

The **Crop Recommendation System** is a machine learning-powered web application designed to help farmers and agricultural professionals make data-driven decisions about crop selection. By inputting soil nutrients, pH level, and environmental conditions, the system predicts the most suitable crop to cultivate.

This system uses a **Random Forest Classification Model** trained on historical agricultural data to provide accurate recommendations.

---

## ✨ Features

✅ **Easy-to-use Web Interface** - Clean, responsive UI for crop recommendations  
✅ **Real-time Predictions** - Instant crop suggestions based on inputs  
✅ **Machine Learning Powered** - Random Forest model for accurate predictions  
✅ **Input Validation** - Validates all numeric inputs for data integrity  
✅ **Mobile Responsive** - Works seamlessly on desktop and mobile devices  
✅ **Error Handling** - User-friendly error messages for invalid inputs

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager - usually comes with Python)
- **Git** (optional, for version control)

### Check if Python is installed:

```bash
python --version
# or
python3 --version
```

---

## 🚀 Installation

### Step 1: Clone or Download the Project

If you have Git:

```bash
git clone <repository-url>
cd "Crop Recommendation System"
```

Or manually download and extract the project folder.

### Step 2: Navigate to Project Directory

```bash
cd /path/to/"Crop Recommendation System"
```

### Step 3: Create a Virtual Environment (Recommended)

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

_(Virtual environments keep project dependencies isolated from your system Python)_

### Step 4: Install Required Packages

```bash
pip install -r requirements.txt
```

This will install:

- **Flask** - Web framework for the UI
- **pandas** - Data manipulation and analysis
- **scikit-learn** - Machine learning library

---

## ▶️ How to Run

### Step 1: Activate Virtual Environment (if not already active)

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

### Step 2: Start the Application

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 3: Open in Browser

Click on the link or manually navigate to:

```
http://localhost:5000
```

or

```
http://127.0.0.1:5000
```

### Step 4: Stop the Application

Press `Ctrl + C` in your terminal/command prompt.

---

## 📁 Project Structure

```
Crop Recommendation System/
├── app.py                      # Main Flask application
├── load_crop_data.py          # Data loading and preprocessing utility
├── Crop_recommendation.csv    # Training dataset with crop data
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html            # Web interface (HTML/CSS/Form)
└── README.md                 # This file
```

### File Descriptions:

| File                        | Purpose                                                                      |
| --------------------------- | ---------------------------------------------------------------------------- |
| **app.py**                  | Main Flask application that handles routing, model training, and predictions |
| **load_crop_data.py**       | Utility script for data cleaning and preprocessing                           |
| **Crop_recommendation.csv** | Dataset containing features and target crop labels                           |
| **requirements.txt**        | Lists all Python package dependencies and versions                           |
| **templates/index.html**    | Frontend HTML template with CSS styling and form                             |

---

## 💻 Usage Guide

### Using the Web Application

1. **Open the Application**
   - Navigate to `http://localhost:5000` in your browser

2. **Enter the Parameters**

   Fill in the following fields with appropriate values:

   | Parameter       | Description                        | Example | Range                |
   | --------------- | ---------------------------------- | ------- | -------------------- |
   | **N**           | Nitrogen content in soil (mg/kg)   | 90      | 0-200                |
   | **P**           | Phosphorus content in soil (mg/kg) | 42      | 0-200                |
   | **K**           | Potassium content in soil (mg/kg)  | 43      | 0-200                |
   | **pH**          | Soil pH level                      | 6.5     | 0-14 (typically 3-9) |
   | **Temperature** | Average temperature (°C)           | 25.5    | Variable by region   |
   | **Humidity**    | Relative humidity (%)              | 70      | 0-100                |
   | **Rainfall**    | Annual rainfall (cm)               | 20.0    | 0-300+               |

3. **Get Recommendation**
   - Click the "Get Crop Recommendation" button
   - The system will display the recommended crop

4. **View Results**
   - ✅ Successful prediction shows the recommended crop
   - ❌ Error messages help identify invalid inputs

### Example Input:

```
N: 90
P: 42
K: 43
pH: 6.5
Temperature: 25.5 °C
Humidity: 70 %
Rainfall: 200.0 cm
```

**Output:** Recommended Crop: **Rice**

---

## 🤖 How It Works

### Model Architecture

```
Input Features (7)
    ↓
StandardScaler (Normalization)
    ↓
Random Forest Classifier
    ↓
Crop Prediction
```

### Step-by-Step Process:

1. **Data Loading**: CSV file is loaded with soil and weather parameters
2. **Data Cleaning**:
   - Removes null/missing values
   - Removes duplicate rows
   - Renames columns for consistency
3. **Feature Extraction**: Selects 7 features (N, P, K, pH, temperature, humidity, rainfall)
4. **Data Splitting**: 80% training, 20% testing
5. **Preprocessing**: StandardScaler normalizes the features to similar ranges
6. **Model Training**: Random Forest Classifier trained on normalized data
7. **Prediction**: New inputs are normalized and passed through the model

### Why Random Forest?

- **Accuracy**: Ensemble method combining multiple decision trees
- **Robustness**: Handles non-linear relationships well
- **Interpretability**: Feature importance can be extracted
- **Efficiency**: Fast prediction time

---

## 🛠️ Technologies Used

| Technology       | Purpose                                        |
| ---------------- | ---------------------------------------------- |
| **Python 3.7+**  | Programming language                           |
| **Flask**        | Web framework for creating the web application |
| **scikit-learn** | Machine learning library (Random Forest model) |
| **pandas**       | Data manipulation and analysis                 |
| **HTML/CSS**     | Frontend interface                             |
| **Jinja2**       | Template rendering (built into Flask)          |

---

## 📊 Data Requirements

The `Crop_recommendation.csv` file should contain the following columns:

```csv
N, P, K, pH, temperature, humidity, rainfall, crop
90, 42, 43, 6.5, 25.5, 70, 200.0, Rice
...
```

### Data Format:

- **Numeric columns**: N, P, K, pH, temperature, humidity, rainfall
- **Target column**: crop (name of the recommended crop)
- **Format**: CSV (Comma-Separated Values)
- **Missing values**: Should be minimal; duplicates will be removed automatically

### Supported Crops (Examples):

Rice, Corn, Wheat, Cotton, Sugarcane, Chickpea, Soybean, Maize, etc.
_(Depends on your actual dataset)_

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**

```bash
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: Crop_recommendation.csv"

**Solution:**

- Ensure the CSV file is in the same directory as `app.py`
- Check the filename spelling and case

### Issue: "Port 5000 is already in use"

**Solution:**

```bash
# On macOS/Linux:
lsof -i :5000
kill -9 <PID>

# Or run on a different port:
python app.py  # and edit app.py to change port
```

### Issue: Invalid numeric values error

**Solution:**

- Ensure all input fields have numeric values
- Check that values are reasonable for their respective parameters

---

## 📈 Future Improvements

- 🔐 Add user authentication and save recommendations history
- 📊 Display model accuracy and confidence scores
- 📁 Support multiple CSV datasets
- 🗺️ Add location-based recommendations
- 📱 Create mobile app version
- 🌐 Deploy to cloud (Heroku, AWS, Google Cloud)
- 📈 Model comparison (test multiple algorithms)
- 💾 Allow users to upload custom datasets
- 📧 Email recommendation reports
- 🎨 Enhanced UI with data visualization charts
- 🌍 Multi-language support
- 📝 Detailed crop care instructions

---

## 📝 License

This project is open-source. Feel free to modify and use it for educational and commercial purposes.

---

## 👨‍💻 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📞 Support & Contact

If you encounter any issues or have questions:

- Check the [Troubleshooting](#troubleshooting) section
- Review your input parameters
- Ensure all dependencies are installed correctly

---

## 🙏 Acknowledgments

- Agricultural data sourced from crop research databases
- Machine learning powered by scikit-learn
- Built with Flask web framework

---

## 📝 Changelog

### Version 1.0 (Current)

- ✅ Initial release with Random Forest model
- ✅ Web UI with form inputs
- ✅ Real-time crop recommendations
- ✅ Input validation and error handling

---

**Happy Farming! 🌾**

For best recommendations, ensure your input parameters match your actual farm conditions.
