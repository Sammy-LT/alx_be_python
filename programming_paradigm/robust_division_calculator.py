import sys

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please provide numeric inputs."

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python robust_division_calculator.py <numerator> <denominator>")
        sys.exit(1)

    result = safe_divide(sys.argv[1], sys.argv[2])
    print(result)
