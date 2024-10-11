# Data Science Internship Projects - Prodigy Infotech

# Author: Thrisha D

This repository contains data analysis and visualization tasks completed as part of the Data Science Internship at Prodigy Infotech. Each project focuses on a unique aspect of data analysis, including visualization, classification, sentiment analysis, and exploratory data analysis.

## Requirements

To run these projects, ensure you have the following libraries installed:
```bash
pip install pandas matplotlib seaborn textblob nltk scikit-learn
```

## Task 1: Population Distribution Visualization

### Objective

Create a bar chart to visualize the population distribution by country for the year 2020.

### Dataset

- **Dataset**: [World Bank Population Data](https://data.worldbank.org/indicator/SP.POP.TOTL)
- **File**: `API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv`

### Instructions

1. **Load the Dataset**:
   - Download the dataset from the link above.
   - Load the dataset with `pandas`, skipping the initial metadata rows.

2. **Data Cleaning**:
   - Remove unnecessary columns and retain only relevant columns: `Country Name`, `Country Code`, `Indicator Name`, and `2020`.
   - Drop rows with missing values for the 2020 population.

3. **Visualization**:
   - Select the first 10 countries and create a horizontal bar chart with country names and population for 2020.
   - Add titles and labels.

### Code
Refer to `task1.py` for the complete code.

---

## Task 2: Titanic Data Analysis

### Objective

Perform data cleaning and exploratory data analysis (EDA) on the Titanic dataset, exploring relationships between features like age, gender, and survival rate.

### Dataset

- **Dataset**: [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic)
- **File**: `train.csv`

### Instructions

1. **Load the Dataset**:
   - Download and load the Titanic dataset using `pandas`.

2. **Data Cleaning**:
   - Handle missing values in the `Age` and `Embarked` columns.
   - Create new features and encode categorical variables as necessary.

3. **Exploratory Data Analysis (EDA)**:
   - Visualize survival rates by gender, passenger class, and age.
   - Create a correlation heatmap for numerical features.

### Code
Refer to `task2.py` for the complete code.

---

## Task 3: Bank Marketing Dataset - Decision Tree Classifier

### Objective

Build a decision tree classifier to predict if a customer will subscribe to a term deposit.

### Dataset

- **Dataset**: [Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- **File**: `bank-full.csv`

### Instructions

1. **Load the Dataset**:
   - Download the dataset from the UCI Machine Learning Repository.
   - Load the dataset and perform one-hot encoding on categorical columns.

2. **Model Training**:
   - Split the data into training and testing sets, then train a `DecisionTreeClassifier`.

3. **Evaluation**:
   - Evaluate the model using accuracy, precision, and recall.
   - Display a confusion matrix for performance visualization.

### Code
Refer to `task3.py` for the complete code.

---

## Task 4: Social Media Sentiment Analysis

### Objective

Analyze sentiment in social media data to understand public opinion.

### Dataset

- **Dataset**: [Twitter US Airline Sentiment](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
- **File**: `twitter_training.csv`

### Instructions

1. **Load the Dataset**:
   - Load the dataset with `pandas`.

2. **Data Cleaning**:
   - Define a `clean_text` function to preprocess text, removing URLs, punctuation, and converting text to lowercase.

3. **Sentiment Analysis**:
   - Use TextBlob to analyze sentiment and classify each tweet as Positive, Neutral, or Negative.

4. **Visualization**:
   - Plot the distribution of sentiment using a bar chart.

### Code
Refer to `task4.py` for the complete code.

---

## Task 5: Traffic Accident Data Analysis

### Objective

Analyze traffic accident data to identify patterns related to weather, road conditions, and time of day.

### Dataset

- **Dataset**: [US Traffic Accidents (2016 - 2021)](https://www.kaggle.com/sobhanmoosavi/us-accidents)
- **File**: `US_Accidents_March23.csv`

### Instructions

1. **Load a Subset of the Dataset**:
   - Load the first 10,000 rows of the dataset for manageable analysis.

2. **Analysis of Accident Trends**:
   - Extract accident hour from the `Start_Time` column and plot accident frequency by hour.

3. **Impact of Weather and Road Conditions**:
   - Analyze accident frequency under different weather and road conditions.

4. **Hotspot Visualization**:
   - Plot a geographic scatter plot using accident latitude and longitude.

### Code
Refer to `task5.py` for the complete code.

---

## Additional Notes

Each task has its own script file (e.g., `task1.py`, `task2.py`) containing the code with detailed comments. Make sure to adjust file paths in each script as necessary before running. 

This README provides a structured approach for running each task, with clear objectives and steps for replication. Each task showcases various aspects of data analysis, including data visualization, classification, and sentiment analysis.
