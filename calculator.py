def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract y from x and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    
    while True:
        # Get operation choice from user
        choice = input("\nEnter choice (1/2/3) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please try again.")
            continue
            
        # Get the numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
            
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")

if __name__ == "__main__":
    main() 