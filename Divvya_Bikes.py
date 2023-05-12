from flask import Flask, request, jsonify
from Free_Bike import Free_Bike
from StatioN_Status import StatioN_Status




app = Flask(__name__)
data = {}
@app.route("/")
def stations():

    s = StatioN_Status()
    i = Free_Bike()
    data["total_active_stations"] = s.activeStationsData()
    data[ "total_docks_avl"] = sum(s.docksQty())
    data["total_bikes_avl"] = sum(s.bikesQty())
    data["bikes_list"] = i.bikeList()
    data["total_reserve_bike"] = i.resevBike()
    
    return jsonify(data)





if __name__ == "__main__" :
    app.run()
