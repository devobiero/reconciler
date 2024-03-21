import csv
import pytest

from src.csv_handler import CSVHandler

filename = "test.csv"

test_data = [
    {
        "ID": "001",
        "Name": "John Doe",
        "Date": "2023-01-01",
        "Amount": "100.00",
    },
    {
        "ID": "002",
        "Name": "John Doe",
        "Date": "2023-01-01",
        "Amount": "200.50",
    },
    {
        "ID": "003",
        "Name": "Robert Brown",
        "Date": "2023-01-03",
        "Amount": "300.75",
    },
]


@pytest.fixture
def csv_handler():
    # Setup - create a CSV file with test data
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["ID", "Name", "Date", "Amount"]
        )
        writer.writeheader()
        for row in test_data:
            writer.writerow(row)

    # Provide the CSVHandler instance with the test file
    handler = CSVHandler(filename)
    yield handler

    # Teardown - delete the test file
    import os

    os.remove(filename)


def test_read(csv_handler):
    # Test reading from the CSV file
    data = csv_handler.read()
    assert data == test_data


def test_write(csv_handler):
    # Test writing to the CSV file
    new_data = [
        [],  # absent_in_target
        [],  # absent_in_source
        [
            {
                "Type": "Discrepancy",
                "Record Identifier": "002",
                "Field": "Name",
                "Source Value": "Janet",
                "Target Value": "Jane",
            }
        ],
    ]
    csv_handler.write(new_data)

    # Read the file to verify the written data
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        written_data = list(reader)

    # Check if the data is written correctly
    assert written_data == [
        ["Type", "Record Identifier", "Field", "Source Value", "Target Value"],
        ["Discrepancy", "002", "Name", "Janet", "Jane"],
    ]


def test_handle_file_not_found(tmp_path):
    # Create CSVHandler instance with a non-existent file
    handler = CSVHandler(tmp_path / "nonexistent_file.csv")
    data = handler.read()
    assert data == []
