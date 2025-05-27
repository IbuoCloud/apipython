import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
from typing import List, Tuple

def plot_function(expression: str, x_range: Tuple[float, float] = (-10, 10)) -> str:
    """Genera gráfico de una función matemática y devuelve imagen en base64"""
    x = np.linspace(x_range[0], x_range[1], 400)
    y = eval(expression, {'np': np, 'x': x})
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title(f'Gráfico de: {expression}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    
    return base64.b64encode(buffer.read()).decode('utf-8')

def plot_3d_surface(expression: str, 
                   x_range: Tuple[float, float] = (-5, 5),
                   y_range: Tuple[float, float] = (-5, 5)) -> str:
    """Genera gráfico 3D de una superficie"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = eval(expression, {'np': np, 'x': X, 'y': Y})
    
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title(f'Superficie 3D: {expression}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    
    return base64.b64encode(buffer.read()).decode('utf-8')

def plot_histogram(data: List[float], bins: int = 10) -> str:
    """Genera histograma de datos"""
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title('Histograma de datos')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    
    return base64.b64encode(buffer.read()).decode('utf-8')
