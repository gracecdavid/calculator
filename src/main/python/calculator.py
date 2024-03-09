# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
def main():
    calc = Calculator()
    print("Enter two numbers:")
    result = calc.add(3,5)
    print("Result:",result)
if __name__ == "__main__":
    main()
