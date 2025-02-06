import csv
from openpyxl import Workbook

# SUBJECTS, FACTS, SCHOOLS
MODE = "SUBJECTS"

def csv_to_xlsx(csv_filename, xlsx_filename, delimiter=';'):
    """
    Converts a CSV file to an XLSX file using openpyxl.

    :param csv_filename: Path to the input CSV file.
    :param xlsx_filename: Path to the output XLSX file.
    :param delimiter: Delimiter used in the CSV file (default ';').
    """
    # Create a new workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    if MODE == "SUBJECTS":
        ws.title = 'NewSubjects'
    elif MODE == "FACTS":
        ws.title = "NewFacts"

    # Open the CSV file and read it with the specified delimiter
    with open(csv_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter)

        # Append each row to the active worksheet
        row = next(reader)
        ws.append(row)

        cnt = 0
        for row in reader:
            row = list(row)
            print(row)
            if MODE == "FACTS":
                for j in range(5, 12):
                    row[j] = str(round(float(row[j]), 3))
                    row[j] = row[j].replace('.', ',')
            ws.append(row)
            print(cnt)

    # Save the workbook to the XLSX file
    wb.save(xlsx_filename)


if __name__ == "__main__":
    # Example usage:
    input_csv = "dimensions/subject_dim_202502052137.csv"
    output_xlsx = "dimensions/subject_dim_202502052137.xlsx"
    csv_to_xlsx(input_csv, output_xlsx)
    print(f"Converted '{input_csv}' to '{output_xlsx}' successfully.")
