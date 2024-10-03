def hello_world():
    print("Hello, SonarQube!")

# Duplicated function code
def duplicate_function():
    print("This is a duplicate function")

def duplicate_function_again():
    print("This is a duplicate function")  # Duplicated logic

# Unused variable example
def unused_variable_function():
    unused_variable = 42  # This variable is never used

# Function with high complexity
def complex_function(value):
    if value == 1:
        if value > 0:
            if value < 100:
                if value % 2 == 0:
                    print("Complexity increasing!")

# Bug: Division by zero
def divide_by_zero():
    value = 42 / 0  # This will cause a runtime error

# Hardcoded password example
def hardcoded_password():
    password = "12345"  # Hardcoded password is a security issue
    print(f"Password is: {password}")

if __name__ == "__main__":
    hello_world()
    duplicate_function()
    duplicate_function_again()
    unused_variable_function()
    complex_function(2)
    hardcoded_password()
    # Comment out divide_by_zero to avoid runtime error during test
    # divide_by_zero()
