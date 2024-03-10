"""
A simple calculator module.
"""

class Calculator:
    """
    A class representing a simple calculator.
    """

    def add(self, a, b):
        """
        Adds two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of the two numbers.
        """
        return a + b

    def sub(self, a, b):
        """
        Subtracts one number from another.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The result of subtracting the second number from the first.
        """
        return a - b

def main():
    """
    Entry point of the program.
    """
    calc = Calculator()
    print("Enter two numbers:")
    add_result = calc.add(3, 5)
    print("Result:", add_result)

    print("Enter two numbers:")
    sub_result = calc.sub(10, 5)
    print("Result:", sub_result)
    sub_result = calc.sub(0,5)
    print("Result:", sub_result)

if __name__ == "__main__":
    main()
