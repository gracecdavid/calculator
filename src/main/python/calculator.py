# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
def main():
    calc = Calculator()
    print("Enter two numbers:")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print("1. Addition\n2. Subtraction")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        result = calc.add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = calc.sub(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
