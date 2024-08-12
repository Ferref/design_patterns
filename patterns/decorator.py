from abc import ABC, abstractmethod

# Component interface defines the interface for objects that can have responsibilities added to them
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def ingredients(self) -> str:
        pass

# Concrete component that implements the Coffee interface
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        # Base cost of a simple coffee
        return 2.00

    def ingredients(self) -> str:
        # Base ingredients of a simple coffee
        return "Coffee"

# Abstract decorator class that implements the Coffee interface 
# and maintains a reference to a Coffee object
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee  # The coffee object being decorated

    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def ingredients(self) -> str:
        pass

# A concrete decorator that adds milk to the coffee
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        # Adding the cost of milk to the base coffee cost
        return self._coffee.cost() + 0.50

    def ingredients(self) -> str:
        # Adding milk's ingredients to the base ingredients
        return f"{self._coffee.ingredients()}, Milk"

# A concrete decorator that adds sugar to the coffee
class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        # Adding the cost of sugar to the base coffee cost
        return self._coffee.cost() + 0.25

    def ingredients(self) -> str:
        # Adding sugar's ingredients to the base ingredients
        return f"{self._coffee.ingredients()}, Sugar"

# Client code to demonstrate the Decorator pattern
if __name__ == '__main__':
    # Creating a simple coffee
    coffee = SimpleCoffee()
    print(f"Cost: {coffee.cost():.2f}, Ingredients: {coffee.ingredients()}")

    # Decorating with milk
    coffee_with_milk = MilkDecorator(coffee)
    print(f"Cost: {coffee_with_milk.cost():.2f}, Ingredients: {coffee_with_milk.ingredients()}")

    # Further decorating with sugar
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"Cost: {coffee_with_milk_and_sugar.cost():.2f}, Ingredients: {coffee_with_milk_and_sugar.ingredients()}")