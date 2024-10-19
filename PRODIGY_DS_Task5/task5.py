# Import necessary libraries for data analysis and visualization
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For plotting graphs
import seaborn as sns  # For creating attractive statistical plots

# Load a subset of the dataset to keep the analysis manageable
# Load the first 10,000 rows; this helps to work with a large dataset efficiently
data = pd.read_csv('C:/Users/akhil/OneDrive/Desktop/DSI/dataset5/US_Accidents_March23.csv', nrows=10000)

# Display the first few rows of the data to understand its structure
print(data.head())

# Step 1: Data Analysis - Understanding patterns by weather, road conditions, and time of day

# Convert 'Start_Time' column to datetime format to easily extract date and time components
data['Start_Time'] = pd.to_datetime(data['Start_Time'])

# Extract the hour of the accident from 'Start_Time' to analyze time-of-day patterns
data['Hour'] = data['Start_Time'].dt.hour

# Step 2: Visualize accident frequency by time of day
# Create a figure with specified size for better readability of the histogram
plt.figure(figsize=(10, 6))

# Plot a histogram showing the frequency of accidents at each hour of the day (0 to 23)
# The 'kde=True' parameter adds a smooth density line over the histogram
sns.histplot(data['Hour'], bins=24, kde=True)

# Set the title and labels for the plot to make it informative
plt.title('Accident Frequency by Hour of Day')  # Title of the plot
plt.xlabel('Hour of Day')  # Label for x-axis (0-23 hours)
plt.ylabel('Number of Accidents')  # Label for y-axis (accident count)
plt.show()  # Display the plot

# Step 3: Analyze the impact of Weather and Road Conditions on accident frequency

# Plot the count of accidents for each weather condition
# We only show the top 10 weather conditions for readability
plt.figure(figsize=(12, 8))  # Set figure size for readability

# Use seaborn's countplot to plot the frequency of accidents by weather condition
# 'order' parameter arranges conditions by their frequency in descending order (top 10)
sns.countplot(y='Weather_Condition', data=data, order=data['Weather_Condition'].value_counts().index[:10])

# Add title and axis labels for clarity
plt.title('Top 10 Weather Conditions Leading to Accidents')  # Plot title
plt.xlabel('Number of Accidents')  # Label for x-axis
plt.ylabel('Weather Condition')  # Label for y-axis
plt.show()  # Display the plot

# Plot accident count by road condition (if 'Road_Condition' column exists in the dataset)
# Note: Check for the column's existence to avoid errors if the column is not present
if 'Road_Condition' in data.columns:
    plt.figure(figsize=(12, 8))  # Set figure size for clarity
    
    # Plot the frequency of accidents by road condition using countplot
    sns.countplot(y='Road_Condition', data=data, order=data['Road_Condition'].value_counts().index[:10])
    
    # Set the title and axis labels to describe the plot content
    plt.title('Top 10 Road Conditions Leading to Accidents')  # Title of the plot
    plt.xlabel('Number of Accidents')  # Label for x-axis
    plt.ylabel('Road Condition')  # Label for y-axis
    plt.show()  # Display the plot

# Step 4: Accident Hotspot Visualization - using Latitude and Longitude

# Create a scatter plot to show accident locations based on latitude and longitude
plt.figure(figsize=(10, 6))  # Set figure size for better readability

# Scatter plot using 'Start_Lng' for longitude (x-axis) and 'Start_Lat' for latitude (y-axis)
# 'alpha=0.2' makes points semi-transparent, so areas with many points appear denser (hotspots)
sns.scatterplot(x='Start_Lng', y='Start_Lat', data=data, alpha=0.2)

# Set plot title and axis labels to describe the content
plt.title('Accident Hotspots (Latitude vs Longitude)')  # Title for the plot
plt.xlabel('Longitude')  # Label for x-axis
plt.ylabel('Latitude')  # Label for y-axis
plt.show()  # Display the plot
