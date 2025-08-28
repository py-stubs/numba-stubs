from collections.abc import Callable
from typing import Any, Iterable, Literal, overload

from ._types import Type

ErrorModel = Literal["python", "numpy"]
InLine = Literal["never", "always"]

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
    identity: Literal[0, 1, "reorderable"] | None = None,
    nopython: bool = True,
    target: Literal["cpu", "parallel", "gpu"] = "cpu",
    forceobj: bool = False,
    cache: bool = False,
    locals: dict[str, Any] = {},
) -> Callable[[Callable[P, R]], Callable[P, R]]: ...

class prange(object):
    def __new__(cls, *args: Any) -> range: ...
