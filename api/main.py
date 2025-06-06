import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Union
from api.schemas import SolutionResponse



import math_engine.numeric as numeric
import math_engine.symbolic as symbolic
import math_engine.plotting as plotting
import math_engine.equation as equation
from api.schemas import NumbersInput, TwoNumbersInput, ExpressionInput, EquationInput, PlotInput
from api.dependencies import NumbersDep, TwoNumbersDep, ExpressionDep, ConfigDep


app = FastAPI(
    title="Math API",
    description="API para operaciones matemáticas avanzadas",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Endpoints numéricos
@app.post("/numeric/add")
async def add_numbers(numbers: NumbersDep):
    return {"result": numeric.add(numbers)}

@app.post("/numeric/subtract")
async def subtract_numbers(numbers: TwoNumbersDep):
    a, b = numbers
    return {"result": numeric.subtract(a, b)}

@app.post("/numeric/multiply")
async def multiply_numbers(numbers: NumbersDep):
    return {"result": numeric.multiply(numbers)}

@app.post("/numeric/divide")
async def divide_numbers(numbers: TwoNumbersDep):
    a, b = numbers
    try:
        return {"result": numeric.divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoints simbólicos
@app.post("/symbolic/solve", response_model=SolutionResponse)
async def solve_symbolic(expression_data: ExpressionDep, config: ConfigDep):
    expr, var = expression_data
    try:
        result = symbolic.solve_equation(expr, var)
        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result["message"])
        
        solutions = [str(sol).strip() for sol in result["solutions"]]
        return SolutionResponse(
            solutions=solutions,
            variable=str(result["variable"]),
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/symbolic/derivative")
async def calculate_derivative(expression_data: ExpressionDep):
    expr, var = expression_data
    return {"result": symbolic.derivative(expr, var)}

@app.post("/symbolic/integral")
async def calculate_integral(expression_data: ExpressionDep):
    expr, var = expression_data
    return {"result": symbolic.integral(expr, var)}

# Endpoints de gráficos
@app.post("/plot/function")
async def plot_function(data: PlotInput, config: ConfigDep):
    return {
        "image": plotting.plot_function(data.expression, (data.x_range.min, data.x_range.max)),
        "config": config
    }

@app.post("/plot/surface")
async def plot_surface(data: PlotInput, config: ConfigDep):
    return {
        "image": plotting.plot_3d_surface(
            data.expression, 
            (data.x_range.min, data.x_range.max),
            (data.y_range.min, data.y_range.max)
        ),
        "config": config
    }

# Endpoints de ecuaciones
@app.post("/equation/solve")
async def solve_equation(data: EquationInput, config: ConfigDep):
    try:
        return {
            "solutions": equation.solve_equation(data.equation, data.method),
            "config": config
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Math API - Documentación disponible en /docs"}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=80, help='Port to run the server on')
    parser.add_argument('--log-level', type=str, default='info', 
                        choices=['critical', 'error', 'warning', 'info', 'debug', 'trace'],
                        help='Log level for the server')
    args = parser.parse_args()

    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=args.port,
        reload=True,
        workers=1,
        log_level=args.log_level
    )
