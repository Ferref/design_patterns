class SubsystemA:
    def operation_a(self) -> str:
        return "SubsystemA: Operation A"

class SubsystemB:
    def operation_b(self) -> str:
        return "SubsystemB: Operation B"

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self) -> str:
        result = []
        result.append(self._subsystem_a.operation_a())
        result.append(self._subsystem_b.operation_b())
        return "\n".join(result)
