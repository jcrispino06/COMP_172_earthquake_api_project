import requests
import json

class EarthquakeData:
    def __init__(self):
        self.urls = {"sevenDay":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
                     "allMonth":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson",
                     "pastDay":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson",
                     "pastHour":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"}
    def get_bbox_data(self, url):
        request_data = requests.get(url)
        json_data = request_data.json()
        raw_bbox_data = json_data["bbox"]
        formatted_bbox_data = {
            "minLongitude":raw_bbox_data[0],
            "minLatitude":raw_bbox_data[1],
            "maxLongitude":raw_bbox_data[2],
            "maxLatitude":raw_bbox_data[3],
            "maxDepth":raw_bbox_data[4]
        }
        return formatted_bbox_data

    def past_month_data(self):
        url = self.urls["allMonth"]
        request_data = requests.get(url)
        json_data = request_data.json()
        bbox_data = self.get_bbox_data(url)
        return {"features":json_data["features"],"bbox":bbox_data}

    def past_week_data(self):
        url = self.urls["sevenDay"]
        request_data = requests.get(url)
        json_data = request_data.json()
        bbox_data = self.get_bbox_data(url)
        return {"features": json_data["features"], "bbox": bbox_data}

    def past_day_data(self):
        url = self.urls["pastDay"]
        request_data = requests.get(url)
        json_data = request_data.json()
        bbox_data = self.get_bbox_data(url)
        return {"features": json_data["features"], "bbox": bbox_data}

    def past_hour_data(self):
        url = self.urls["pastHour"]
        request_data = requests.get(url)
        json_data = request_data.json()
        bbox_data = self.get_bbox_data(url)
        return {"features": json_data["features"], "bbox": bbox_data}

