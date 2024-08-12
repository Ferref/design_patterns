# SubsystemA is a class that provides a specific operation.
class SubsystemA:
    def operation_a(self) -> str:
        # Returns the result of operation A from SubsystemA
        return "SubsystemA: Operation A"

# SubsystemB is another class that offers a different operation.
class SubsystemB:
    def operation_b(self) -> str:
        # Returns the result of operation B from SubsystemB
        return "SubsystemB: Operation B"

# The Facade class provides a unified interface to the complex subsystems.
class Facade:
    def __init__(self):
        # Initialize the subsystems; they act as the components behind the facade.
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self) -> str:
        # This method orchestrates calls to the subsystems
        result = []  # List to hold results from subsystems
        result.append(self._subsystem_a.operation_a())  # Call operation A and store the result
        result.append(self._subsystem_b.operation_b())  # Call operation B and store the result
        # Join the results with a newline character and return the final output
        return "\n".join(result)