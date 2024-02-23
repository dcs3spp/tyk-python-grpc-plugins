import coprocess_return_overrides_pb2 as _coprocess_return_overrides_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MiniRequestObject(_message.Message):
    __slots__ = ("headers", "set_headers", "delete_headers", "body", "url", "params", "add_params", "extended_params", "delete_params", "return_overrides", "method", "request_uri", "scheme", "raw_body")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SetHeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AddParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ExtendedParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    SET_HEADERS_FIELD_NUMBER: _ClassVar[int]
    DELETE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    ADD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DELETE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RETURN_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_URI_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    RAW_BODY_FIELD_NUMBER: _ClassVar[int]
    headers: _containers.ScalarMap[str, str]
    set_headers: _containers.ScalarMap[str, str]
    delete_headers: _containers.RepeatedScalarFieldContainer[str]
    body: str
    url: str
    params: _containers.ScalarMap[str, str]
    add_params: _containers.ScalarMap[str, str]
    extended_params: _containers.ScalarMap[str, str]
    delete_params: _containers.RepeatedScalarFieldContainer[str]
    return_overrides: _coprocess_return_overrides_pb2.ReturnOverrides
    method: str
    request_uri: str
    scheme: str
    raw_body: bytes
    def __init__(self, headers: _Optional[_Mapping[str, str]] = ..., set_headers: _Optional[_Mapping[str, str]] = ..., delete_headers: _Optional[_Iterable[str]] = ..., body: _Optional[str] = ..., url: _Optional[str] = ..., params: _Optional[_Mapping[str, str]] = ..., add_params: _Optional[_Mapping[str, str]] = ..., extended_params: _Optional[_Mapping[str, str]] = ..., delete_params: _Optional[_Iterable[str]] = ..., return_overrides: _Optional[_Union[_coprocess_return_overrides_pb2.ReturnOverrides, _Mapping]] = ..., method: _Optional[str] = ..., request_uri: _Optional[str] = ..., scheme: _Optional[str] = ..., raw_body: _Optional[bytes] = ...) -> None: ...
