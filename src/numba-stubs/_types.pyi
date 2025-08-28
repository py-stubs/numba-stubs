from typing import Any, Self

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
