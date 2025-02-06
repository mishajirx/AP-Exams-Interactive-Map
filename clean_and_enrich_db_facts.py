import decimal
from collections import deque

import psycopg2
from config import ConnectionString
from config import SubjectsHierarchy

conn = psycopg2.connect(ConnectionString)

q = conn.cursor()

q.execute("SELECT \"School Code\" FROM school_dim")

year: int
school_code: int


def extract_grades() -> dict:
    global school_code, year
    q.execute(f"""
        SELECT subject_id, "Score=1","Score=2","Score=3","Score=4","Score=5"  
        FROM ap_performance_facts WHERE \"School Code\" = {school_code} AND \"year\" = {year}""")

    grades = q.fetchall()
    result = {}
    for row in grades:
        result[row[0]] = row[1:]
    # print(result)
    return result


def upload_grades(subject_id: int, grades: list[5]):
    global school_code, year
    q.execute(f"""
        UPDATE ap_performance_facts
        SET "Score=1"={grades[0]},"Score=2"={grades[1]},"Score=3"={grades[2]},"Score=4"={grades[3]},"Score=5"={grades[4]}
        WHERE subject_id = {subject_id} AND \"School Code\" = {school_code} AND \"year\" = {year}""")


def update_characteristics_based_on_grades(subject_id: int, grades: list[5]):
    global school_code, year
    q.execute(f"""
            UPDATE ap_performance_facts
            SET "% Score 3-5"={100 * sum(grades[2:5]) / sum(grades[0:5])}, 
            "% Score 1-2"={100 * sum(grades[0:2]) / sum(grades[0:5])}
            WHERE subject_id = {subject_id} AND \"School Code\" = {school_code} AND \"year\" = {year}""")


def extract_years():
    global school_code, year
    q.execute(f""" 
    select distinct \"year\" from ap_performance_facts WHERE \"School Code\" = {school_code}""")
    years = q.fetchall()
    result = set()
    for row in years:
        result.add(row[0])
    # print(result)
    return result


cnt = 0

for (school_code,) in q.fetchall():
    for year in extract_years():
        print(school_code, cnt)
        cnt += 1
        q.execute(
            f"SELECT subject_id FROM ap_performance_facts WHERE \"School Code\" = {school_code} AND \"year\" = {year}")
        subjects = set([el[0] for el in q.fetchall()])

        q.execute(f"""
                    SELECT subject_id, "Tests Taken" FROM ap_performance_facts WHERE \"School Code\" = {school_code} AND \"year\" = {year}
                    AND (\"% Score 3-5\" + \"% Score 1-2\") = 0 """)
        response = q.fetchall()
        empty_subjects = set([el[0] for el in response])
        tests_taken_empty_subjects = {}
        for el in response:
            tests_taken_empty_subjects[el[0]] = el[1]

        if 0 in empty_subjects:
            q.execute(f"""
                            DELETE FROM ap_performance_facts WHERE \"School Code\" = {school_code} AND \"year\" = {year}""")
            continue

        queue = deque([0])
        known_grades_database = extract_grades()
        while queue:
            u = queue.popleft()

            if u not in subjects:
                continue

            # Retrieve total grades for a specific subject hierarchy node
            total_grades = known_grades_database[u]

            # Initialize list to accumulate grades for known subjects (5 categories of grades)
            known_grades = [0] * 5

            # Calculate grades for known subjects in the current hierarchy node
            # Filter subjects to only include known ones (exclude empty subjects)
            known_subtree = (SubjectsHierarchy[u] & (subjects - empty_subjects))
            for v in known_subtree:
                v_grades = known_grades_database[v]
                for ind in range(5):
                    known_grades[ind] += v_grades[ind]
            left_grades = [total_grades[ind] - known_grades[ind] for ind in range(5)]
            empty_subtree = SubjectsHierarchy[u] & empty_subjects
            # Calculate the total number of tests taken for all unrepresented subjects
            total_empty_tests = 0
            for v in empty_subtree:
                total_empty_tests += tests_taken_empty_subjects[v]
            total_empty_tests = decimal.Decimal(total_empty_tests)
            # Distribute remaining grades proportionally among unrepresented subjects
            for v in empty_subtree:
                # Calculate grades proportion for each category based on tests taken for each
                # unrepresented subject
                v_grades = [left_grades[i] * (tests_taken_empty_subjects[v] / total_empty_tests) for i
                            in range(5)]
                # Update known grades database for the unrepresented subject with newly calculated
                # grades
                known_grades_database[v] = v_grades
                # Upload grades for the specific school and subject
                upload_grades(v, v_grades)
                # Update school characteristics based on the new grades
                update_characteristics_based_on_grades(v, v_grades)

            # Add all child nodes (represented and unrepresented subjects) to the processing queue
            for v in SubjectsHierarchy[u] & subjects:
                queue.append(v)

conn.commit()
conn.close()
