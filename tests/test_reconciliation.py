from datetime import date

from src.csv_handler import CSVHandler
from src.reconciliation import Reconciler

source_data = CSVHandler("./data/source.csv").read()
target_data = CSVHandler("./data/target.csv").read()
reconciler = Reconciler(source_data, target_data)


def test_validate():
    # Assert validation
    assert len(reconciler.source_data) == 3
    assert isinstance(reconciler.source_data[0].date, date)
    assert reconciler.source_data[0].name == "John Doe"
    assert reconciler.source_data[0].amount == 100.00


def test_compare():
    # Call compare method
    reconciler.compare()

    # Assert results
    assert len(reconciler.absent_in_target) == 1
    assert len(reconciler.absent_in_source) == 1
    assert len(reconciler.discrepancies) == 1
    assert reconciler.absent_in_target[0].id == "003"
    assert reconciler.absent_in_source[0].id == "004"
    assert reconciler.discrepancies[0]["Record Identifier"] == "002"
