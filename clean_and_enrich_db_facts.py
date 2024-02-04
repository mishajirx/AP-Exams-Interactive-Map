import decimal
from collections import deque

import psycopg2
from config import ConnectionString
from config import SubjectsHierarchy

conn = psycopg2.connect(ConnectionString)

q = conn.cursor()

q.execute("SELECT \"School Code\" FROM school_dim")


def extract_grades(school_code: int) -> dict:
    q.execute(f"""
        SELECT subject_id, "Score=1","Score=2","Score=3","Score=4","Score=5"  
        FROM ap_performance_facts WHERE \"School Code\" = {school_code}""")

    grades = q.fetchall()
    result = {}
    for row in grades:
        result[row[0]] = row[1:]
    # print(result)
    return result


def upload_grades(school_code: int, subject_id: int, grades: list[5]):
    q.execute(f"""
        UPDATE ap_performance_facts
        SET "Score=1"={grades[0]},"Score=2"={grades[1]},"Score=3"={grades[2]},"Score=4"={grades[3]},"Score=5"={grades[4]}
        WHERE subject_id = {subject_id} AND \"School Code\" = {school_code}""")


def update_characteristics_based_on_grades(school_code: int, subject_id: int, grades: list[5]):
    q.execute(f"""
            UPDATE ap_performance_facts
            SET "% Score 3-5"={100 * sum(grades[2:5]) / sum(grades[0:5])}, 
            "% Score 1-2"={100 * sum(grades[0:2]) / sum(grades[0:5])}
            WHERE subject_id = {subject_id} AND \"School Code\" = {school_code}""")


cnt = 0

for (school_code,) in q.fetchall():
    print(school_code, cnt)
    cnt += 1
    q.execute(f"SELECT subject_id FROM ap_performance_facts WHERE \"School Code\" = {school_code}")
    subjects = set([el[0] for el in q.fetchall()])
    # print(subjects)

    q.execute(f"""
            SELECT subject_id, "Tests Taken" FROM ap_performance_facts WHERE \"School Code\" = {school_code}
            AND (\"% Score 3-5\" + \"% Score 1-2\") = 0 """)
    response = q.fetchall()
    empty_subjects = set([el[0] for el in response])
    tests_taken_empty_subjects = {}
    for el in response:
        tests_taken_empty_subjects[el[0]] = el[1]
    # print(empty_subjects)
    # print(tests_taken_empty_subjects)

    if 0 in empty_subjects:
        q.execute(f"""
                    DELETE FROM ap_performance_facts WHERE \"School Code\" = {school_code}""")
        continue

    queue = deque([0])
    known_grades_database = extract_grades(school_code)
    while queue:
        u = queue.popleft()

        if u not in subjects:
            continue
        # print(u)

        total_grades = known_grades_database[u]
        known_grades = [0] * 5

        known_subtree = (SubjectsHierarchy[u] & (subjects - empty_subjects))
        # print("known_subtree", known_subtree)
        for v in known_subtree:
            # print(v)
            v_grades = known_grades_database[v]
            # print(v_grades)
            for ind in range(5):
                known_grades[ind] += v_grades[ind]

        left_grades = [total_grades[ind] - known_grades[ind] for ind in range(5)]

        empty_subtree = SubjectsHierarchy[u] & empty_subjects
        total_empty_tests = 0
        for v in empty_subtree:
            total_empty_tests += tests_taken_empty_subjects[v]
        total_empty_tests = decimal.Decimal(total_empty_tests)
        # print("empty_subtree", empty_subtree)
        # print("total", sum(total_gra
        # des), total_grades)
        # print("known", sum(known_grades), known_grades)
        # print("left", sum(left_grades), left_grades)

        for v in empty_subtree:
            # print((tests_taken_empty_subjects[v], total_empty_tests))
            v_grades = [left_grades[i] * (tests_taken_empty_subjects[v] / total_empty_tests) for i in range(5)]
            # print(v_grades)
            known_grades_database[v] = v_grades
            upload_grades(school_code, v, v_grades)
            update_characteristics_based_on_grades(school_code, v, v_grades)

        for v in SubjectsHierarchy[u] & subjects:
            queue.append(v)

conn.commit()
conn.close()
