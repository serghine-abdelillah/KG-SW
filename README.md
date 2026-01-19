# Tourism Knowledge Graph Web Interface

This project implements a semantic Knowledge Graph (KG) for tourism using RDF/Turtle and provides a web interface to explore it, similar to Wikidata.  
The interface allows users to browse hotels, view details, and access related entities like cities, tourists, and reviews.

---

## ✅ Features

- RDF/Turtle Knowledge Graph (KG)
- Linked entities (Hotel → City → Review → Tourist)
- Web interface built with Flask
- SPARQL queries to fetch data dynamically
- Entity pages with semantic URLs (like Wikidata)
- Bootstrap-based UI for clean design

---

## 📁 Project Structure
e-tourism/
│
├─ src/
│ ├─ ontology.py
│ └─ populate_extended.py
├─ app.py
├─ ontology_connected.py
├─ populate_extended.py
├─ requirements.txt
├─ README.md
│
├─ templates/
│ ├─ index.html
│ └─ hotel.html
│
└─ data/
├─ tourism_ontology_connected.ttl
└─ tourism_graph_extended.ttl


