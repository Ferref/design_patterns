# SubsystemA contains a specific operation that can be used by clients directly or through a facade.
class SubsystemA:
    def operation_a(self) -> str:
        # This method simulates an operation within SubsystemA.
        return "SubsystemA: Operation A"

# SubsystemB contains a different operation that can also be accessed by clients directly or through a facade.
class SubsystemB:
    def operation_b(self) -> str:
        # This method simulates an operation within SubsystemB.
        return "SubsystemB: Operation B"

# The Facade class provides a simplified interface to the complex subsystems.
class Facade:
    def __init__(self):
        # The facade initializes and holds references to the subsystems.
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self) -> str:
        # The operation method combines the operations of multiple subsystems.
        # This provides a unified and simplified interface to the client.
        result = []
        result.append(self._subsystem_a.operation_a())  # Calls an operation in SubsystemA
        result.append(self._subsystem_b.operation_b())  # Calls an operation in SubsystemB
        return "\n".join(result)  # Joins the results of the subsystem operations into a single string
