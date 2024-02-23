from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessSpec(_message.Message):
    __slots__ = ("url", "methods")
    URL_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    url: str
    methods: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, url: _Optional[str] = ..., methods: _Optional[_Iterable[str]] = ...) -> None: ...

class AccessDefinition(_message.Message):
    __slots__ = ("api_name", "api_id", "versions", "allowed_urls")
    API_NAME_FIELD_NUMBER: _ClassVar[int]
    API_ID_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_URLS_FIELD_NUMBER: _ClassVar[int]
    api_name: str
    api_id: str
    versions: _containers.RepeatedScalarFieldContainer[str]
    allowed_urls: _containers.RepeatedCompositeFieldContainer[AccessSpec]
    def __init__(self, api_name: _Optional[str] = ..., api_id: _Optional[str] = ..., versions: _Optional[_Iterable[str]] = ..., allowed_urls: _Optional[_Iterable[_Union[AccessSpec, _Mapping]]] = ...) -> None: ...

class BasicAuthData(_message.Message):
    __slots__ = ("password", "hash")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    password: str
    hash: str
    def __init__(self, password: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...

class JWTData(_message.Message):
    __slots__ = ("secret",)
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret: str
    def __init__(self, secret: _Optional[str] = ...) -> None: ...

class Monitor(_message.Message):
    __slots__ = ("trigger_limits",)
    TRIGGER_LIMITS_FIELD_NUMBER: _ClassVar[int]
    trigger_limits: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, trigger_limits: _Optional[_Iterable[float]] = ...) -> None: ...

class SessionState(_message.Message):
    __slots__ = ("last_check", "allowance", "rate", "per", "expires", "quota_max", "quota_renews", "quota_remaining", "quota_renewal_rate", "access_rights", "org_id", "oauth_client_id", "oauth_keys", "basic_auth_data", "jwt_data", "hmac_enabled", "hmac_secret", "is_inactive", "apply_policy_id", "data_expires", "monitor", "enable_detailed_recording", "metadata", "tags", "alias", "last_updated", "id_extractor_deadline", "session_lifetime", "apply_policies", "certificate", "max_query_depth")
    class AccessRightsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AccessDefinition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AccessDefinition, _Mapping]] = ...) -> None: ...
    class OauthKeysEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LAST_CHECK_FIELD_NUMBER: _ClassVar[int]
    ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    PER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    QUOTA_MAX_FIELD_NUMBER: _ClassVar[int]
    QUOTA_RENEWS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_REMAINING_FIELD_NUMBER: _ClassVar[int]
    QUOTA_RENEWAL_RATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    OAUTH_KEYS_FIELD_NUMBER: _ClassVar[int]
    BASIC_AUTH_DATA_FIELD_NUMBER: _ClassVar[int]
    JWT_DATA_FIELD_NUMBER: _ClassVar[int]
    HMAC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HMAC_SECRET_FIELD_NUMBER: _ClassVar[int]
    IS_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    APPLY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    MONITOR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DETAILED_RECORDING_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ID_EXTRACTOR_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    SESSION_LIFETIME_FIELD_NUMBER: _ClassVar[int]
    APPLY_POLICIES_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    MAX_QUERY_DEPTH_FIELD_NUMBER: _ClassVar[int]
    last_check: int
    allowance: float
    rate: float
    per: float
    expires: int
    quota_max: int
    quota_renews: int
    quota_remaining: int
    quota_renewal_rate: int
    access_rights: _containers.MessageMap[str, AccessDefinition]
    org_id: str
    oauth_client_id: str
    oauth_keys: _containers.ScalarMap[str, str]
    basic_auth_data: BasicAuthData
    jwt_data: JWTData
    hmac_enabled: bool
    hmac_secret: str
    is_inactive: bool
    apply_policy_id: str
    data_expires: int
    monitor: Monitor
    enable_detailed_recording: bool
    metadata: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    alias: str
    last_updated: str
    id_extractor_deadline: int
    session_lifetime: int
    apply_policies: _containers.RepeatedScalarFieldContainer[str]
    certificate: str
    max_query_depth: int
    def __init__(self, last_check: _Optional[int] = ..., allowance: _Optional[float] = ..., rate: _Optional[float] = ..., per: _Optional[float] = ..., expires: _Optional[int] = ..., quota_max: _Optional[int] = ..., quota_renews: _Optional[int] = ..., quota_remaining: _Optional[int] = ..., quota_renewal_rate: _Optional[int] = ..., access_rights: _Optional[_Mapping[str, AccessDefinition]] = ..., org_id: _Optional[str] = ..., oauth_client_id: _Optional[str] = ..., oauth_keys: _Optional[_Mapping[str, str]] = ..., basic_auth_data: _Optional[_Union[BasicAuthData, _Mapping]] = ..., jwt_data: _Optional[_Union[JWTData, _Mapping]] = ..., hmac_enabled: bool = ..., hmac_secret: _Optional[str] = ..., is_inactive: bool = ..., apply_policy_id: _Optional[str] = ..., data_expires: _Optional[int] = ..., monitor: _Optional[_Union[Monitor, _Mapping]] = ..., enable_detailed_recording: bool = ..., metadata: _Optional[_Mapping[str, str]] = ..., tags: _Optional[_Iterable[str]] = ..., alias: _Optional[str] = ..., last_updated: _Optional[str] = ..., id_extractor_deadline: _Optional[int] = ..., session_lifetime: _Optional[int] = ..., apply_policies: _Optional[_Iterable[str]] = ..., certificate: _Optional[str] = ..., max_query_depth: _Optional[int] = ...) -> None: ...
