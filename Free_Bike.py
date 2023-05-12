import requests
import json

class Free_Bike:
    
    reserved_list = []    


    def getData(self):
        try:
            print("Free_bike_status Scripts Started")
            url = "https://gbfs.divvybikes.com/gbfs/en/free_bike_status.json"
            headers = { 'Accept':'application/json','Content-Type': 'application/x-www-form-urlencoded' }
            response = requests.get(url, headers=headers, timeout=15)


            serialization = response.json()
            print('Response_Code :',response.status_code)

            jsondata = json.dumps(serialization)

            dictdata = json.loads(jsondata)
        except Exception as e:
            self.Log.error("Error get payload")

        return dictdata


    def bikeList(self):
        jsdata = self.getData()
        data = jsdata.get('data')
        dictdata =data.get('bikes')
        for i in dictdata:
            self.reserved_list.append(i.get("is_reserved"))

        return len(dictdata)


    def resevBike(self):
        #print(reserved_list)
        return sum(self.reserved_list)

i = Free_Bike()
print(i.bikeList())
print(i.resevBike())
