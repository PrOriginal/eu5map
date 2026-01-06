import json
import os
import re as regex
class Location:
    def __init__(self,name,topography,vegetation,climate,religion,raw_material,culture=None,natural_harbor_suitability = 0, modifier = None):
        self.name = name
        self.topography = topography
        self.vegetation = vegetation
        self.climate = climate
        self.religion = religion
        self.culture = culture
        self.raw_material = raw_material
        self.natural_harbor_suitability = float(natural_harbor_suitability)
        self.modifier = modifier

    def to_dict(self):
        return self.__dict__

regex_valid_location = "^.+material.+$" #r"(\w+)\s*=\s*\{([^}]+)\}"
regex_location_name = "^\\w+"
regex_location_params = "(\w+)\s*=\s*([\w\d.]+)"

with open("location_templates.txt") as f:
    valid_locations = [line for line in f if regex.findall(regex_valid_location, line)]

locations_objects = []

for location in valid_locations:
    name = regex.findall(regex_location_name, location)
    params = dict(regex.findall(regex_location_params,location))
    locations_objects.append(Location(name=name, **params))

if os.path.exists("locations.json"):
    os.remove("locations.json")

with open("locations.json", "w") as f:
        f.write(json.dumps([location.to_dict() for location in locations_objects]))