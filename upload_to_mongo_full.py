import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB (adjust IP and port if needed)
client = MongoClient("mongodb://149.165.171.120:27017/")
db = client["flightdb"]
collection = db["airports"]

# Read the CSV
df = pd.read_csv("airports.csv")

# Convert DataFrame to dictionary records and insert into MongoDB
records = df.to_dict(orient="records")
collection.insert_many(records)
print(f"✅ Inserted {len(records)} records into MongoDB.")

# Example Queries
print("\nTotal documents:")
print(collection.count_documents({}))

print("\nSample airport in the United States:")
print(collection.find_one({"Country": "United States"}))

print("\nAirports above 5000 ft altitude:")
for doc in collection.find({"Altitude": {"$gt": 5000}}).limit(5):
    print(doc)

print("\nTop 5 countries by number of airports:")
pipeline = [
    {"$group": {"_id": "$Country", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 5}
]
for doc in collection.aggregate(pipeline):
    print(doc)

print("\nAirports with 'International' in their name:")
for doc in collection.find({"Name": {"$regex": ".*International.*"}}).limit(3):
    print(doc)

print("\nAirports in Europe/London timezone:")
for doc in collection.find({"Tz": "Europe/London"}).limit(3):
    print(doc)