import os
import pandas as pd
from pymongo import MongoClient

# Print the current working directory
print("Current working directory:", os.getcwd())

# List files in the current directory
print("Files in the current directory:", os.listdir())

# Step 1: Define the CSV file path (relative path)
csv_file_path = 'example_data _.csv'

# Verify if the file exists
if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"The file at path {csv_file_path} does not exist. Please check the path.")

# Step 2: Read the CSV file
df = pd.read_csv(csv_file_path)

# Step 3: Convert the DataFrame to JSON
data = df.to_dict(orient='records')

# Step 4: Insert JSON data into MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Connect to the MongoDB server
db = client['example_database']  # Use or create a database named 'school_database'
collection = db['example_data']  # Use or create a collection named 'student_performance'

# Insert data into MongoDB
collection.insert_many(data)

print("Data inserted successfully into MongoDB!")
