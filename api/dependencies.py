from fastapi import Depends, HTTPException, status
from typing import Annotated
from .schemas import NumbersInput, TwoNumbersInput, ExpressionInput

def validate_numbers_input(data: NumbersInput) -> list[float]:
    """Valida y procesa entrada de lista de números"""
    if len(data.numbers) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Debe proporcionar al menos un número"
        )
    return data.numbers

def validate_two_numbers(data: TwoNumbersInput) -> tuple[float, float]:
    """Valida y procesa entrada de dos números"""
    return (data.a, data.b)

def validate_expression(data: ExpressionInput) -> tuple[str, str]:
    """Valida y procesa expresión matemática"""
    if not data.expression.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La expresión no puede estar vacía"
        )
    return (data.expression, data.variable)

# Dependencias inyectables
NumbersDep = Annotated[list[float], Depends(validate_numbers_input)]
TwoNumbersDep = Annotated[tuple[float, float], Depends(validate_two_numbers)]
ExpressionDep = Annotated[tuple[str, str], Depends(validate_expression)]

def get_config():
    """Configuración compartida para la API"""
    return {
        "max_plot_points": 1000,
        "default_precision": 6,
        "max_equation_complexity": 100
    }

ConfigDep = Annotated[dict, Depends(get_config)]
