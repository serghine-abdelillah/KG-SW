from rdflib import Graph, Namespace

EX = Namespace("http://abdelillahSerghine.org/tourism#")

g = Graph()
g.parse("data/tourism_graph_extended.ttl", format="turtle")

def get_cities():
    return sorted(set(str(c).split("#")[-1] for c in g.subjects(None, EX.City)))

def get_hotels():
    return sorted(set(str(h).split("#")[-1] for h in g.subjects(None, EX.Hotel)))

def get_hotel_details(hotel_name):
    q = f"""
    PREFIX ex: <{EX}>
    SELECT ?cityName ?stars ?price ?rating ?touristName
    WHERE {{
        ex:{hotel_name} a ex:Hotel ;
            ex:locatedIn ?city ;
            ex:stars ?stars ;
            ex:pricePerNight ?price ;
            ex:hasReview ?review .

        ?city ex:name ?cityName .
        ?review ex:hasRating ?rating ;
                ex:writtenBy ?tourist .
        ?tourist ex:name ?touristName .
    }}
    """

    results = g.query(q)

    data = {
        "city": None,
        "stars": None,
        "price": None,
        "reviews": []
    }

    for r in results:
        data["city"] = str(r.cityName)
        data["stars"] = int(r.stars)
        data["price"] = float(r.price)
        data["reviews"].append({
            "rating": float(r.rating),
            "tourist": str(r.touristName)
        })

    return data

def get_hotels_in_city(city):
    q = f"""
    PREFIX ex: <{EX}>
    SELECT ?hotel WHERE {{
        ?hotel a ex:Hotel ;
               ex:locatedIn ex:{city} .
    }}
    """
    return [str(r.hotel).split("#")[-1] for r in g.query(q)]
