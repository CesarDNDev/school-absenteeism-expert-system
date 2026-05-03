"""
Test del sistema experto con vectores ordenados
"""

from sistema_experto import valorar_caso

print("=" * 80)
print("TEST DEL SISTEMA EXPERTO CON VECTORES ORDENADOS")
print("=" * 80)
print()

# TEST 1: Sin intervención previa
print("TEST 1: Sin intervención previa del centro")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='no',
    intensidad_absentismo='media',
    siso=45,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 2: Desprotección
print("TEST 2: Caso con desprotección")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=45,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='si',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 3: Riesgo bajo
print("TEST 3: Riesgo bajo - Seguimiento")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='baja',
    siso=45,
    colaboracion_familiar='alta',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print(f"Factores: {resultado['factores_activados']}")
print()

# TEST 4: Intervención preventiva (SISO alto, pocas faltas)
print("TEST 4: Intervención preventiva (SISO > 58, faltas bajas)")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='baja',
    siso=65,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 5: Intervención ETI especializada
print("TEST 5: Intervención ETI (absentismo alto + SISO > 58)")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='alta',
    siso=70,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 6: No cooperación familiar
print("TEST 6: No cooperación familiar")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='alta',
    siso=45,
    colaboracion_familiar='nula',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 7: Equipo de familia
print("TEST 7: Equipo de familia (absentismo medio, SISO bajo, familia colabora)")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=50,
    colaboracion_familiar='alta',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 8: Caso complejo (salud mental)
print("TEST 8: Caso complejo - Revisión manual")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=45,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='salud_mental_grave',
    estado_informacion='completa'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 9: Información incompleta
print("TEST 9: Información incompleta")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=45,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='incompleta'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

# TEST 10: Información contradictoria
print("TEST 10: Información contradictoria")
print("-" * 80)
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=45,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='contradictoria'
)
print(f"Recomendación: {resultado['recomendacion']}")
print(f"Nivel de riesgo: {resultado['nivel_riesgo']}")
print(f"Explicación: {resultado['explicacion']}")
print()

print("=" * 80)
print("TESTS COMPLETADOS")
print("=" * 80)
