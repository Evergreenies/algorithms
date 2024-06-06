"""
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:
"""

from typing import Any


class PrefixMapSum:
    def __init__(self) -> None:
        self.map: dict = {}

    def insert(self, key: str, value: Any) -> None:
        self.map[key] = value

        for index in range(len(key)):
            prefix = key[: index + 1]
            self.map[prefix] = self.map.get(prefix, 0) + value

    def sum(self, prefix: str) -> int:
        return self.map.get(prefix, 0)


pms = PrefixMapSum()
pms.insert("apple", 3)
pms.insert("app", 2)

print(pms.sum("apple"))
print(pms.sum("ap"))
print(pms.sum("a"))
