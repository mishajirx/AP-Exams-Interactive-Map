import csv
from json import dumps, loads
from pprint import pprint
from config import SubjectToID
import psycopg2
from openpyxl import load_workbook
from config import ConnectionString

conn = psycopg2.connect(ConnectionString)

q = conn.cursor()

common_id = 0

# SY  ;DIST_CODE   ;DIST_NAME        ;ORG_CODE     ;ORG_NAME     ;ORG_TYPE	SUBJ_CAT	SUBJ	STUGRP	TESTS_TAKEN	SCORE_1	SCORE_2	SCORE_3	SCORE_4	SCORE_5	PCT_1_2	PCT_3_5
# "id";"subject_id";"hierarchy_level";"School Code";
# "Tests Taken";"Score=1";"Score=2";"Score=3";"Score=4";"Score=5";"% Score 1-2";"% Score 3-5";
# "Year"

query = f"SELECT DISTINCT \"School Code\" FROM postgres.public.school_dim"
q.execute(query)
org_id_list = [el[0] for el in q.fetchall()]

input_file = f"../Facts/ap_performance_whole.csv"

csv_file = open(input_file)
reader = csv.reader(csv_file, delimiter=",")
print(next(reader))

record_id = 0

fields = ["id", "subject_id", "hierarchy_level", "School Code", "Tests Taken", "Score=1", "Score=2", "Score=3",
          "Score=4", "Score=5", "% Score 1-2", "% Score 3-5", "Year"]

marked = set()
for row in reader:
    year, d_id, d_name, org_id, org_name, org_type, subj_cat, subj, studgrp, *stats = row
    # "Tests Taken";"Score=1";"Score=2";"Score=3";"Score=4";"Score=5";"% Score 1-2";"% Score 3-5";
    # len(_) = 8
    if studgrp != "All Students":
        continue
    if org_type != "School":
        continue
    if int(org_id) not in org_id_list:
        if int(org_id) in marked:
            continue
        marked.add(int(org_id))
        print(org_name, org_id)
        org_name = org_name.replace('\'', '')
        d_name = d_name.replace('\'', '')
        row = (org_id, org_name, d_name, 0, 0)
        query = f"INSERT INTO school_dim VALUES {row}"
        print(query)
        q.execute(query)

conn.commit()
conn.close()

csv_file.close()
