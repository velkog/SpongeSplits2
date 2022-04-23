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

# protoc --plugin=protoc-gen-mypy=path/to/protoc_gen_mypy.bat --python_out=output/location --mypy_out=output/location

# .\deps\protoc-3.19.1-win64\bin\protoc.exe --plugin=".\deps\mypy-protobuf\mypy_protobuf\protoc_gen_mypy.bat" -I=".\autosplit\network\message\protobuf\" --python_out=".\autosplit\network\message\" --mypy_out=".\autosplit\network\message\" .\autosplit\network\message\protobuf\frame.proto .\autosplit\network\message\protobuf\pineapple_result.proto


# "deps/protoc-3.19.1-win64/bin/protoc.exe" --plugin=deps/mypy-protobuf/mypy_protobuf/protoc_gen_mypy.bat --proto_path=autosplit/network/message/protobuf/ --python_out=autosplit/network/message/ --mypy_out=autosplit/network/message/ autosplit/network/message/protobuf/frame.proto autosplit/network/message/protobuf/pineapple_result.proto



# compilea = "{PROTOC} --plugin={MYPY_PROTOC} --proto_path={PROTO_PATH} --python_out={PROTO_OUT} --mypy_out={PROTO_OUT} {PROTO_SRCS}"
# compile = "\"deps/protoc-3.19.1-win64/bin/protoc.exe\" --plugin=deps/mypy-protobuf/mypy_protobuf/protoc_gen_mypy.bat --proto_path=kogger_splitter/network/message/protobuf/ --python_out=kogger_splitter/network/message/ --mypy_out=kogger_splitter/network/message/"
# lint_mypy = "mypy autosplit/"
# lint_pycln = "pycln autosplit/ --check"
# lint_isort ="isort autosplit/ --diff"


# [tool.taskipy.variables]
# PROTOC = "\"deps/protoc-3.19.1-win64/bin/protoc.exe\""
# MYPY_PROTOC = "deps/mypy-protobuf/mypy_protobuf/protoc_gen_mypy.bat"
# PROTO_PATH = "kogger_splitter/network/message/protobuf/"
# PROTO_OUT = "kogger_splitter/network/message/"
# PROTO_SRCS = "kogger_splitter/network/message/protobuf/frame.proto kogger_splitter/network/message/protobuf/pineapple_result.proto"
