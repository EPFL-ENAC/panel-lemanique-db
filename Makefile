.PHONY: clean preprocess_data populate_database reset_tables

clean:
	cd data_preprocessing && make $@

preprocess_data:
	cd data_preprocessing && make $@

reset_tables:
	cd backend && make $@
