import csv


class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> list[dict[str, str]]:
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]

            return data
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return []

    def write(self, data):
        absent_in_target, absent_in_source, discrepancies = data
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Type",
                    "Record Identifier",
                    "Field",
                    "Source Value",
                    "Target Value",
                ]
            )

            for record in absent_in_target:
                writer.writerow(["Missing in Target", record.id, "", "", ""])

            for record in absent_in_source:
                writer.writerow(["Missing in Source", "", record.id, "", ""])

            for discrepancy in discrepancies:
                writer.writerow(
                    [
                        discrepancy["Type"],
                        discrepancy["Record Identifier"],
                        discrepancy["Field"],
                        discrepancy["Source Value"],
                        discrepancy["Target Value"],
                    ]
                )
