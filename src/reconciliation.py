from datetime import date
from pydantic import BaseModel, ValidationError


class Record(BaseModel):
    """
    A model representing a record entry to ensure
    that attributes are of the correct type.
    """

    id: str
    name: str
    date: date
    amount: float


class Reconciler:
    def __init__(
        self,
        source_data: list[dict[str, str]],
        target_data: list[dict[str, str]],
    ):
        self.source_data = self.__validate(source_data)
        self.target_data = self.__validate(target_data)
        self.absent_in_target: list[Record] = []
        self.absent_in_source: list[Record] = []
        self.discrepancies: list[str] = []

    def __validate(self, lines) -> list[Record]:
        """Verify that the records satisfy the structure defined."""
        records = []
        for item in lines:
            try:
                records.append(
                    Record(
                        id=item["ID"],
                        name=item["Name"],
                        date=item["Date"],
                        amount=item["Amount"],
                    )
                )
            except ValidationError as e:
                print("Record failed validation check, reason: ", e)

        return records

    def compare(self):
        """
        Compares records between the source and target datasets.
        It identifies records that are present in the source
        but missing in the target (and vice versa). Additionally, it detects
        discrepancies between corresponding records in both datasets,
        highlighting any differences in field values.
        """
        source_ids = set(record.id for record in self.source_data)
        target_ids = set(record.id for record in self.target_data)

        self.absent_in_target = [
            record
            for record in self.source_data
            if record.id not in target_ids
        ]
        self.absent_in_source = [
            record
            for record in self.target_data
            if record.id not in source_ids
        ]

        for source in self.source_data:
            for target in self.target_data:
                if source.id == target.id:
                    for key, val in dict(source).items():
                        target_val = dict(target)[key]
                        if key != "id" and val != target_val:
                            self.discrepancies.append(
                                {
                                    "Type": "Field Discrepancy",
                                    "Record Identifier": source.id,
                                    "Field": key,
                                    "Source Value": val,
                                    "Target Value": target_val,
                                }
                            )
                    break
