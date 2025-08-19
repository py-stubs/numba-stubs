from typing import Any, Literal, Self

ErrorModel = Literal["python", "numpy"]
InLine = Literal["never", "always"]
Target = Literal["cpu", "parallel", "gpu"]
Identity = Literal[0, 1, "reorderable"]

class Type[T]:
    def __call__(self, *args: Any, **kwds: Any) -> Self: ...

class Array[T](Type[T]):
    def __init__(self, dtype: Type[Any], ndim: Any, layout: Any) -> None: ...

class Integer(Type[int]):
    def __getitem__(self, args: Any) -> Array[int]: ...

class NoneType(Type[None]): ...

class Boolean(Type[bool]):
    def __getitem__(self, args: Any) -> Array[bool]: ...

class Float(Type[float]):
    def __getitem__(self, args: Any) -> Array[float]: ...
