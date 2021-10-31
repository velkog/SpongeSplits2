# --- Velkog ---
#
# Compiling resources for SpongeSplits program

PXX		= python3
SOURCE		= autosplit
MAIN		= $(SOURCE)/autosplit.py
SOURCES 	= $(SOURCE)/network/protobuf/


make start:
		compile
		$(PXX) $(MAIN)
compile:;	for source in $(SOURCES) ; do $(MAKE) -C $$source compile ; done
clean:;		for source in $(SOURCES) ; do $(MAKE) -C $$source clean ; done
format:;	poetry run black $(SOURCE)/
lint:
			poetry run mypy $(SOURCE)/ --ignore-missing-imports --strict
			poetry run black $(SOURCE)/ --check
test:;		poetry run python -m unittest discover $(SOURCE)
