import coprocess_mini_request_object_pb2 as _coprocess_mini_request_object_pb2
import coprocess_response_object_pb2 as _coprocess_response_object_pb2
import coprocess_session_state_pb2 as _coprocess_session_state_pb2
import coprocess_common_pb2 as _coprocess_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Object(_message.Message):
    __slots__ = ("hook_type", "hook_name", "request", "session", "metadata", "spec", "response")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SpecEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOOK_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    hook_type: _coprocess_common_pb2.HookType
    hook_name: str
    request: _coprocess_mini_request_object_pb2.MiniRequestObject
    session: _coprocess_session_state_pb2.SessionState
    metadata: _containers.ScalarMap[str, str]
    spec: _containers.ScalarMap[str, str]
    response: _coprocess_response_object_pb2.ResponseObject
    def __init__(self, hook_type: _Optional[_Union[_coprocess_common_pb2.HookType, str]] = ..., hook_name: _Optional[str] = ..., request: _Optional[_Union[_coprocess_mini_request_object_pb2.MiniRequestObject, _Mapping]] = ..., session: _Optional[_Union[_coprocess_session_state_pb2.SessionState, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., spec: _Optional[_Mapping[str, str]] = ..., response: _Optional[_Union[_coprocess_response_object_pb2.ResponseObject, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: str
    def __init__(self, payload: _Optional[str] = ...) -> None: ...

class EventReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
