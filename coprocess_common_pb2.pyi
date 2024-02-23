from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HookType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknown: _ClassVar[HookType]
    Pre: _ClassVar[HookType]
    Post: _ClassVar[HookType]
    PostKeyAuth: _ClassVar[HookType]
    CustomKeyCheck: _ClassVar[HookType]
    Response: _ClassVar[HookType]
Unknown: HookType
Pre: HookType
Post: HookType
PostKeyAuth: HookType
CustomKeyCheck: HookType
Response: HookType

class StringSlice(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, items: _Optional[_Iterable[str]] = ...) -> None: ...
