py -m venv .venv
.venv\Scripts\pip.exe install -r requirements\dev.txt

curl -L https://github.com/protocolbuffers/protobuf/releases/download/v3.20.1/protoc-3.20.1-win64.zip > protobuf.zip
mkdir deps\protobuf
tar -xf protobuf.zip -C deps\protobuf
del /Q protobuf.zip