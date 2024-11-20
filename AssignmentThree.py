import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_name = 'StudentsPerformance.csv'  # Replace with your file path if necessary
try:
    data = pd.read_csv(file_name)
    print("Data Loaded Successfully!")
except FileNotFoundError:
    print("File not found. Please ensure the file exists in the specified location.")
    exit()

# Display the first few rows of the data
print("\nSample Data:")
print(data.head())

# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Data Cleaning
data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]  # Clean column names
data['math_score'] = pd.to_numeric(data['math_score'], errors='coerce')
data['reading_score'] = pd.to_numeric(data['reading_score'], errors='coerce')
data['writing_score'] = pd.to_numeric(data['writing_score'], errors='coerce')

# Add a column for average score
data['average_score'] = data[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

# Visualization
# 1. Average Scores by Gender
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='gender', y='average_score', ci=None, palette='Set2')
plt.title('Average Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.tight_layout()
plt.show()

# 2. Test Scores by Parental Level of Education
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='parental_level_of_education', y='average_score', palette='coolwarm')
plt.title('Test Scores by Parental Level of Education')
plt.xlabel('Parental Level of Education')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Math Scores Distribution by Lunch Type
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='math_score', hue='lunch', kde=True, palette='viridis')
plt.title('Math Scores Distribution by Lunch Type')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Test Preparation Course Impact
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='test_preparation_course', y='average_score', palette='muted')
plt.title('Impact of Test Preparation Course on Scores')
plt.xlabel('Test Preparation Course')
plt.ylabel('Average Score')
plt.tight_layout()
plt.show()

# 5. Race/Ethnicity Group Performance
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='race/ethnicity', y='average_score', palette='plasma')
plt.title('Average Test Scores by Race/Ethnicity Groups')
plt.xlabel('Race/Ethnicity')
plt.ylabel('Average Score')
plt.tight_layout()
plt.show()
