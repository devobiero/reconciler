# Reconciliation tool

## Setup

To make a virtual environment and install requirements:

```
$ make install
```

## Usage

To run the tool:

```
make run
```

or

```
./csv_reconciler -s ./data/source.csv -t ./data/target.csv -o ./data/reconciliation_report.csv
```

Check `./data` folder for the reconciliation report.

## Testing

To run unit tests:

```
make test
```

To run linter:

```
make lint
```
