import requests
import json

# NASA dataset URL
url = "https://data.nasa.gov/resource/y77d-th95.json"

# Fetch data from the URL
response = requests.get(url)
data = response.json()

### first question: How many entries are in the dataset?
print(f"Total meteorite entries in dataset: {len(data)}")

### second question: What is the name and mass of the most massive meteorite in this dataset?
meteorite_All_data = []
most_massive_meteorite = {"name": "Unknown", "mass": 0}

for meteorite in data:
    name = meteorite.get("name", "Unknown")
    mass = meteorite.get("mass", "0")  # Default mass to 0 if missing
    year = meteorite.get("year", "Unknown")
    latitude = meteorite.get("reclat", "Unknown")
    longitude = meteorite.get("reclong", "Unknown")

    # Convert mass to float for comparison
    try:
        mass = float(mass)
    except ValueError:
        mass = 0  # Ignore invalid mass values

    # Track the most massive meteorite
    if mass > most_massive_meteorite["mass"]:
         most_massive_meteorite = {"name": name, "mass": mass}

    meteorite_All_data.append({
        "name": name,
        "mass": mass,
        "year": year,
        "latitude": latitude,
        "longitude": longitude
    })

# Print extracted meteorite landing details
print(json.dumps(meteorite_All_data, indent=2))

# Print the most massive meteorite
print(f"\nMost massive meteorite: {most_massive_meteorite['name']} with mass {most_massive_meteorite['mass']} grams")
# print Total data entries
print(f"Total meteorite entries in dataset: {len(data)}")

###What is the most frequent year in this dataset?
#year_counts = year_Counter()
#year_counts[year] += 1
#print(f"Year: {year}, Count: {year_count}")