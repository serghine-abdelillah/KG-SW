from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:3030/tourism/sparql")

sparql.setQuery("""
PREFIX ex: <http://example.org/tourism#>

SELECT ?hotel ?rating
WHERE {
  ?hotel a ex:Hotel ;
         ex:hasRating ?rating .
  FILTER(?rating >= 4)
}
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for r in results["results"]["bindings"]:
    print(r["hotel"]["value"], r["rating"]["value"])
