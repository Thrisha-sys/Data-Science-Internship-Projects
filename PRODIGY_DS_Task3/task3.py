# Importing necessary libraries
import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting dataset into training and testing sets
from sklearn.tree import DecisionTreeClassifier  # Decision Tree algorithm
from sklearn.metrics import accuracy_score, confusion_matrix  # For model evaluation metrics
import seaborn as sns  # For visualization of the confusion matrix
import matplotlib.pyplot as plt  # For plotting

# Step 1: Load the Dataset
# Load the Bank Marketing dataset into a DataFrame, specifying the delimiter as ';'
data = pd.read_csv('C:/Users/akhil/OneDrive/Desktop/DSI/dataset3/bank-full.csv', delimiter=';')
print(data.head())  # Display the first few rows to understand the dataset structure

# Step 2: Encode Categorical Variables
# Convert categorical features into numeric using one-hot encoding; drop_first=True removes the first category to avoid redundancy
data = pd.get_dummies(data, drop_first=True)

# Step 3: Prepare Features and Target Variable
# Separate the features (X) and target variable (y)
# Drop the column 'y_yes' from X as it will serve as our target variable
X = data.drop('y_yes', axis=1)  # X contains all columns except the target
y = data['y_yes']  # y contains the target variable 'y_yes' indicating if a term deposit was subscribed

# Step 4: Split Data into Training and Testing Sets
# Split the dataset into 80% training and 20% testing to evaluate model performance
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Print shapes to verify the split
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Step 5: Train the Decision Tree Classifier
# Create an instance of DecisionTreeClassifier with a fixed random state for reproducibility
dt_classifier = DecisionTreeClassifier(random_state=42)

# Fit the classifier on the training data
dt_classifier.fit(X_train, y_train)

# Step 6: Evaluate the Model
# Predict the target values for the test set
y_pred = dt_classifier.predict(X_test)

# Calculate and print the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 7: Confusion Matrix Visualization
# Generate a confusion matrix to assess the performance of the classifier
conf_matrix = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix using Seaborn's heatmap
plt.figure(figsize=(6, 4))  # Set the figure size
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',  # Annotate with actual counts, in 'Blues' color
            xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])  # Label x and y ticks as 'No' and 'Yes'
plt.xlabel('Predicted')  # Set x-axis label as 'Predicted'
plt.ylabel('Actual')  # Set y-axis label as 'Actual'
plt.title('Confusion Matrix')  # Set the plot title
plt.show()  # Display the plot
