from flask import Flask, jsonify, request
import requests
#import simplejson as json



app = Flask(__name__)

###     In this function get data from divyabikes station_url and bike_url, 
#       Store in a variable and get total_active_stations, total_bikes_avl, 
#       total_reserved_bikes and store it on a dict and displayed in local  web server  

@app.route("/")
def main():
    try:
        data = {}
        # Divvya bikes station_status jsondata url
        station_url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
        # Divvya bikes jsondata url
        free_bike_url = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
        # Use header for Json application
        headers = { 'Accept':'application/json','Content-Type': 'application/x-www-form-urlencoded' }
        
        #Send GET requests to Station_status web address and recive proper response
        station_response= requests.get(station_url, headers)

        # Send GET requests to free_bike_status web adress and recive response
        free_bike_response = requests.get(free_bike_url, headers)

        # Print response code if recive 200 means no error
        print("Sataion_Response", station_response.status_code)
        print("Free_Bike_Response",free_bike_response.status_code)
        
        # Decode Jsondata
        bikeJsondata = free_bike_response.json()
        bikesdata = bikeJsondata.get('data')
        bikes = bikesdata.get('bikes')
        #total_bikes = len(bikesdata)
        reserved_bike = 0
        for bike in bikes:
            if bike.get("is_reserved") == 1:
                reserved_bike += 1
        stJsondata =  station_response.json()
        stationdata = stJsondata.get('data')
        #return jsonify(stationdata)
        stations = stationdata.get("stations")
        total_stations = len(stations)
        counter = 0
        docksdata = []
        bikesdata = []
        for docks in stations:
            docksdata.append(docks.get("num_docks_available"))
            bikesdata.append(docks.get("num_ebikes_available"))
            if docks.get("station_status") == "active":
                counter += 1

        data["total_docks_avl"] = sum(docksdata)
        data["total_bikes_avl"] = sum(bikesdata)
        data["total_station_active"] = counter
        data["total_bikes_avl"] = len(bikesdata)
        data ["total_bikes_reserved"] = reserved_bike
        return jsonify(data)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    app.run(debug=True, port=8080)
