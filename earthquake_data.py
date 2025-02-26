import requests
import json

class EarthquakeData:
    def __init__(self):
        self.urls = {"sevenDay":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
                     "allMonth":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson",
                     "pastDay":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson",
                     "pastHour":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"}

    def all_month_data(self):
        url = self.urls["allMonth"]
        request_data = requests.get(url)
        json_data = request_data.json()
        return json_data["features"]

    def seven_day_data(self):
        url = self.urls["sevenDay"]
        request_data = requests.get(url)
        json_data = request_data.json()
        return json_data["features"]

    def past_day_data(self):
        url = self.urls["pastDay"]
        request_data = requests.get(url)
        json_data = request_data.json()
        return json_data["features"]

    def past_hour_data(self):
        url = self.urls["pastHour"]
        request_data = requests.get(url)
        json_data = request_data.json()
        return json_data["features"]



earthquakes = EarthquakeData()
seven_day_data = earthquakes.seven_day_data()
for earthquake in seven_day_data:
    print(earthquake["properties"]["title"])
