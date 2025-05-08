# Jetstream2 MongoDB Virtualization Project

This project demonstrates how to set up a MongoDB instance using Docker on Jetstream2, ingest a real-world airport dataset using Python, and perform sample queries through PyMongo.

## 📦 Contents

- `upload_to_mongo_full.py`: Python script to ingest data into MongoDB and perform queries.
- Screenshots: MongoDB status, data insertion confirmation, query outputs.
- Report (optional): Summarizes methodology, results, and challenges.

## 🔧 Technologies Used

- MongoDB 6.0 (via Docker)
- Jetstream2 (virtual machines)
- Python 3.12
- PyMongo, Pandas
- Ubuntu 22.04

## 🚀 Setup Instructions

### 1. Launch Jetstream2 Instances

- Create two VMs on Jetstream2: `mongo-vm` (for MongoDB) and `analyticsinstance` (for data processing).
- Use Ubuntu 22.04 as the base image.

### 2. On `mongo-vm`

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo docker run -d -p 27017:27017 --name mongodb mongo:6.0
```

### 3. On `analyticsinstance`

```bash
sudo apt update
sudo apt install -y python3-pip
python3 -m venv venv
source venv/bin/activate
pip install pandas pymongo
```

Download dataset and Python file:
```bash
wget https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat -O airports.csv
```

Then run:
```bash
python upload_to_mongo_full.py
```

### 4. Sample Queries (in script)

- Count records
- Filter by country, altitude, timezone
- Aggregate by country
- Regex match on name

## 📎 References

- [Jetstream2 Docs](https://docs.jetstream-cloud.org/)
- [MongoDB](https://www.mongodb.com/)
- [OpenFlights Dataset](https://github.com/jpatokal/openflights)