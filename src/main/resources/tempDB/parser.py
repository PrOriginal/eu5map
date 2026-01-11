import json
import re as regex

REGEX_VALID_LOCATION = r"^.+material.+$"
REGEX_LOCATION_NAME = r"^\w+"
REGEX_LOCATION_PARAMS = r"(\w+)\s*=\s*([\w\d.]+)"

RAW_DATA = "location_templates.txt"
ORGANIZED_DATA = "locations.json"

class Location:
    def __init__(self,name,**kwargs):
        self.name = format_text(name)
        self.topography = format_text(kwargs.get("topography"))
        self.vegetation = format_text(kwargs.get("vegetation"))
        self.climate = format_text(kwargs.get("climate"))
        self.religion = format_text(kwargs.get("religion"))
        self.culture = format_text(kwargs.get("culture"))
        self.raw_material = format_text(kwargs.get("raw_material"))
        self.modifier = format_text(kwargs.get("modifier"))
        self.natural_harbor_suitability = float(kwargs.get("natural_harbor_suitability", 0))

    def to_dict(self):
        return self.__dict__

def get_valid_locations(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        locations = [line for line in f if regex.findall(REGEX_VALID_LOCATION, line)]
    return locations

def format_text(text):
    if text:
        return text.replace("_"," ").title()
    else:
        return None

def gather_location_params(locations):
    locations_objects = []
    for location in locations:
        name = regex.search(REGEX_LOCATION_NAME, location).group()
        params = dict(regex.findall(REGEX_LOCATION_PARAMS,location))
        locations_objects.append(Location(name=name, **params))
    return locations_objects

def write_locations_to_json(locations, file_name):
    with open(file_name, "w") as f:
        f.write(json.dumps([location.to_dict() for location in locations], indent=2, ensure_ascii=False))
        print(f"Data successfully saved to {file_name}")

def main():
    try:
        print("Reading data...")
        valid_locs = get_valid_locations(RAW_DATA)
        print(f"{len(valid_locs)} valid locations found")

        print("Processing parameters and creating objects...")
        locations_obj = gather_location_params(valid_locs)
        print(f"Successfully created {len(locations_obj)} 'Location' objects")

        print("Saving to JSON...")
        write_locations_to_json(locations_obj, ORGANIZED_DATA)

    except Exception as e:
        print(f"Unexpected error: {e}")

main()