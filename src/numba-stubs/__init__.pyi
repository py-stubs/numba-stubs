from collections.abc import Callable
from typing import Any, Iterable, overload

from ._stubs_types import (
    Boolean,
    ErrorModel,
    Float,
    Identity,
    InLine,
    Integer,
    NoneType,
    Target,
    Type,
)

@overload
def jit[R, **P](
    function_or_signature: Callable[P, R],
    *,
    locals: dict[str, Any] = {},
    cache: bool = False,
    pipeline_class: type | None = None,
    boundscheck: bool | None = None,
    nopython: bool = True,
    forceobj: bool = False,
    looplift: bool = True,
    error_model: ErrorModel = "python",
    inline: InLine | Callable[..., bool] = "never",
    parallel: bool = False,
    nogil: bool = False,
) -> Callable[P, R]: ...
@overload
def jit[R, **P](
    function_or_signature: list[Type[R]] | None = None,
    *,
    locals: dict[str, Any] = {},
    cache: bool = False,
    pipeline_class: type | None = None,
    boundscheck: bool | None = None,
    nopython: bool = True,
    forceobj: bool = False,
    looplift: bool = True,
    error_model: ErrorModel = "python",
    inline: InLine | Callable[..., bool] = "never",
    parallel: bool = False,
    nogil: bool = False,
) -> Callable[[Callable[P, R]], Callable[P, R]]: ...
def guvectorize[R, **P](
    signatures: Iterable[Type[Any]] | Type[Any],
    layout: str,
    /,
    *,
    identity: Identity | None = None,
    nopython: bool = True,
    target: Target = "cpu",
    forceobj: bool = False,
    cache: bool = False,
    locals: dict[str, Any] = {},
) -> Callable[[Callable[P, R]], Callable[P, R]]: ...

class prange(object):
    def __new__(cls, *args: Any) -> range: ...

float32: Float
float64: Float
byte: Integer
uint8: Integer
uint16: Integer
uint32: Integer
uint64: Integer

intp: Integer
int8: Integer
int16: Integer
int32: Integer
int64: Integer
void: NoneType
bool_: Boolean
