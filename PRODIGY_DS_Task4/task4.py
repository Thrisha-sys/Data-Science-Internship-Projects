# Import necessary libraries
import pandas as pd  # For data manipulation
import re  # For regular expressions to clean text
from textblob import TextBlob  # For sentiment analysis
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For data visualization, specifically for count plots

# Step 1: Load the Dataset
# Load the dataset from the specified path and read it into a DataFrame
data = pd.read_csv('C:/Users/akhil/OneDrive/Desktop/DSI/dataset4/twitter_training.csv')  # Replace with the path to your dataset
print(data.head())  # Display the first few rows to verify that the dataset loaded correctly

# Step 2: Data Cleaning with Type Check
# Define a function to clean text data by removing unwanted characters and formats
def clean_text(text):
    if not isinstance(text, str):  # Check if the text is a string
        return ""  # Return an empty string if text is not a string (e.g., NaN values)
    text = text.lower()  # Convert text to lowercase to standardize it
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # Remove URLs starting with 'http' or 'www'
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove punctuation, special characters, and numbers
    return text  # Return the cleaned text

# Apply the cleaning function to the 'Text' column in the dataset
data['cleaned_text'] = data['Text'].apply(clean_text)

# Display the original and cleaned text columns to verify that cleaning worked as expected
print(data[['Text', 'cleaned_text']].head())

# Step 3: Sentiment Analysis using TextBlob
# Define a function to perform sentiment analysis on the cleaned text
def get_sentiment(text):
    blob = TextBlob(text)  # Create a TextBlob object for sentiment analysis
    polarity = blob.sentiment.polarity  # Extract the polarity score (-1 to 1 scale)
    if polarity > 0:
        return 'Positive'  # Positive sentiment for polarity greater than 0
    elif polarity == 0:
        return 'Neutral'  # Neutral sentiment for polarity equal to 0
    else:
        return 'Negative'  # Negative sentiment for polarity less than 0

# Apply sentiment analysis to the 'cleaned_text' column and store the result in a new 'sentiment' column
data['sentiment'] = data['cleaned_text'].apply(get_sentiment)

# Step 4: Visualize Sentiment Distribution
plt.figure(figsize=(8, 6))  # Set the figure size for better readability
# Create a count plot to show the distribution of each sentiment category in the dataset
sns.countplot(x='sentiment', data=data, palette='viridis')  # Use 'viridis' color palette
plt.title('Sentiment Distribution in Social Media Data')  # Title of the plot
plt.xlabel('Sentiment')  # Label for the x-axis
plt.ylabel('Count')  # Label for the y-axis
plt.show()  # Display the plot
