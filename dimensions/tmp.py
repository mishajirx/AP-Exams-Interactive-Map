import csv

# Replace this with the actual filename or use StringIO if reading from a string
filename = "subject_dim_202402041458.csv"

my_dict = {}

with open(filename, mode='r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    next(reader)
    for row in reader:
        subject_id = row[0]
        subject_name = row[1]
        # subject_area = row[2]  # we won’t use subject_area in the dictionary
        hierarchy_level = row[3]

        # Build the dictionary entry: "Subject Name": ("subject_id", "hierarchy_level")
        my_dict[subject_name] = (int(subject_id), int(hierarchy_level))

print(my_dict)
