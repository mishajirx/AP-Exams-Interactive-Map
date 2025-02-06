from json import loads
from pprint import pprint

import psycopg2
from openpyxl import load_workbook
from requests import get

from config import ConnectionString
from config import GoogleMaps_API

conn = psycopg2.connect(ConnectionString)

q = conn.cursor()


def process_school(district_school: str) -> tuple[float, float]:
    school = "%20".join(["Massachusetts"] + (district_school + "School").split())
    print(school)
    query = "https://maps.googleapis.com/maps/api/geocode/json?"
    query += f"address={school}&"
    query += "region=us&"
    query += f"key={GoogleMaps_API}"
    response = loads(get(query).content)
    try:
        coordinates = response['results'][0]['geometry']['location']
        return (coordinates['lat'], coordinates['lng'])
    except:
        print("----ERROR----")
        print(school)
        return (0, 0)


query = f"SELECT DISTINCT \"School Code\", \"School Name\" FROM postgres.public.school_dim WHERE latitude = 0 AND longtitude = 0"
q.execute(query)
org_id_list = [(el[0], el[1]) for el in q.fetchall()]

for org_id, school_name in org_id_list:
    latitude, longtitude = process_school(school_name)
    print(school_name, latitude, longtitude)
    q.execute(f"""UPDATE
    postgres.public.school_dim
    SET
    latitude = {latitude}, longtitude={longtitude}
    WHERE
    \"School Code\"={org_id}""")

conn.commit()
conn.close()
