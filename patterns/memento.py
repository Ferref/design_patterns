class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state

class Originator:
    _state = None

    def set_state(self, state: str):
        print(f"Originator: Setting state to {state}")
        self._state = state

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.get_state()
        print(f"Originator: State restored to {self._state}")

class Caretaker:
    def __init__(self):
        self._mementos = []
        self._originator = Originator()

    def backup(self):
        self._mementos.append(self._originator.save())

    def undo(self):
        if not self._mementos:
            return
        memento = self._mementos.pop()
        self._originator.restore(memento)
