from json import dumps, loads
from pprint import pprint

from openpyxl import load_workbook
from config import GoogleMaps_API
from requests import get


def process_school(district: str) -> int:

    district = "%20".join(["Massachusetts"] + district.split())
    print(district)
    query = "https://maps.googleapis.com/maps/api/geocode/json?"
    query += f"address={district}&"
    query += "region=us&"
    query += f"key={GoogleMaps_API}"
    response = loads(get(query).content)
    # pprint(response)
    print(response)
    try:
        coordinates = response['results'][0]['geometry']['location']

    except Exception as e:
        print("----ERROR----")
        print(e)
        print(district)
        return 0


input_file = "dimensions/school_dim.xlsx"
output_file = "dimensions/school_dim_new.xlsx"

# load excel file
workbook = load_workbook(filename=input_file)

# open workbook
sheet = workbook.active

results = [

]

# Get school coordinates
for i in range(2, 340):
    district = sheet[f"C{i}"].value
    sheet[f'F{i}'] = process_school(district)
    break

# save the file
# workbook.save(filename=output_file)
