"""Python AsyncIO Dispatcher"""

import asyncio
import json
import signal
import logging

import grpc
from google.protobuf.json_format import MessageToJson
from grpc_reflection.v1alpha import reflection
import coprocess_object_pb2_grpc
import coprocess_object_pb2
from coprocess_common_pb2 import HookType


class PythonDispatcher(coprocess_object_pb2_grpc.DispatcherServicer):
    async def Dispatch(
        self, object: coprocess_object_pb2.Object, context: grpc.aio.ServicerContext
    ) -> coprocess_object_pb2.Object:
        logging.info(f"REQUEST\n{MessageToJson(object)}\n")

        if object.hook_type == HookType.Pre:
            logging.info(f"Pre plugin name: {object.hook_name}")
            logging.info(f"Activated Pre Request plugin from API: {object.spec.get('APIID')}")
        elif object.hook_type == HookType.Response:
            logging.info(f"Response plugin name: {object.hook_name}")
            logging.info(f"Activated Response plugin from API: {object.spec.get('APIID')}")

        return object

    async def DispatchEvent(
        self, event: coprocess_object_pb2.Event, context: grpc.aio.ServicerContext
    ) -> coprocess_object_pb2.EventReply:

        event = json.loads(event.payload)
        logging.info(f"RECEIVED EVENT: {event}")
        return coprocess_object_pb2.EventReply()


async def serve() -> None:
    server = grpc.aio.server()

    coprocess_object_pb2_grpc.add_DispatcherServicer_to_server(
        PythonDispatcher(), server
    )
    listen_addr = "[::]:50051"

    SERVICE_NAMES = (
        coprocess_object_pb2.DESCRIPTOR.services_by_name["Dispatcher"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


async def shutdown_server(server) -> None:
    logging.info("Shutting down server...")
    await server.stop(None)


def handle_sigterm(sig, frame) -> None:
    asyncio.create_task(shutdown_server(server))


async def handle_sigint() -> None:
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, loop.stop)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    server = None

    signal.signal(signal.SIGTERM, handle_sigterm)

    try:
        asyncio.get_event_loop().run_until_complete(serve())
        # server = asyncio.run(serve())
    except KeyboardInterrupt:
        pass
