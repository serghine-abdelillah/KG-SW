# populate.py
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, XSD
import random
import os

# Load ontology
g = Graph()
g.parse("../data/tourism_ontology.ttl", format="turtle")

EX = Namespace("http://abdelillahSerghine.org/tourism#")
g.bind("ex", EX)

# Ensure data folder exists
os.makedirs("../data", exist_ok=True)

# -------------------------------
# Cities (Europe + Algeria)
# -------------------------------
cities = {
    "Paris": "France",
    "London": "UK",
    "Rome": "Italy",
    "Berlin": "Germany",
    "Barcelona": "Spain",
    "Algiers": "Algeria",
    "Oran": "Algeria",
    "Constantine": "Algeria",
    "Annaba": "Algeria",
    "Tlemcen": "Algeria"
}

for city, country in cities.items():
    city_uri = EX[city]
    g.add((city_uri, RDF.type, EX.City))
    g.add((city_uri, EX.name, Literal(city)))
    g.add((city_uri, EX.country, Literal(country)))

# -------------------------------
# Real hotels per city (≈30)
# -------------------------------
hotels_by_city = {
    "Paris": [
        "Hotel Ritz Paris",
        "Le Meurice",
        "Hotel Lutetia",
        "Shangri-La Paris"
    ],
    "London": [
        "The Savoy",
        "The Ritz London",
        "Claridges",
        "The Langham"
    ],
    "Rome": [
        "Hotel Eden",
        "Hotel de Russie",
        "Rome Cavalieri",
        "Hotel Quirinale"
    ],
    "Berlin": [
        "Hotel Adlon Kempinski",
        "The Ritz Carlton Berlin",
        "Hotel de Rome",
        "Steigenberger Hotel"
    ],
    "Barcelona": [
        "W Barcelona",
        "Hotel Arts Barcelona",
        "Majestic Hotel",
        "H10 Casa Mimosa"
    ],
    # ---------------- Algeria ----------------
    "Algiers": [
        "El Aurassi Hotel",
        "Hotel Sofitel Algiers",
        "AZ Hotel Kouba",
        "Hotel Saint George"
    ],
    "Oran": [
        "Hotel Sheraton Oran",
        "Royal Hotel Oran",
        "Four Points Oran"
    ],
    "Constantine": [
        "Hotel Novotel Constantine",
        "Hotel Ibis Constantine"
    ],
    "Annaba": [
        "Hotel Sheraton Annaba",
        "Rym El Djamil Hotel"
    ],
    "Tlemcen": [
        "Hotel Renaissance Tlemcen",
        "Hotel Les Zianides"
    ]
}

# -------------------------------
# Create hotel instances
# -------------------------------
for city, hotel_list in hotels_by_city.items():
    for hotel_name in hotel_list:
        hotel_uri = EX[hotel_name.replace(" ", "").replace("-", "")]

        g.add((hotel_uri, RDF.type, EX.Hotel))
        g.add((hotel_uri, EX.name, Literal(hotel_name)))
        g.add((hotel_uri, EX.locatedIn, EX[city]))
        g.add((hotel_uri, EX.stars, Literal(random.randint(3, 5), datatype=XSD.int)))
        g.add((hotel_uri, EX.pricePerNight,
               Literal(round(random.uniform(60, 400), 2), datatype=XSD.float)))
        g.add((hotel_uri, EX.hasRating,
               Literal(round(random.uniform(3.2, 5.0), 1), datatype=XSD.float)))

# -------------------------------
# Save populated graph
# -------------------------------
g.serialize("../data/tourism_graph.ttl", format="turtle")
print(" Tourism graph populated with real hotels (Europe + Algeria)")
