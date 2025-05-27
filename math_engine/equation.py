from sympy import symbols, Eq, solve, nsolve
from sympy.abc import x, y
import numpy as np
from typing import Union, List, Dict
from .numeric import power, sqrt
from .symbolic import solve_equation as symbolic_solve

class EquationSolver:
    @staticmethod
    def linear(a: float, b: float) -> float:
        """Resuelve ecuaciones lineales: ax + b = 0"""
        if a == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero")
        return -b / a

    @staticmethod
    def quadratic(a: float, b: float, c: float) -> List[float]:
        """Resuelve ecuaciones cuadráticas: ax² + bx + c = 0"""
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("La ecuación no tiene soluciones reales")
        return [
            (-b + sqrt(discriminant)) / (2*a),
            (-b - sqrt(discriminant)) / (2*a)
        ]

    @staticmethod
    def polynomial(coefficients: List[float]) -> List[Union[float, complex]]:
        """Resuelve ecuaciones polinómicas usando numpy"""
        return list(np.roots(coefficients))

    @staticmethod
    def system(equations: List[str], variables: List[str]) -> Dict[str, float]:
        """Resuelve sistemas de ecuaciones"""
        sym_vars = symbols(' '.join(variables))
        eqs = [Eq(*map(eval, eq.split('='))) for eq in equations]
        solutions = solve(eqs, sym_vars)
        return {str(var): float(sol) for var, sol in solutions.items()}

    @staticmethod
    def differential(equation: str, initial_conditions: Dict[str, float]) -> str:
        """Resuelve ecuaciones diferenciales básicas"""
        # Implementación simplificada para demostración
        return symbolic_solve(equation, 'x')

def solve_equation(equation: str, method: str = 'auto') -> Union[float, List[float], Dict[str, float]]:
    """Resuelve ecuaciones usando el método más apropiado"""
    if '=' not in equation:
        raise ValueError("La ecuación debe contener un signo igual")
    
    if method == 'symbolic':
        return symbolic_solve(equation)
    else:
        # Implementar lógica para detectar tipo de ecuación
        try:
            return EquationSolver.linear(1, -2)  # Ejemplo simplificado
        except Exception:
            return symbolic_solve(equation)
