# populate_extended.py
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, XSD
import random

# Load existing populated graph
g = Graph()
g.parse("../data/tourism_graph.ttl", format="turtle")

EX = Namespace("http://abdelillahSerghine.org/tourism#")
g.bind("ex", EX)

# ------------------------------------------------
# Tourists (20 instances)
# ------------------------------------------------
tourists = [
    "AliceMartin", "JohnSmith", "MohamedAli", "SarahJohnson", "YassineB",
    "EmmaBrown", "LucasDubois", "AmineK", "SofiaGarcia", "LiamWilson",
    "NoahMuller", "ChloeBernard", "KarimH", "InesZ", "DavidM",
    "FatimaL", "PaulR", "NinaS", "OmarT", "LauraP"
]

for t in tourists:
    tourist_uri = EX[t]
    g.add((tourist_uri, RDF.type, EX.Tourist))
    g.add((tourist_uri, EX.name, Literal(t)))

# ------------------------------------------------
# Attractions per city (≈20)
# ------------------------------------------------
attractions_by_city = {
    "Paris": ["Eiffel Tower", "Louvre Museum", "Montmartre"],
    "London": ["Big Ben", "London Eye", "British Museum"],
    "Rome": ["Colosseum", "Vatican Museums", "Trevi Fountain"],
    "Berlin": ["Brandenburg Gate", "Berlin Wall Memorial"],
    "Barcelona": ["Sagrada Familia", "Park Güell"],
    "Algiers": ["Martyrs Memorial", "Casbah of Algiers"],
    "Oran": ["Santa Cruz Fort", "Oran Waterfront"],
    "Constantine": ["Sidi Mcid Bridge"],
    "Annaba": ["Basilica of St Augustine"],
    "Tlemcen": ["Mansourah Ruins"]
}

for city, attractions in attractions_by_city.items():
    for attr in attractions:
        attr_uri = EX[attr.replace(" ", "").replace("-", "")]
        g.add((attr_uri, RDF.type, EX.Attraction))
        g.add((attr_uri, EX.name, Literal(attr)))
        g.add((attr_uri, EX.locatedIn, EX[city]))

# ------------------------------------------------
# Reviews (≈30 instances)
# Review → Hotel
# Review → writtenBy Tourist
# ------------------------------------------------
hotels = list(g.subjects(RDF.type, EX.Hotel))

review_count = 1
for hotel in random.sample(hotels, min(30, len(hotels))):
    reviewer = EX[random.choice(tourists)]
    review_uri = EX[f"Review{review_count}"]

    g.add((review_uri, RDF.type, EX.Review))
    g.add((review_uri, EX.hasRating,
           Literal(round(random.uniform(3.0, 5.0), 1), datatype=XSD.float)))
    g.add((review_uri, EX.writtenBy, reviewer))
    g.add((hotel, EX.hasReview, review_uri))

    review_count += 1

# ------------------------------------------------
# Save extended graph
# ------------------------------------------------
g.serialize("../data/tourism_graph_extended.ttl", format="turtle")

print(" Tourism graph successfully extended:")
print(" - Tourists added")
print(" - Attractions added")
print(" - Reviews linked to hotels and tourists")
