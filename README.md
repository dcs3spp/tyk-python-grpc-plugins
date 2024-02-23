# Python gRPC Plugin for Tyk Gateway

This repository implements a basic Tyk gRPC plugin that listens for requests received from the Tyk Gateway and outputs
the incoming request payload in JSON format. 

To accomplish this a gRPC server has been implemented that complies with Tyk's [ServiceDispatcher](https://github.com/TykTechnologies/tyk/blob/master/coprocess/proto/coprocess_object.proto)
service.

The repository contains the following files:
- protobuf (.proto) files provided by [Tyk](https://github.com/TykTechnologies/tyk/blob/master/coprocess/proto). These specify the expected interface for the gRPC Server and supporting types.
- Python bindings (coprocess_*.py) contain the supporting data structures generated by *protoc* to implement a Tyk gRPC server tht implements the SrviceDispatcher.
- Python type hints (coprocess_*.pyi) are included with the generated python classes, to enable autocompletion in IDEs.
- File tyk_async_server.py contains the implementation of a Python gRPC server that implements the [ServiceDispatcher](https://github.com/TykTechnologies/tyk/blob/master/coprocess/proto/coprocess_object.proto) interface.

## Prerequisites

### 3rd Party Tools
- [grpcurl](https://github.com/fullstorydev/grpcurl) - gRPC client CLI
- [poetry](https://python-poetry.org/) - Python dependency management CLI
- [make](https://www.gnu.org/software/make/) - CLI used to build and run the gRPC server
- [Python 3.12](https://www.python.org/downloads/release/python-3120/?ref=upstract.com)

### Python Dependencies
- [grpcio](https://grpc.io/) - Required for generating the Python bindings.
- [grpc-reflection](https://github.com/grpc/grpc/blob/master/doc/python/server_reflection.md) - Used to allow server introspection so that endpoints can be listed/called from gRPC clients.
- [protobuf](https://googleapis.dev/python/protobuf/latest/) - The protobuf API for Python.


## Quickstart - Running The Server
1. [Install](https://python-poetry.org/docs/#installation) Poetry
2. Run the gRPC server by issuing the following command: `make run`
3. In a separate terminal window issue the following command: `make dispatch`

The supporting *Makefile* rules are:

1. **build**: Generate the supporting Python classes and type hints to enable the development of a gRPCServer for the *Dispatcher* interface
2. **clean**: Remove the supporting Python classes and type hints
3. **serve**: Start the gRPC server to serve the plugins
4. **dispatch**: Use *grpcurl* to send a test *Dispatch* request to the gRPC server
5. **dispatch_event**: Use *grpcurl* to send a test *DispatchEvent* to the gRPC server
6. **petstore**: If you have imported a Tyk OAS API based on the pet store [schema](https://petstore3.swagger.io/api/v3/openapi.json) then this will send a fetch request to the *findByStatus* endpoint 

## Configure Tyk Gateway To Serve Plugins Using The gRPC Server

Tyk Gateway needs to be configured with *coprocess* enabled in addition to the URL of the gRPC server.

Within the root of the *tyk.conf* file, add the following:

```json
"coprocess_options": {
  "enable_coprocess":   true,
  "coprocess_grpc_server": "tcp://<host>:<port>"
}
```

Alternatively, the following environment variables can be set:

```bash
TYK_GW_COPROCESSOPTIONS_ENABLECOPROCESS=true
TYK_GW_COPROCESSOPTIONS_COPROCESSGRPCSERVER=tcp://<host>:<port>
```

## Configure Your API To Use The gRPC Plugin

Create a Tyk Classic API or a Tyk OAS API and enable plugins. The plugin driver should be set to *grpc*. 

### Tyk Classic API

The gRPC plugin can be configured within the *classic middleware* section of your API:

```json
 "custom_middleware": {
      "pre": [],
      "post": [],
      "post_key_auth": [],
      "auth_check": {
        "disabled": false,
        "name": "",
        "path": "",
        "require_session": false,
        "raw_body_only": false
      },
      "response": [
        {
          "disabled": false,
          "name": "MyResponseMiddleware",
          "path": "",
          "require_session": false,
          "raw_body_only": false
        }
      ],
      "driver": "grpc",
      "id_extractor": {
        "disabled": false,
        "extract_from": "",
        "extract_with": "",
        "extractor_config": {}
      }
    },
```

The example listed above shows that the plugin driver is configured as *grpc*. A response plugin has been configured
with the name *MyResponseMiddleware*. In this example *require_session* is disabled, which means that session state
relating to the authenticated key/user is not forwarded by the Gateway. Enable this to hav the Gateway forward session state.

### Tyk OAS API

A Tyk OAS API Definition contains the OAS JSON schema with an *x-tyk-api-gateway* section appended.

The gRPC plugin can be configured within the *middleware* section of the *x-tyk-api-gateway* section as shown below:

```json
"x-tyk-api-gateway": {
    "info": {
      "id": "ce6528c0af7b43206b9cf736a5e5d1b4",
      "dbId": "65d5d40a294b1b0001c0972a",
      "orgId": "5e9d9544a1dcd60001d0ed20",
      "name": "Swagger Petstore",
      "state": {
        "active": true
      }
    },
    "upstream": {
      "url": "http://petstore3.swagger.io/api/v3"
    },
    "server": {
      "listenPath": {
        "value": "/",
        "strip": true
      }
    },
    "middleware": {
      "global": {
        "pluginConfig": {
          "driver": "grpc"
        },
        "cors": {
          "enabled": true,
          "maxAge": 24,
          "allowedHeaders": [
            "Accept",
            "Content-Type",
            "Origin",
            "X-Requested-With",
            "Authorization"
          ],
          "allowedOrigins": [
            "*"
          ],
          "allowedMethods": [
            "GET",
            "HEAD",
            "POST"
          ]
        },
        "prePlugin": {
          "plugins": [
            {
              "enabled": true,
              "functionName": "MyPrePluginMiddleware",
              "path": ""
            }
          ]
        }
      }
    }
  }
```

In the listing above, a pre request plugin has been configured within the *middleware* section. This has a function name of
*MyPrePluginMiddleware*. The plugin driver has been configured as *grpc*.

This means that Tyk Gateway will send a request to the gRPC server, with the plugin hook name as *MyPrePluginMiddleware*.

To quickly get started, the Tyk Dashboard can be used to create a Tyk OAS API by importing the infamous pet store OAS
[JSON](https://petstore3.swagger.io/api/v3/openapi.json) schema. Then the [findByStatus](https://petstore3.swagger.io/api/v3/pet/findByStatus?status=available)
endpoint can be used for testing.

## Example Payload Received By The gRPC Server From Tyk Gateway

```json
{
  "hookType": "Pre",
  "hookName": "MyPrePluginMiddleware",
  "request": {
    "headers": {
      "User-Agent": "curl/8.1.2",
      "Host": "localhost:8080",
      "Accept": "*/*"
    },
    "url": "/pet/findByStatus?status=available",
    "params": {
      "status": "available"
    },
    "returnOverrides": {
      "responseCode": -1
    },
    "method": "GET",
    "requestUri": "/pet/findByStatus?status=available",
    "scheme": "http"
  },
  "spec": {
    "bundle_hash": "d41d8cd98f00b204e9800998ecf8427e",
    "OrgID": "5e9d9544a1dcd60001d0ed20",
    "APIID": "ce6528c0af7b43206b9cf736a5e5d1b4"
  }
}
```

## FAQs

### What Is The Tyk gRPC protobuf Service Interface That I Should Implement?

The *Dispatcher* gRPC service and supporting data structures are located within the *coprocess_object.proto* file:

```protobuf
service Dispatcher {

  /**
   * @brief Accepts and returns an \ref Object
   */
  rpc Dispatch (Object) returns (Object) {}

  /**
   * @brief Dispatches an event to the target language
   */
  rpc DispatchEvent (Event) returns (EventReply) {}
}
```

This contains the following methods:
- **Dispatch**: Called by Tyk Gateway for every configured hook on every request.
- **DispatchEvent**: Provides a mechanism for the gRPC server to receive Tyk events.

### How Do I Implement The Python Tyk gRPC Plugin Service?

Firstly, you need to use the *protoc* compiler to generate the supporting Python classes. These classes allow serialisation
of protobuf messages. The *protoc* compiler will also generate a base class for your gRPCServer. This repository contains the
generated Python classes (coprocess_*.py). If you want to remove and regenerate them, issue the following commands:

```bash
make clean
make build
```

Inspect the generated file, *coprocess_object_pb2_grpc.py*. It contains a class named *DispatcherServicer*, listed below:

```python
class DispatcherServicer(object):
    """*
    @brief GRPC server interface

    The server interface that must be implemented by the target language
    """

    def Dispatch(self, request, context):
        """*
        @brief Accepts and returns an \ref Object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DispatchEvent(self, request, context):
        """*
        @brief Dispatches an event to the target language
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
```

Notice that the comments from the protobuf file have been included in the generated Python class.

Finally, write a class that inherits from the *DispatcherServicer* base class, implementing the *Dispatch* and *DispatchEvent*
methods. An example implementation, included in *tyk_async_server.py*, is listed below:

```python
class PythonDispatcher(coprocess_object_pb2_grpc.DispatcherServicer):
    async def Dispatch(
        self, object: coprocess_object_pb2.Object, context: grpc.aio.ServicerContext
    ):
        logging.info("REQUEST START")
        logging.info(MessageToJson(object))
        logging.info("REQUEST END")

        return object

    async def DispatchEvent(
        self, event: coprocess_object_pb2.Event, context: grpc.aio.ServicerContext
    ):
        event = json.loads(event.payload)
        logging.info(f"RECEIVED EVENT: {event}")
        return coprocess_object_pb2.EventReply()
```

- The *Dispatch* method uses the *MessageToJson* function provided, by Google's protobuf API, to output the message
received from the Gateway in JSON format.
- The *DispatchEvent* method outputs the JSON payload of an event for dispatch. 

## Further Questions
- It looks like a gRPC server is global to all endpoints. Can we configure different gRPC servers for different APIs?
- Can we configure different API endpoints to serve plugins from different GRPC servers? I am aware of grpc-proxy, but can plugins be served from different API endpoints on different gRPC servers?

## Protobuf Issues
Google Python Protobuf tooling does not generate relative import statements.
https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-1648982084
