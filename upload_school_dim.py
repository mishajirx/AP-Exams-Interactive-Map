import psycopg2
from openpyxl import load_workbook
from config import ConnectionString

conn = psycopg2.connect(ConnectionString)

q = conn.cursor()

wb = load_workbook(filename="dimensions/school_dim.xlsx")
sh = wb.active

is_first = True
for row in sh.values:
    if is_first:
        is_first = False
        continue
    query = f"INSERT INTO dim_schools VALUES {row}"
    print(query)
    q.execute(query)

conn.commit()
conn.close()
