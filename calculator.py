#!/usr/bin/env python3
"""
Simple interactive calculator.

Usage:
  - Run: `python3 calculator.py`
  - Enter expressions like: `2 + 3`, `4.5 * 6`, `10 / 2`, `2 ** 8`, `10 % 3`.
  - Type `q`, `quit`, or `exit` to end.
"""

def format_number(n: float) -> str:
    # Print as int when no fractional part
    if n == int(n):
        return str(int(n))
    return str(n)

def calculate(a: float, op: str, b: float):
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*" or op == "x" or op == "X":
            return a * b
        if op == "/":
            if b == 0:
                return "Error: division by zero"
            return a / b
        if op == "%":
            if b == 0:
                return "Error: modulo by zero"
            return a % b
        if op == "**" or op == "^":
            return a ** b
        return f"Unknown operator: {op}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Simple calculator — enter expressions like: 2 + 3")
    while True:
        try:
            s = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye")
            break

        if not s:
            continue
        if s.lower() in ("q", "quit", "exit"):
            print("Bye")
            break

        parts = s.split()
        if len(parts) != 3:
            print("Invalid format. Use: <number> <operator> <number> (e.g. 2 + 3)")
            continue

        a_str, op, b_str = parts
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid numbers. Please enter numeric operands.")
            continue

        result = calculate(a, op, b)
        if isinstance(result, (int, float)):
            print(format_number(result))
        else:
            print(result)

if __name__ == "__main__":
    main()
