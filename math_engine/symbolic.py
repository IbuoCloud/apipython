from sympy import symbols, Eq, solve, simplify, diff, integrate, series, sympify

from sympy.abc import x, y, z
from typing import Union, List, Dict

def solve_equation(equation: str, variable: str = 'x') -> Dict[str, Union[float, complex, str]]:
    """Resuelve ecuaciones algebraicas
    
    Args:
        equation: Ecuación matemática como string (ej: "x^2 - 4" o "x^2 = 4")
        variable: Variable a resolver (default: 'x')
        
    Returns:
        Dict con soluciones en formato {"solutions": [sol1, sol2, ...], "variable": var}
        
    Raises:
        ValueError: Si la ecuación no es válida o no tiene solución
    """
    try:
        var = symbols(variable)
        
        if '=' in equation:
            parts = equation.split('=')
            if len(parts) != 2:
                raise ValueError("La ecuación debe contener exactamente un '='")
            lhs, rhs = parts
            expr = Eq(sympify(lhs), sympify(rhs))
        else:
            expr = Eq(sympify(equation), 0)
            
        solutions = solve(expr, var)
        
        if not solutions:
            raise ValueError("La ecuación no tiene solución")
            
        return {
            "solutions": [str(sol) for sol in solutions],
            "variable": variable,
            "status": "success"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "variable": variable
        }



def derivative(expression: str, variable: str = 'x', order: int = 1) -> str:
    """Calcula derivadas de una expresión"""
    var = symbols(variable)
    expr = simplify(expression)
    return str(diff(expr, var, order))

def integral(expression: str, variable: str = 'x') -> str:
    """Calcula integrales indefinidas"""
    var = symbols(variable)
    expr = simplify(expression)
    return str(integrate(expr, var))

def taylor_series(expression: str, point: float = 0, degree: int = 5) -> str:
    """Calcula series de Taylor"""
    expr = simplify(expression)
    return str(series(expr, x, point, degree).removeO())

def simplify_expression(expression: str) -> str:
    """Simplifica expresiones algebraicas"""
    return str(simplify(expression))
