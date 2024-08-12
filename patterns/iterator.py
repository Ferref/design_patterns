# Iterator interface
class Iterator:
    def has_next(self) -> bool:
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

# Concrete Iterator class
class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            result = self._collection[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

# Iterable Collection class
class Collection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self) -> Iterator:
        return ConcreteIterator(self._items)

# Client code
if __name__ == "__main__":
    collection = Collection()
    collection.add_item("Item1")
    collection.add_item("Item2")
    collection.add_item("Item3")

    iterator = iter(collection)
    while iterator.has_next():
        print(iterator.next())  # Output: Item1, Item2, Item3
