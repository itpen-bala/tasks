# from typing import Self (since python 3.11)
from __future__ import annotations

import numpy as np


class RingBufferIterator:
    def __init__(self, buf: np.ndarray) -> None:
        self.buf = buf
        self.curr_index = 0

    def __next__(self) -> np.ndarray | None:
        if self.curr_index < self.buf.size:
            result = self.buf[self.curr_index]
            self.curr_index += 1
            return result
        raise StopIteration

    def __iter__(self) -> RingBufferIterator:
        return self


class RingBuffer:
    def __init__(self, size: int) -> None:
        self.buf = np.zeros(size, dtype=np.int8)
        self.last_el = -1

    def __iter__(self) -> RingBufferIterator:
        return RingBufferIterator(self.buf)

    def get_by_index(self, index: int) -> np.int8 | None:
        try:
            return self.buf[index]
        except IndexError:
            print(f"Index {index} is out of bounds for length {self.buf.size}")
            return None

    def get_last(self) -> np.int8 | None:
        if self.last_el < 0:
            print("Buffer is empty")
            return None
        else:
            return self.buf[self.last_el]

    def set(self, value: int) -> None:
        if self.last_el < self.buf.size - 1:
            self.last_el += 1
        else:
            self.last_el = 0
        self.buf[self.last_el] = value
