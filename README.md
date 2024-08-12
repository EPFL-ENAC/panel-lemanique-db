
[![Project Status](https://img.shields.io/badge/status-under%20development-yellow)](https://github.com/EPFL-ENAC/panel-lemanique-db)
![GitHub License](https://img.shields.io/github/license/EPFL-ENAC/panel-lemanique-db)

# panel-lemanique-db

This repository pre-processes data from the Panel Lémanique, ingests it in a PostgreSQL database, and creates an API enabling using to query the data directly from the database.

## Install

Start by cloning the repository, e.g. using

```bash
git clone git@github.com:EPFL-ENAC/panel-lemanique-db.git
```

### Pre-processing (R)

To set up the pre-processing environment, you need [RStudio](https://posit.co/download/rstudio-desktop/) with the [renv](https://rstudio.github.io/renv/) package installed.

Open the `data_preprocessing/panel-lemanique-db.Rproj` file with RStudio and restore the dependencies from the lockfile using

```r
renv::restore()
```

### Backend (python)

To set up the backend environment, you need [pip](https://pip.pypa.io/en/stable/installation/) or [poetry](https://python-poetry.org/docs/#installation). Then, install the dependencies using one of the following methods

#### pip
```bash
pip install -e backend
```

#### Poetry

 ```bash
 cd backend && poetry install
 ```

## Usage overview

To use the repository, run

```bash
make <rule>
```

where `<rule>` is one of the following rules

* `make preprocess_data`: run the pre-processing step
* `create_tables` creates the tables in the PostgreSQL database, using the SQLAlchemy models
* `reset_tables` drops the tables from the PostgreSQL database before recreating them using `create_tables`
* `ingest_data` ingests the pre-processed data into the PostgreSQL database

**Important**: any interaction with the PostgreSQL database requires an `.env` file, which should contain the host, name and port of the database, as well as the user name and the password. The `.env.example` provides an example of such a file.

## Adding data from a new wave or subproject

1. Add a pre-processing script in `data_preprocessing/`
2. Add a pre-processing rule to `data_preprocessing/Makefile` and include the rule as a dependency of the `preprocess_data` rule
3. Add a data ingestion script in `backend/data_ingestion/`
4. Add a data ingestion rule to `Makefile` and include the rule as a dependency of the `ingest_data` rule.
