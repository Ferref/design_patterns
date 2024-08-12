from abc import ABC, abstractmethod

# Abstract base class for products, serves as a blueprint for concrete products
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        # Abstract method that must be implemented by all concrete products
        pass

# Concrete product class that implements the abstract method from Product
class ConcreteProductA(Product):
    def operation(self) -> str:
        # Provides a specific implementation for ConcreteProductA
        return "Operation of ConcreteProductA"

# Concrete product class that implements the abstract method from Product
class ConcreteProductB(Product):
    def operation(self) -> str:
        # Provides a specific implementation for ConcreteProductB
        return "Operation of ConcreteProductB"

# Factory class responsible for creating product instances based on type
class ProductFactory:
    @staticmethod
    def create_product(product_type: str) -> Product:
        """
        Factory method to create a product instance based on the given type.

        :param product_type: The type of product to create. Should be 'A' or 'B'.
        :return: An instance of the specified product type.
        """
        if product_type == 'A':
            # If the product type is 'A', create and return ConcreteProductA instance
            return ConcreteProductA()
        elif product_type == 'B':
            # If the product type is 'B', create and return ConcreteProductB instance
            return ConcreteProductB()
        else:
            # Raise an error if the product type is invalid
            raise ValueError("Invalid product type")

# Client code that demonstrates the use of the factory to create product instances
if __name__ == '__main__':
    # Create product A using the ProductFactory
    product_a = ProductFactory.create_product('A')
    # Create product B using the ProductFactory
    product_b = ProductFactory.create_product('B')

    # Use the created products and print their operations
    print(product_a.operation())  # Output: Operation of ConcreteProductA
    print(product_b.operation())  # Output: Operation of ConcreteProductB