# --- Velkog ---
#
# Compiling resources for SpongeSplits program
#
# --- Comand line args ---
#   * env=liux - runs shell commands locally rather than through Windows within WSL
#

VENV			= .venv
WIN_ENV			= bin/activate.ps1
PXX				= $(VENV)/Scripts/python.exe

CMDX			= cmd.exe
PWSHX			= powershell.exe
WINX			= $(PWSHX) -executionpolicy bypass -File $(WIN_ENV) $(VENV)
ENVX			= $(WINX)

SOURCE			= autosplit
MAIN			= $(SOURCE)/app.py

DEPS 			= deps
PROTOC			= $(DEPS)/protobuf/bin/protoc.exe
PROTO_MSG_PATH	= $(SOURCE)/network/message
PROTO_DEFS_PATH	= $(PROTO_MSG_PATH)/protobuf
PROTO_DEFS		= frame.proto pineapple_result.proto

AUTOFLAKE		= autoflake $(SOURCE) -r --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables
BLACK			= black $(SOURCE) --exclude $(PROTO_MSG_PATH)
ISORT			= isort $(SOURCE) --skip $(PROTO_MSG_PATH) --profile black
MYPY			= mypy $(SOURCE) --ignore-missing-imports --strict
TEST			= -m unittest discover $(SOURCE)

ifeq ($(env), linux)
ENVX 			= 
PROTOC 			= protoc
PXX				= python3
MYPY			:= $(MYPY) --exclude $(SOURCE)/system/win
endif

make start:;	$(PXX) $(MAIN)
compile:;		$(ENVX) $(PROTOC) --proto_path=$(PROTO_DEFS_PATH) --python_out=$(PROTO_MSG_PATH) --mypy_out=$(PROTO_MSG_PATH) $(PROTO_DEFS)
clean:;			rm $(PROTO_MSG_PATH)/*_pb2.*
format:
				$(ENVX) $(AUTOFLAKE) --in-place
				$(ENVX) $(ISORT)
				$(ENVX) $(BLACK)
install:;		cmd.exe /c bin/setup.bat
lint:		
				$(ENVX) $(MYPY)
				$(ENVX) $(AUTOFLAKE) --check
				$(ENVX) $(ISORT) --diff
				$(ENVX) $(BLACK) --check
reset:
				rm -rf deps/
				rm -rf .venv/
				rm -rf .mypy_cache/
				find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
setup:;			$(CMDX) /c setup.bat
test:;			$(PXX) $(TEST)

autoflake:;		$(ENVX) $(AUTOFLAKE) --check
black:;			$(ENVX) $(BLACK) --check
isort:;			$(ENVX) $(ISORT) --diff
mypy:;			$(ENVX) $(MYPY)
