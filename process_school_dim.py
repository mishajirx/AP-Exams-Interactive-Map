from json import dumps, loads
from pprint import pprint

from openpyxl import load_workbook
from config import GoogleMaps_API
from requests import get


def process_school(district_school: str) -> tuple[float, float]:

    school = "%20".join(["Massachusetts"] + (district_school + "School").split())
    print(school)
    query = "https://maps.googleapis.com/maps/api/geocode/json?"
    query += f"address={school}&"
    query += "region=us&"
    query += f"key={GoogleMaps_API}"
    response = loads(get(query).content)
    # pprint(response)
    try:
        coordinates = response['results'][0]['geometry']['location']
        return (coordinates['lat'], coordinates['lng'])
    except:
        print("----ERROR----")
        print(school)
        return (0, 0)


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
    district, school = sheet[f"B{i}"].value.split(" - ")
    sheet[f'C{i}'] = district
    sheet[f'B{i}'] = school

# save the file
workbook.save(filename=output_file)
