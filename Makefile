build:
	poetry run python -m grpc_tools.protoc \
    	--proto_path=. \
      	--python_out=. \
    	--grpc_python_out=. \
    	--pyi_out=. \
    	*.proto

docker-build:
	docker buildx build -t grpc-example -f Dockerfile .

docker-run:
	docker run --rm --name gtp-example-container grpc-example

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

petstore-auth:
	curl -H "Authorization: eyJvcmciOiI1ZTlkOTU0NGExZGNkNjAwMDFkMGVkMjAiLCJpZCI6IjA4NjM5YTZlOWYyOTQ1YWI4OGQ2ZTgwNzU3ODEzMjNmIiwiaCI6Im11cm11cjY0In0=" -L http://localhost:8080/pet/findByStatus?status=available

jsonrpc:
	curl -X GET http://localhost:8080/extract-json-values-grpc-server/todos
