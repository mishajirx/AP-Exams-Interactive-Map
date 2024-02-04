import psycopg2
from openpyxl import load_workbook

conn = psycopg2.connect("""
    host=rc1a-sfzt3mb3eikmvb7p.mdb.yandexcloud.net
    port=6432
    sslmode=verify-full
    dbname=AP_Perfomance
    user=dba
    password=zrfjvs34!
    target_session_attrs=read-write
""")

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
