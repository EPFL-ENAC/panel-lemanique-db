.PHONY: create_tables drop_tables

drop_tables:
	python3 panel_lemanique_db/drop_tables.py

create_tables:
	python3 panel_lemanique_db/create_tables.py
