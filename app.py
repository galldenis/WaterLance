from flask import Flask, render_template, request
from geopy.distance import great_circle

app = Flask(__name__)


fountains =[
{"name": "Fountain 1", "latitude": 45.764764, "longitude": 21.205476},
{"name": "Fountain 2", "latitude": 45.769774, "longitude": 21.216080},
{"name": "Fountain 3", "latitude": 45.752607, "longitude": 21.252886},
{"name": "Fountain 4", "latitude": 45.731511, "longitude": 21.241347},
{"name": "Fountain 5", "latitude": 45.769309, "longitude": 21.247127},
{"name": "Fountain 6", "latitude": 45.760655, "longitude": 21.253191},
{"name": "Fountain 7", "latitude": 45.735804, "longitude": 21.212614},
{"name": "Fountain 8", "latitude": 45.737219, "longitude": 21.205148},
{"name": "Fountain 9", "latitude": 45.751283, "longitude": 21.221639},
{"name": "Fountain 10", "latitude": 45.762157, "longitude": 21.237765},
{"name": "Fountain 11", "latitude": 45.757736, "longitude": 21.235970},
{"name": "Fountain 12", "latitude": 45.761490, "longitude": 21.228633},
{"name": "Fountain 13", "latitude": 45.754937, "longitude": 21.200920},
{"name": "Fountain 14", "latitude": 45.755278, "longitude": 21.188553},
{"name": "Fountain 15", "latitude": 45.745485, "longitude": 21.262956},
{"name": "Fountain 16", "latitude": 45.751267, "longitude": 21.221646},
{"name": "Fountain 17", "latitude": 45.728615, "longitude": 21.209695},
{"name": "Fountain 18", "latitude": 45.737524, "longitude": 21.216453},
{"name": "Fountain 19", "latitude": 45.759088, "longitude": 21.225105},
{"name": "Fountain 22", "latitude": 45.740477, "longitude": 21.207590},
{"name": "Fountain 23", "latitude": 45.770451, "longitude": 21.208407},
{"name": "Fountain 24", "latitude": 45.759056, "longitude": 21.203462},
{"name": "Fountain 25", "latitude": 45.757161, "longitude": 21.214304},
{"name": "Fountain 26", "latitude": 45.740673, "longitude": 21.239477},
{"name": "Fountain 27", "latitude": 45.750142, "longitude": 21.280370},
{"name": "Fountain 28", "latitude": 45.730052, "longitude": 21.264702},
{"name": "Fountain 29", "latitude": 45.732494, "longitude": 21.200601},
{"name": "Fountain 30", "latitude": 45.736329, "longitude": 21.251961},
{"name": "Fountain 31", "latitude": 45.753858, "longitude": 21.256843},
{"name": "Fountain 32", "latitude": 45.765116, "longitude": 21.219272},
{"name": "Fountain 33", "latitude": 45.730235, "longitude": 21.209502},
{"name": "Fountain 34", "latitude": 45.746419, "longitude": 21.216423},
{"name": "Fountain 35", "latitude": 45.741134, "longitude": 21.211555},
{"name": "Fountain 36", "latitude": 45.723161, "longitude": 21.202125},
{"name": "Fountain 37", "latitude": 45.728013, "longitude": 21.181452},
{"name": "Fountain 38", "latitude": 45.769757, "longitude": 21.216109},
{"name": "Fountain 39", "latitude": 45.774608, "longitude": 21.221247},
{"name": "Fountain 40", "latitude": 45.745921, "longitude": 21.241001},
{"name": "Fountain 41", "latitude": 45.772354, "longitude": 21.219153},
{"name": "Fountain 42", "latitude": 45.757911, "longitude": 21.229492},
{"name": "Fountain 43", "latitude": 45.759959, "longitude": 21.277085},
{"name": "Fountain 44", "latitude": 45.752226, "longitude": 21.190456},
{"name": "Fountain 45", "latitude": 45.757895, "longitude": 21.250350},
{"name": "Fountain 46", "latitude": 45.762243, "longitude": 21.237986},
{"name": "Fountain 47", "latitude": 45.723355, "longitude": 21.202511},
{"name": "Fountain 48", "latitude": 45.728098, "longitude": 21.181556},
{"name": "Fountain 49", "latitude": 45.735619, "longitude": 21.239769},
{"name": "Fountain 50", "latitude": 45.750109, "longitude": 21.244515},
{"name": "Fountain 51", "latitude": 45.741568, "longitude": 21.226211},
{"name": "Fountain 52", "latitude": 45.735505, "longitude": 21.239544},
{"name": "Fountain 53", "latitude": 45.765602, "longitude": 21.259637},
{"name": "Fountain 54", "latitude": 45.758604, "longitude": 21.246666},
{"name": "Fountain 55", "latitude": 45.752225, "longitude": 21.190460},
{"name": "Fountain 56", "latitude": 45.779570, "longitude": 21.237211},
{"name": "Fountain 57", "latitude": 45.735083, "longitude": 21.249034},
{"name": "Fountain 58", "latitude": 45.754934, "longitude": 21.226883},
{"name": "Fountain 59", "latitude": 45.757830, "longitude": 21.250429},
{"name": "Fountain 60", "latitude": 45.763058, "longitude": 21.189344},
{"name": "Fountain 61", "latitude": 45.730080, "longitude": 21.264751},
{"name": "Fountain 62", "latitude": 45.752433, "longitude": 21.295777}
]


@app.route("/", methods=["get","post"])
def closest_fountain():
    if not request.args.get('longitude') or not request.args.get('latitude'):
        return render_template('page.html')
    lat = request.args.get('longitude')
    lng = request.args.get('latitude')
    user_location = (lat, lng)

    closest_fountain = None
    closest_distance = None
    for fountain in fountains:
        fountain_location = (fountain["latitude"], fountain["longitude"])
        distance = great_circle(user_location, fountain_location).m
        if closest_fountain is None or distance < closest_distance:
            closest_fountain = fountain
            closest_distance = distance

    return render_template('test.html', lat_p=lat, lng_p=lng, lat_f=closest_fountain['latitude'], lng_f=closest_fountain['longitude'])





# de pe chat openai--------------------------------------------------------------------------------------
#     from geopy.distance import geodesic
# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="myGeocoder")

# fountains = [{"name":"Fountain 1", "latitude": 45.7588, "longitude": 21.2275},
#              {"name":"Fountain 2", "latitude": 45.7492, "longitude": 21.2394},
#              #93 more fountains with name and coordinates
#              {"name":"Fountain 93", "latitude": 45.7492, "longitude": 21.2394}]

# def find_nearest_fountain(user_location):
#     nearest_fountain = None
#     shortest_distance = None
#     for fountain in fountains:
#         d = geodesic((lat, lng), (fountain["latitude"], fountain["longitude"]))
#         if not nearest_fountain or d.km < shortest_distance:
#             shortest_distance = d.km
#             nearest_fountain = fountain
#     return nearest_fountain

# location = geolocator.geocode("Timisoara, Romania")
# nearest_fountain = find_nearest_fountain(location)
# print("The nearest fountain is {} located at {}, {} with a distance of {} km".format(
#     nearest_fountain["name"], nearest_fountain["latitude"], nearest_fountain["longitude"], shortest_distance))