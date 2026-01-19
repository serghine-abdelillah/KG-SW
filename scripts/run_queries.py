from rdflib import Graph

g = Graph()
g.parse("../data/tourism_graph.ttl", format="turtle")

query_files = [
    "../queries/q1_all_hotels.sparql",
    "../queries/q2_hotels_by_city.sparql",
    "../queries/q3_hotels_by_rating.sparql",
    "../queries/q4_avg_price_city.sparql",
    "../queries/q5_affordable_hotels.sparql"
]

for qfile in query_files:
    print(f"\n--- Running {qfile} ---")
    with open(qfile, "r") as f:
        query = f.read()
    results = g.query(query)
    for row in results:
        print(row)
