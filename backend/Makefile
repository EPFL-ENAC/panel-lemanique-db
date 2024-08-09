.PHONY: create_tables drop_tables ingest_wave2 ingest_data

drop_tables:
	python3 database/drop_tables.py

create_tables:
	python3 database/create_tables.py

reset_tables: drop_tables create_tables
