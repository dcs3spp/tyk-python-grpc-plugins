build:
	poetry run python -m grpc_tools.protoc \
    	--proto_path=. \
      	--python_out=. \
    	--grpc_python_out=. \
    	--pyi_out=. \
    	*.proto

clean:
	rm coprocess_*.py
	rm coprocess_*.pyi

serve:
	poetry run python -m tyk_async_server

dispatch:
	grpcurl -plaintext -d '{}' localhost:50051 coprocess.Dispatcher/Dispatch

dispatch_event:
	grpcurl -plaintext -d '{"payload": "{\"event\": \"test\"}"}' localhost:50051 coprocess.Dispatcher/DispatchEvent

petstore:
	curl -L http://localhost:8080/pet/findByStatus?status=available
