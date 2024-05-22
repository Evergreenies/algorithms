"""
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, 
which also implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""

from typing import Any, Iterator, Optional


class PeekableInterface(object):
    def __init__(self, iterator: Iterator):
        pass

    def peek(self) -> Optional[Any]:
        pass

    def next(self) -> Optional[Any]:
        pass

    def hasNext(self) -> bool:
        pass


class PeekableIterator(PeekableInterface):
    def __init__(self, iterator: Iterator):
        self._iterator = iterator
        self._next_value = None

    def has_next(self) -> bool:
        return (self._next_value is not None) or (hasattr(self._iterator, "__next__"))

    def peek(self) -> Optional[Any]:
        if self._next_value is None:
            try:
                self._next_value = next(self._iterator)
            except StopIteration:
                raise StopIteration

        return self._next_value

    def next(self) -> Optional[Any]:
        if self._next_value is not None:
            value = self._next_value
            self._next_value = None
            return value
        else:
            try:
                return next(self._iterator)
            except StopIteration:
                raise StopIteration


class MyIterator:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        return value


if __name__ == "__main__":
    iteratr = MyIterator([1, 2, 3, 4])
    peekable = PeekableIterator(iteratr)

    print(peekable.peek())
    print(peekable.next())

    print(peekable.peek())
    print(peekable.next())
