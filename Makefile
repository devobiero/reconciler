.PHONY: install
install:
	python3 -m venv venv && . venv/bin/activate && pip install -r requirements-dev.txt

.PHONY: run
run:
	. venv/bin/activate && ./csv_reconciler -s ./data/source.csv -t ./data/target.csv -o ./data/reconciliation_report.csv

.PHONY: lint
lint:
	. venv/bin/activate && pre-commit run --all-files

.PHONY: typing
typing:
	. venv/bin/activate && mypy src tests

.PHONY: test
test:
	pytest

.PHONY: ci
ci: lint typing test
