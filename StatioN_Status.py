import requests
import json

class StatioN_Status:

    bikes = []
    docks = []

    def getData(self):
        try:
            print("Divvya Bikes Stations ...")
            url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
            headers = { 'Accept':'application/json','Content-Type': 'application/x-www-form-urlencoded' }
            response = requests.get(url, headers=headers, timeout=15)


            serialization = response.json()
            print('Response_Code :',response.status_code)

            jsondata = json.dumps(serialization)

            dictdata = json.loads(jsondata)
        except Exception as e:
            self.Log.error("Error get payload")

        return dictdata

    def stationsData(self):
        jsondata = self.getData()
        mainstation = jsondata.get("data")

        stations = mainstation.get("stations")

        print('Stations :',len(stations))

        return stations
    def activeStationsData(self):
        satations = self.stationsData()
        activestationcount = 0
        for i in satations:
            if i.get('station_status') == 'active':
                activestationcount += 1
            self.docks.append(i.get('num_docks_available'))
                
            self.bikes.append(i.get('num_bikes_available'))
        return activestationcount
    
    def docksQty(self):
        #print(self.docks)
        return self.docks

    def bikesQty(self):
        #print(self.bikes)
        return self.bikes
    
s = StatioN_Status()
a = s.activeStationsData()
d = s.docksQty()
print(sum(d))
print(sum(s.bikesQty()))

