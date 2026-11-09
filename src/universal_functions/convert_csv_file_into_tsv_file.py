import csv
from pathlib import Path

def convert_csv_file_into_tsv_file(path_to_csv_file,
                                   path_to_tsv_file=None,
                                   tab_amount="\t"):
    print(tab_amount, "convert_csv_file_into_tsv_file")
    tab_amount += "\t"

    path_to_csv_file = Path(path_to_csv_file)

    if path_to_tsv_file is None:
        path_to_tsv_file = path_to_csv_file.with_suffix(".tsv")
    else:
        path_to_tsv_file = Path(path_to_tsv_file)

    print(tab_amount, "path_to_csv_file =", path_to_csv_file)
    print(tab_amount, "path_to_tsv_file =", path_to_tsv_file)

    if not path_to_csv_file.exists():
        print(tab_amount, "ERROR: convert_csv_file_into_tsv_file: CSV file does not exist.")
        exit()

    with open(path_to_csv_file, newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    with open(path_to_tsv_file, "w", newline="", encoding="utf-8") as tsv_file:
        writer = csv.writer(tsv_file, delimiter="\t")
        writer.writerows(rows)

    print(tab_amount, "rows_converted =", len(rows))
    print(tab_amount, "tsv file created")

    return str(path_to_tsv_file)

if __name__ == "__main__":
    print("src/universal_functions/spreadsheet_stuff/convert_csv_file_into_tsv_file.py --> start")
    tab_amount = "\t"



    print("src/universal_functions/spreadsheet_stuff/convert_csv_file_into_tsv_file.py --> end")