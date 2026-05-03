# Tests del Sistema Experto de Absentismo Escolar

## Estructura de tests

```
tests/
├── __init__.py                 # Inicialización del paquete de tests
├── README.md                   # Este archivo
├── test_simple.py              # Tests básicos de funcionamiento
├── test_reglas.py              # Tests unitarios de cada regla
└── casos_prueba.py             # 10 casos de prueba completos
```

## Ejecutar tests

### Tests básicos
```bash
python tests/test_simple.py
```

### Tests unitarios de reglas
```bash
python tests/test_reglas.py
```

### Casos de prueba completos
```bash
python tests/casos_prueba.py
```

## Cobertura de tests

### test_simple.py
- ✅ 5 tests básicos
- ✅ Verifica funcionamiento general
- ✅ Casos representativos de cada nivel de riesgo

### test_reglas.py
- ✅ 11 tests unitarios
- ✅ Una prueba por cada regla CLIPS
- ✅ Test del umbral SISO = 58
- ✅ Verificación de assertions

### casos_prueba.py
- ✅ 10 casos de prueba detallados
- ✅ Salida formateada con explicaciones
- ✅ Factores activados
- ✅ Cobertura completa de escenarios

## Reglas testeadas

| # | Regla | Test |
|---|-------|------|
| 1 | Sin intervención previa | ✅ |
| 2 | Revisión manual | ✅ |
| 3 | Información contradictoria | ✅ |
| 4 | Información incompleta | ✅ |
| 5 | Desprotección (prioridad 100) | ✅ |
| 6 | Seguimiento | ✅ |
| 7 | Intervención preventiva | ✅ |
| 8 | Intervención ETI | ✅ |
| 9 | No cooperación familiar | ✅ |
| 10 | Equipo de familia | ✅ |

## Casos especiales testeados

- ✅ Umbral SISO = 58 (límite crítico)
- ✅ Múltiples reglas activadas simultáneamente
- ✅ Prioridad de desprotección sobre otras reglas
- ✅ Todos los valores de situación_personal
- ✅ Todos los estados de información

## Resultados esperados

Todos los tests deben pasar sin errores:
```
✅ TODOS LOS TESTS PASARON CORRECTAMENTE
```

## Agregar nuevos tests

Para agregar un nuevo test:

1. Crear función `test_nombre_descriptivo()` en `test_reglas.py`
2. Usar `assert` para verificar resultados esperados
3. Agregar `print("✅ TEST: descripción - OK")` al final
4. Ejecutar para verificar

Ejemplo:
```python
def test_nuevo_caso():
    """Descripción del test"""
    resultado = valorar_caso(...)
    assert resultado['recomendacion'] == 'Esperado'
    print("✅ TEST: Nuevo caso - OK")
```
