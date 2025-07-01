def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input types. Use numbers only."

# Example usage (optional for testing):
if __name__ == "__main__":
    print(safe_divide(10, 2))      # Output: 5.0
    print(safe_divide(10, 0))      # Output: Error: Cannot divide by zero.
    print(safe_divide("10", 2))    # Output: Error: Invalid input types. Use numbers only.
