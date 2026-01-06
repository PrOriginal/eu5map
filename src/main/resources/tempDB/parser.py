import os
import re as regex
class Location:
    def __init__(self,name,topography,vegetation,climate,religion,culture,raw_material,natural_harbor_suitability = 0):
        self.name = name
        self.topography = topography
        self.vegetation = vegetation
        self.climate = climate
        self.religion = religion
        self.culture = culture
        self.raw_material = raw_material
        self.natural_harbor_suitability = natural_harbor_suitability

regex_valid_location = "^.+material.+$"
regex_location_name = "^\\w+"
regex_location_feature = ""
location_info = []

if os.path.exists("locations.json"):
    os.remove("locations.json")
db = open("locations.json", "x")

with open("location_templates.txt") as source:
    valid_locations = [line for line in source if regex.findall(regex_valid_location, line)]
    print(valid_locations[1])

        # with open("locations.json", "w") as new_db:
        # print(locations)
        # for line in source:
        #     name = regex.findall(regex_location_name, line)
        #     print(name)
        #     new_db.write("\n---------------------------------------------\n")
        #     new_db.write(name[0])