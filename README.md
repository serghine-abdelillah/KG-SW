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
``` bassh
e-tourism/
│
├─ src/
│ ├─ ontology.py
│ └─ populate_extended.py
│
├─ app.py
├─ kg.py
├─ requirements.txt
├─ README.md
│
├─ templates/
│ ├─ index.html
│ └─ hotel.html
│
├─ static/
│ ├─ style.css
│
│
└─ data/
├─ tourism_ontology_connected.ttl
└─ tourism_graph_extended.ttl

```

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/serghine-abdelillah/KG-SW.git
cd e-tourism
```

## Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
## Install dependencies
 ```bash
pip install -r requirements.txt
```
## 🧠 Generate the Knowledge Graph
 ### Run ontology file
 ```bash
python ontology_connected.py
```
This will generate the ontology file: **data/tourism_ontology_connected.ttl**

### Populate the graph
 ```bash
python populate_extended.py
```
This will generate the KG file: **data/tourism_graph_extended.ttl**

### Run the Web Interface
 ```bash
python app.py
```

Open your browser and go to:

http://127.0.0.1:5000/

🌐 Navigation

Home page lists all hotels

Click on any hotel to view details

Each entity has its own semantic URL

Example:

http://127.0.0.1:5000/hotel/HotelParis1

📌 Screenshots

Add your screenshots here:

Figure 1: Home page listing hotels

Figure 2: Hotel page with city and reviews

Figure 3: Graph relations visualization

⚙️ Requirements

Python 3.10+

Flask

rdflib

🧩 Notes

If you add new entities or properties, rerun:

python populate_extended.py

