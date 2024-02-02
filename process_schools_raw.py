from json import dumps, loads
from pprint import pprint

from openpyxl import load_workbook
from config import GoogleMaps_API
from requests import get


def process_school(district_school: str) -> tuple[float, float]:
    # district, school = district_school.split(" - ")
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


input_file = "ap_performance_mod3.xlsx"
output_file = "ap_performance_mod3.xlsx"

# load excel file
workbook = load_workbook(filename=input_file)

# open workbook
sheet = workbook.active

results = [

]

# Get school coordinates
for i in range(229, 242):
    lat, lng = process_school(sheet[f"A{i}"].value)
    print(lat, lng)
    sheet[f'C{i}'] = lat
    sheet[f'D{i}'] = lng

# Replace all percentage periods with commas
for i in range(2, 339 + 1):
    sheet[f'K{i}'] = ",".join(str(sheet[f'K{i}'].value).split('.'))
    sheet[f'L{i}'] = ",".join(str(sheet[f'L{i}'].value).split('.'))

# Remove commas in number of test takers

for i in range(2, 339 + 1):
    sheet[f'E{i}'] = "".join(str(sheet[f'E{i}'].value).split(','))

# save the file
workbook.save(filename=output_file)
