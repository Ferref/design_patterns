# Abstract Expression class
class Expression:
    def interpret(self, context):
        raise NotImplementedError("The interpret method must be overridden.")

# TerminalExpression class - implements the interpret operation for terminal symbols in the grammar.
class TerminalExpression(Expression):
    def __init__(self, data: str):
        self.data = data

    def interpret(self, context):
        if self.data in context:
            return True
        return False

# OrExpression class - represents a logical OR operation in the grammar.
class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

# AndExpression class - represents a logical AND operation in the grammar.
class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# Client code
if __name__ == "__main__":
    # Define the context - this is the input to the interpreter.
    context = "John is a programmer"

    # Create expressions
    expr1 = TerminalExpression("John")
    expr2 = TerminalExpression("Jane")
    expr3 = TerminalExpression("programmer")

    # Create complex expressions using Or and And expressions
    or_expr = OrExpression(expr1, expr2)  # "John OR Jane"
    and_expr = AndExpression(expr1, expr3)  # "John AND programmer"

    # Interpret the expressions in the context
    print(f"'John OR Jane' in context: {or_expr.interpret(context)}")  # True, because "John" is in the context
    print(f"'John AND programmer' in context: {and_expr.interpret(context)}")  # True, because both "John" and "programmer" are in the context
