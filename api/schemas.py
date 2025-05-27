from pydantic import BaseModel, conlist, confloat
from typing import List, Optional, Dict, Union

class NumbersInput(BaseModel):
    numbers: conlist(float, min_length=1)


class TwoNumbersInput(BaseModel):
    a: Union[int, float]
    b: Union[int, float]

class ExpressionInput(BaseModel):
    expression: str
    variable: Optional[str] = 'x'

class EquationInput(BaseModel):
    equation: str
    method: Optional[str] = 'auto'

class PlotRangeInput(BaseModel):
    min: confloat(gt=-1000, lt=1000)
    max: confloat(gt=-1000, lt=1000)

class PlotInput(BaseModel):
    expression: str
    x_range: Optional[PlotRangeInput] = PlotRangeInput(min=-10, max=10)
    y_range: Optional[PlotRangeInput] = PlotRangeInput(min=-5, max=5)

class SystemEquationInput(BaseModel):
    equations: List[str]
    variables: List[str]

class DifferentialEquationInput(BaseModel):
    equation: str
    initial_conditions: Dict[str, float]
