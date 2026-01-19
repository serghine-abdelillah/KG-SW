# ontology_connected.py
from rdflib import Graph, Namespace, RDF, RDFS, OWL, XSD

# Initialize graph
g = Graph()
EX = Namespace("http://abdelillahSerghine.org/tourism#")
g.bind("ex", EX)

# -------------------------------
# Define Classes
# -------------------------------
classes = ["Place", "City", "Accommodation", "Hotel", "Tourist", "Attraction", "Review"]
for cls in classes:
    g.add((EX[cls], RDF.type, OWL.Class))

# Class hierarchy
g.add((EX.Hotel, RDFS.subClassOf, EX.Accommodation))
g.add((EX.City, RDFS.subClassOf, EX.Place))

# -------------------------------
# Define Properties
# -------------------------------
# Object properties
g.add((EX.locatedIn, RDF.type, OWL.ObjectProperty))  # Hotel → City / Attraction → City
g.add((EX.hasReview, RDF.type, OWL.ObjectProperty))  # Hotel → Review
g.add((EX.writtenBy, RDF.type, OWL.ObjectProperty))  # Review → Tourist
g.add((EX.visits, RDF.type, OWL.ObjectProperty))     # Tourist → Attraction

# Datatype properties
g.add((EX.name, RDF.type, OWL.DatatypeProperty))
g.add((EX.stars, RDF.type, OWL.DatatypeProperty))
g.add((EX.pricePerNight, RDF.type, OWL.DatatypeProperty))
g.add((EX.hasRating, RDF.type, OWL.DatatypeProperty))
g.add((EX.country, RDF.type, OWL.DatatypeProperty))

# -------------------------------
# Domain and Range Definitions
# -------------------------------
# Hotel related
g.add((EX.locatedIn, RDFS.domain, EX.Hotel))
g.add((EX.locatedIn, RDFS.range, EX.City))
g.add((EX.hasReview, RDFS.domain, EX.Hotel))
g.add((EX.hasReview, RDFS.range, EX.Review))

# Review related
g.add((EX.writtenBy, RDFS.domain, EX.Review))
g.add((EX.writtenBy, RDFS.range, EX.Tourist))

# Attraction related
g.add((EX.locatedIn, RDFS.domain, EX.Attraction))
g.add((EX.locatedIn, RDFS.range, EX.City))
g.add((EX.visits, RDFS.domain, EX.Tourist))
g.add((EX.visits, RDFS.range, EX.Attraction))

# -------------------------------
# Save ontology
# -------------------------------
import os
os.makedirs("../data", exist_ok=True)
g.serialize("../data/tourism_ontology_connected.ttl", format="turtle")
print("Ontology saved with connected classes and properties")
