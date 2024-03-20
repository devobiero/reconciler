.PHONY: install
install:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements-dev.txt

.PHONY: run
run:
	source venv/bin/activate && ./csv_reconciler -s ./data/source.csv -t ./data/target.csv -o ./data/reconciliation_report.csv

.PHONY: lint
lint:
	source venv/bin/activate && pre-commit run --all-files

.PHONY: typing
typing:
	source venv/bin/activate && mypy src tests

.PHONY: test
test:
	pytest

.PHONY: ci
ci: lint typing test
