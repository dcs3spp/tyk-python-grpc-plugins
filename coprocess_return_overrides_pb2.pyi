from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReturnOverrides(_message.Message):
    __slots__ = ("response_code", "response_error", "headers", "override_error", "response_body")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_FIELD_NUMBER: _ClassVar[int]
    response_code: int
    response_error: str
    headers: _containers.ScalarMap[str, str]
    override_error: bool
    response_body: str
    def __init__(self, response_code: _Optional[int] = ..., response_error: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., override_error: bool = ..., response_body: _Optional[str] = ...) -> None: ...
