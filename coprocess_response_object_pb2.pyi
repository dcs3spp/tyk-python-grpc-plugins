from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseObject(_message.Message):
    __slots__ = ("status_code", "raw_body", "body", "headers", "multivalue_headers")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    RAW_BODY_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    MULTIVALUE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    raw_body: bytes
    body: str
    headers: _containers.ScalarMap[str, str]
    multivalue_headers: _containers.RepeatedCompositeFieldContainer[Header]
    def __init__(self, status_code: _Optional[int] = ..., raw_body: _Optional[bytes] = ..., body: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., multivalue_headers: _Optional[_Iterable[_Union[Header, _Mapping]]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ("key", "values")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
