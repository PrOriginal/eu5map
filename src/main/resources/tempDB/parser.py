import json
import os
import re as regex

regex_valid_location = "^.+material.+$" #r"(\w+)\s*=\s*\{([^}]+)\}"
regex_location_name = "^\\w+"
regex_location_params = "(\w+)\s*=\s*([\w\d.]+)"

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

def get_valid_locations(file_name):
    with open(file_name) as f:
        locations = [line for line in f if regex.findall(regex_valid_location, line)]
    return locations

def format_location_name(name):
    return name.replace("_"," ").title()

def gather_location_params(locations):
    locations_objects = []
    for location in locations:
        name = regex.search(regex_location_name, location).group()
        name = format_location_name(name)
        print(name)
        params = dict(regex.findall(regex_location_params,location))
        locations_objects.append(Location(name=name, **params))
    return locations_objects

def write_locations_to_json(locations, file_name):
    with open(file_name, "w") as f:
        f.write(json.dumps([location.to_dict() for location in locations], indent=2, ensure_ascii=False))

raw_data = get_valid_locations("location_templates.txt")
locations_obj = gather_location_params(raw_data)
if os.path.exists("locations.json"):
    os.remove("locations.json")
write_locations_to_json(locations_obj, "locations.json")
#-----------------------------------------------------------------------------------------------------------

# with open("location_templates.txt") as f:
#     valid_locations = [line for line in f if regex.findall(regex_valid_location, line)]
#
# for location in valid_locations:
#     location_name = regex.search(regex_location_name, location).group()
#     location_name = location_name.replace("_"," ")
#     print(location_name)
#     params = dict(regex.findall(regex_location_params,location))
#     locations_objects.append(Location(name=location_name, **params))
#
# if os.path.exists("locations.json"):
#     os.remove("locations.json")
#
# with open("locations.json", "w") as f:
#         f.write(json.dumps([location.to_dict() for location in locations_objects]))
