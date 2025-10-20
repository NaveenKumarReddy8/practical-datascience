marimo-server:
	uv run marimo edit practical_datascience.py --port 8080 --no-token

build-docs:
	./create_docs.sh

lint:
	uv run ruff check --fix practical_datascience.py
	uv run ruff format practical_datascience.py