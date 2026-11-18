# EDA & Feature Engineering

A hands-on practice repository for **Exploratory Data Analysis (EDA)**, **data cleaning** and **feature engineering** in Python, using pandas, NumPy, Matplotlib, Seaborn and scikit-learn.

Each script works on a real-world dataset and walks through the usual steps: inspecting the data, fixing data types, handling messy values, creating new features and visualising patterns. The repo is updated regularly as I explore new datasets and techniques.

---

## Projects

### ✈️ Flight Price: Feature Engineering (`flight_price-EDA.py`)
Dataset: [Flight Price Prediction (Kaggle)](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction), business-class flights (`business.csv`, plus `economy.csv` and `Clean_Dataset.csv`).

- Split the `date` column into separate **Date / Month / Year** integer features
- Extract hour and minute from the arrival time
- Clean and normalise the `stop` column, then map it to ordinal values (`non-stop → 0`, `1-stop → 1`, `2+-stop → 2`)
- Parse `time_taken` into hours and minutes
- **One-hot encode** categorical columns (`airline`, `ch_code`, `num_code`) with scikit-learn's `OneHotEncoder`

### 📱 Google Play Store: Data Cleaning (`play_Store.py`)
Dataset: [Google Play Store apps](https://github.com/krishnaik06/playstore-Dataset), loaded directly from GitHub.

- Find and remove rows with non-numeric `Reviews`
- Convert `Size` to a numeric value (handling `M`, `k`, `+`, `,` and `"Varies with device"`)
- Strip `$`, `,` and `+` from `Installs` and `Price` and convert them to numbers
- Parse `Last Updated` into datetime and extract **Day / Month / Year**
- Export the result to `Cleaned_google_playstore.csv`

### 🍷 Red Wine Quality: EDA & Visualisation (`wine.py`)
Dataset: [Wine Quality (UCI)](https://archive.ics.uci.edu/dataset/186/wine+quality), red wine (`winequality-red.csv`).

- Load the data and remove duplicate rows
- Summarise its shape, data types, missing values and correlation matrix
- Save the plots: quality counts, quality distribution, correlation heatmap, pair plot and alcohol vs pH scatter plot
- Runs as a small command-line tool:

```bash
python wine.py                      # run and show plots
python wine.py --no-show            # just save plots to outputs/
python wine.py --data path/to.csv --output-dir my_plots
```

### 🧪 Python OOP practice
`student.py`, `main.py` and `calculator.py` are small class/object exercises.

---

## Repository structure

```
EDA-FE/
├── flight_price-EDA.py          # Flight price feature engineering
├── play_Store.py                # Play Store data cleaning
├── wine.py                      # Wine quality EDA + plots
├── business.csv                 # Flight data (business class)
├── economy.csv                  # Flight data (economy class)
├── Clean_Dataset.csv            # Flight data (combined, cleaned)
├── winequality-red.csv          # Red wine quality data
├── Cleaned_google_playstore.csv # Output of play_Store.py
├── Catplot.png, pairplot.png    # Saved visualisations
├── student.py, main.py, calculator.py  # OOP practice
└── requirements.txt
```

---

## Getting started

```bash
# 1. Clone the repo
git clone https://github.com/Stani21/EDA---Feature_Engineering.git
cd EDA---Feature_Engineering

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run any script
python wine.py
python flight_price-EDA.py
python play_Store.py
```

---

## Tech stack

Python 3.12 · pandas · NumPy · Matplotlib · Seaborn · scikit-learn

---

## Roadmap

- [ ] Handle missing values and outliers in the flight dataset
- [ ] Visualise price trends by airline, stops and days before departure
- [ ] Explore Play Store ratings by category and app type
- [ ] Try different encoding and scaling techniques (label, ordinal, target encoding, StandardScaler)
- [ ] Move the analyses into Jupyter notebooks with written insights

---

## 👤 Author

**Stanish**: [@Stani21](https://github.com/Stani21)
