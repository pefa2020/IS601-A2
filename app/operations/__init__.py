def addition(a: float, b: float) -> float:
    return a + b

def substraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divide by zero is not allowed.")
    return a / b