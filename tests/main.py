from collections.abc import Callable

import numba as nb
import numpy as np


def test_func(x: int, y: int) -> int:
    return x + y


@nb.jit([nb.int64(nb.int64, nb.int64)], nopython=True)
def test(x: int, y: int) -> int:
    return x + y


@nb.guvectorize([nb.void(nb.float64[:], nb.intp[:], nb.float64[:])], "(n),()->(n)")
def move_mean(
    a: np.typing.NDArray[np.float64],
    window: np.typing.NDArray[np.int64],
    *,
    out: np.typing.NDArray[np.float64],
) -> None:
    window_width = window[0]

    asum = 0.0

    count = 0

    for i in range(window_width):
        asum += a[i]

        count += 1

        out[i] = asum / count

    for i in range(window_width, len(a)):
        asum += a[i] - a[i - window_width]

        out[i] = asum / count


test3: Callable[..., int] = nb.jit(test_func)

if __name__ == "__main__":
    print(test(3, 4))
    print(test3(3, 4))

    arr = np.arange(20, dtype=np.float64).reshape(2, 10)

    # currently impossible to type correctly
    print(move_mean(arr, 3))  # type: ignore
