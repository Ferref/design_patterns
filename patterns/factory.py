from abc import ABC, abstractmethod

# Abstract base class for products
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Concrete product classes implementing the abstract base class
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Operation of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Operation of ConcreteProductB"

# Factory class responsible for creating products
class ProductFactory:
    @staticmethod
    def create_product(product_type: str) -> Product:
        """
        Factory method to create a product instance based on the given type.

        :param product_type: The type of product to create. Should be 'A' or 'B'.
        :return: An instance of the specified product type.
        """
        if product_type == 'A':
            return ConcreteProductA()
        elif product_type == 'B':
            return ConcreteProductB()
        else:
            raise ValueError("Invalid product type")

# Client code that uses the factory to get instances of products
if __name__ == '__main__':
    # Create product A
    product_a = ProductFactory.create_product('A')
    # Create product B
    product_b = ProductFactory.create_product('B')

    # Use the products
    print(product_a.operation())  # Output: Operation of ConcreteProductA
    print(product_b.operation())  # Output: Operation of ConcreteProductB
