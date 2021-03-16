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
format:;	black $(SOURCE)/
lint:
			mypy $(SOURCE)/ --ignore-missing-imports --strict
			black $(SOURCE)/ --check
test:;		python -m unittest discover $(SOURCE)
