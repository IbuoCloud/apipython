# Math API

API para operaciones matemáticas avanzadas con soporte para:
- Cálculos numéricos
- Álgebra simbólica
- Resolución de ecuaciones
- Generación de gráficos

## Requisitos

- Python 3.9+
- Dependencias listadas en `requirements.txt`

## Instalación

1. Crear entorno virtual:
```bash
python -m venv venv
```

2. Activar entorno:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar la API:
```bash
python run.py
```

La API estará disponible en:
- http://localhost:8000
- Documentación Swagger: http://localhost:8000/docs
- Documentación Redoc: http://localhost:8000/redoc

## Endpoints principales

### Numéricos
- `/numeric/add` - Suma de números
- `/numeric/subtract` - Resta de números  
- `/numeric/multiply` - Multiplicación de números
- `/numeric/divide` - División de números

### Simbólicos
- `/symbolic/solve` - Resuelve ecuaciones
- `/symbolic/derivative` - Calcula derivadas
- `/symbolic/integral` - Calcula integrales

### Gráficos
- `/plot/function` - Genera gráficos 2D
- `/plot/surface` - Genera gráficos 3D

### Ecuaciones
- `/equation/solve` - Resuelve ecuaciones complejas

## Ejemplos

```python
import requests

# Sumar números
response = requests.post(
    "http://localhost:8000/numeric/add",
    json={"numbers": [1, 2, 3]}
)
print(response.json())  # {"result": 6}
```

## Licencia
MIT
