# Numba stubs

type stubs for numba.

<https://numba.readthedocs.io/en/stable/index.html>

<https://github.com/numba/numba>

## What does this do

Correct all errors from calls, provide autocompletions for type signature, preserve decorated functions and class signatures.

Provide types for:

- jitclass
- jit
- guvectorize signature
- numba types (floats, integers, arrays) as well as Array inference from slicing calls

## Notes

- It's currently impossible to correctly type both the guvectorize functions declarations, decorator signature, AND calls to the decorated func.

- numba types are generics in those stubs. This is not the case in the actual implementation, don't try to subtype them.

- Due to the numerous awkards design choices, overloads are mandatory for jit. This mean that the docstring from the actual implementation is lost (at least with Pylance).

- Signatures specs in jit are expected to be given with numba types, not strings.

## Installation
