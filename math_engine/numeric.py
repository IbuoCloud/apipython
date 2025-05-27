import numpy as np
from typing import Union, List

def add(numbers: List[Union[int, float]]) -> float:
    """Suma una lista de números"""
    return np.sum(numbers)

def subtract(a: Union[int, float], b: Union[int, float]) -> float:
    """Resta dos números (a - b)"""
    return a - b

def multiply(numbers: List[Union[int, float]]) -> float:
    """Multiplica una lista de números"""
    return np.prod(numbers)

def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide dos números (a / b)"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """Calcula la potencia (base^exponente)"""
    return np.power(base, exponent)

def sqrt(number: Union[int, float]) -> float:
    """Calcula la raíz cuadrada"""
    if number < 0:
        raise ValueError("No se puede calcular raíz de número negativo")
    return np.sqrt(number)

def log(number: Union[int, float], base: Union[int, float] = 10) -> float:
    """Calcula el logaritmo"""
    if number <= 0 or base <= 0 or base == 1:
        raise ValueError("Argumentos inválidos para logaritmo")
    return np.log(number) / np.log(base)
