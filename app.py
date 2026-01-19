from flask import Flask, render_template
import kg

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cities")
def cities():
    return render_template("cities.html", cities=kg.get_cities())

@app.route("/city/<city>")
def city(city):
    hotels = kg.get_hotels_in_city(city)
    return render_template("city.html", city=city, hotels=hotels)

@app.route("/hotels")
def hotels():
    return render_template("hotels.html", hotels=kg.get_hotels())

@app.route("/hotel/<hotel>")
def hotel(hotel):
    details = kg.get_hotel_details(hotel)
    return render_template("hotel.html", hotel=hotel, details=details)


if __name__ == "__main__":
    app.run(debug=True)
