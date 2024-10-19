import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
ds = pd.read_csv('C:/Users/akhil/OneDrive/Desktop/DSI/dataset1/API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv', skiprows=3)

# Drop unnecessary columns (e.g., 'Unnamed: 68')
ds_cleaned = ds.drop(columns=['Unnamed: 68'])

# Drop columns that are not required for the analysis
ds_cleaned = ds[['Country Name', 'Country Code', 'Indicator Name', '2020']]

# Drop any rows where the 2020 population value is NaN
ds_cleaned = ds_cleaned.dropna(subset=['2020'])

# Display the cleaned data
print(ds_cleaned.head())

# Display only the first 10 countries from the dataset
ds_first10 = ds_cleaned.head(10)

# Create a bar chart for population in 2020
plt.figure(figsize=(10, 8))
plt.barh(ds_first10['Country Name'], ds_first10['2020'], color='lightblue')
plt.title('Population Distribution by Country in 2020')
plt.xlabel('Population')
plt.ylabel('Country')
plt.tight_layout()
plt.show()