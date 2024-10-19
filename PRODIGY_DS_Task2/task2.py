'''Task 02: Titanic Dataset - Data Cleaning and EDA

Data Cleaning: Handle missing values, ensure data consistency, and address any outliers.

Exploratory Data Analysis (EDA): Analyze survival rates by class, gender, age, and fare. Visualize these relationships to observe any significant patterns.

Patterns and Trends: Explore survival probabilities by different factors and summarize the findings. '''

# Importing necessary libraries
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For data visualization, specifically for enhanced plot aesthetics

# Load the Titanic dataset
# Load the dataset from the specified path and read it into a DataFrame
titanic_data = pd.read_csv('C:/Users/akhil/OneDrive/Desktop/DSI/dataset2/train.csv')

# Step 1: Data Cleaning
# Fill missing 'Age' values with the median age of the column
titanic_data['Age'] = titanic_data['Age'].fillna(titanic_data['Age'].median())

# Fill missing 'Embarked' values with the most frequent value (mode)
# First, find the most frequent value in the 'Embarked' column
embarked_mode = titanic_data['Embarked'].mode()[0]
# Replace missing values in 'Embarked' with this most frequent value
titanic_data['Embarked'] = titanic_data['Embarked'].fillna(embarked_mode)

# Convert 'Sex' column to numeric values for easier analysis: 0 for female, 1 for male
titanic_data['Sex'] = titanic_data['Sex'].map({'female': 0, 'male': 1})

# Step 2: Exploratory Data Analysis (EDA)
# Set a consistent aesthetic style for seaborn plots
sns.set(style="whitegrid")

# 2.1 Survival Rate by Gender
plt.figure(figsize=(6, 4))  # Set the figure size for better readability
# Create a bar plot to visualize survival rate by gender
sns.barplot(x='Sex', y='Survived', data=titanic_data)
plt.xticks([0, 1], ['Female', 'Male'])  # Label x-axis: 0 as Female, 1 as Male
plt.title('Survival Rate by Gender')  # Title for the plot
plt.xlabel('Gender')  # Label x-axis
plt.ylabel('Survival Rate')  # Label y-axis
plt.show()  # Display the plot

# 2.2 Survival Rate by Passenger Class
plt.figure(figsize=(6, 4))  # Set figure size for passenger class plot
# Create a bar plot to visualize survival rate by passenger class
sns.barplot(x='Pclass', y='Survived', data=titanic_data)
plt.title('Survival Rate by Passenger Class')  # Title for the plot
plt.xlabel('Passenger Class')  # Label x-axis
plt.ylabel('Survival Rate')  # Label y-axis
plt.show()  # Display the plot

# 2.3 Age Distribution of Survivors and Non-Survivors
plt.figure(figsize=(8, 5))  # Set figure size for age distribution plot
# Create KDE (Kernel Density Estimate) plots to show age distribution of survivors and non-survivors
sns.kdeplot(titanic_data[titanic_data['Survived'] == 1]['Age'], label='Survived', fill=True)  # Survived
sns.kdeplot(titanic_data[titanic_data['Survived'] == 0]['Age'], label='Not Survived', fill=True)  # Not Survived
plt.title('Age Distribution of Survivors and Non-Survivors')  # Title for the plot
plt.xlabel('Age')  # Label x-axis
plt.ylabel('Density')  # Label y-axis
plt.legend()  # Display legend to differentiate survival status
plt.show()  # Display the plot

# Step 3: Correlation Heatmap
plt.figure(figsize=(10, 6))  # Set figure size for correlation heatmap
# Select only numeric columns from the DataFrame to avoid errors in correlation computation
numeric_data = titanic_data.select_dtypes(include=['float64', 'int64'])
# Create a heatmap to visualize correlations between numeric features
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')  # Title for the heatmap
plt.show()  # Display the heatmap
