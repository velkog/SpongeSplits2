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


# lint:
#                         $(ENVX) mypy $(PY_SRC)/ --ignore-missing-imports --strict
#                         $(ENVX) pycln $(PY_SRC)/ --check
#                         $(ENVX) isort $(PY_SRC)/ --diff
#                         $(ENVX) black $(PY_SRC)/ --check

# format:
#                         $(ENVX) black $(PY_SRC)/
#                         $(ENVX) pycln $(PY_SRC)/ -a
#                         $(ENVX) isort $(PY_SRC)/