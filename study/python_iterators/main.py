from dataclasses import dataclass
from typing import Iterable
import itertools


# Implementacao de um iterator
class SequenceIterator:

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index+= 1
            return item
        else:
            raise StopIteration

class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current 
            self._current, self._next = (
                self._next,
                self._current + self._next
            )
            return fib_number
        else:
            raise StopIteration


@dataclass(frozen=True)
class LineItem:
    price: int
    quantity: int

    def total_price(self) -> int:
        return self.price * self.quantity

def print_totals(items: Iterable[LineItem]) -> None:
    for item in items:
        print(item.total_price())

def main() -> None:
    # pelo mecanismo de abstracao, nao importa o tipo de sequencia que o line_items for
    # ele vai printar independente do tipo: list, tuple ...
    # so precisa ser um tipo iterable
    # mas eh importante a classe ser frozen=True
    # do contrario, tipo de dados como dict ou set podem dar erro de hash
    items = ["a", "b", "c", "d"]
    more_items = ["e", "f"]
    # combinando os dois iterators em um so
    #print(list(itertools.chain(items, more_items)))
    # e utilizar em conjunto com outros metodos 
    #print(list(itertools.combinations(itertools.chain(items, more_items), 2)))
    #print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(50))))
    #print(list(itertools.filterfalse(lambda x: x % 2 != 0, range(50))))
    #print(list(itertools.starmap(lambda x, y: x * y, [(2, 6), (6, 10), (4, 2)])))


if __name__ == '__main__':
    main()
