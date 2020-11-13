# --- Velkog ---
#
# Compiling resources for SpongeSplits program

SOURCES 	= autosplit/network/protobuf/

compile:;	for source in $(SOURCES) ; do $(MAKE) -C $$source compile ; done
clean:;		for source in $(SOURCES) ; do $(MAKE) -C $$source clean ; done
format:;	black autosplit/
lint:
			mypy autosplit/ --ignore-missing-imports --strict
			black autosplit/ --check
test:;		python -m unittest discover autosplit
