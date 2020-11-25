# --- Velkog ---
#
# Makefile for compiling protobuf files used as payloads within the
# asynchronous message queue protocol.

PXX			= protoc
SRC_DIR		= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DST_DIR		= $(SRC_DIR)	# $(abspath $(MK_PATH)../)
SOURCES 	= $(shell find $(SRC_DIR) -name '*.proto')
OUTPUT		= $(shell find $(DST_DIR) -name '*_pb2.py')

compile:;	$(PXX) -I=$(SRC_DIR) --python_out=$(DST_DIR) $(SOURCES)

clean:;		$(RM) $(OUTPUT)
