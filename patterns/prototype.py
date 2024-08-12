import copy

class Prototype:
    # Base prototype class
    def __init__(self, value):
        self.value = value

    def clone(self):
        # Create a shallow copy of the instance
        return copy.copy(self)


class ConcretePrototype(Prototype):
    # Concrete prototype implementation
    def __init__(self, value, list_value):
        super().__init__(value)
        self.list_value = list_value

    def clone(self):
        # Create a deep copy of the instance
        return copy.deepcopy(self)


if __name__ == "__main__":
    # Create an original object
    original = ConcretePrototype(10, [1, 2, 3])
    # Clone the original object
    clone = original.clone()

    # Modify the clone's data
    clone.value = 20
    clone.list_value.append(4)

    # Display original and cloned objects
    print(f"Original value: {original.value}, list: {original.list_value}")  # Output: 10, [1, 2, 3]
    print(f"Clone value: {clone.value}, list: {clone.list_value}")  # Output: 20, [1, 2, 3, 4]
