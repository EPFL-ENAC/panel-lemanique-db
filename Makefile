.PHONY: clean preprocess_data populate_database reset_tables

clean:
	cd data_preprocessing && make $@

preprocess_data:
	cd data_preprocessing && make $@

create_tables:
	cd backend && make $@

reset_tables:
	cd backend && make $@

ingest_wave2:
	python3 -m backend.data_ingestion.ingest_wave2

ingest_data: ingest_wave2

run_api:
	uvicorn backend.app.main:app --reload
