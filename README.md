# Reconciliation tool

## Setup

Make a virtual environment and install the requirements:

```
$ make install
python3 -m venv venv && source venv/bin/activate && pip install -r requirements-dev.txt
```

To run the app:

```
make run
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
