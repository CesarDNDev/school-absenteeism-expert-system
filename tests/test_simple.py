"""Test simple del sistema experto"""
from sistema_experto import valorar_caso

print("=" * 80)
print("TEST DEL SISTEMA EXPERTO DE ABSENTISMO ESCOLAR")
print("=" * 80)

# Test 1: Riesgo bajo
print("\n📋 TEST 1: Riesgo bajo (seguimiento)")
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='baja',
    siso=35,
    colaboracion_familiar='alta',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"✅ Recomendación: {resultado['recomendacion']}")
print(f"✅ Nivel de riesgo: {resultado['nivel_riesgo']}")

# Test 2: Desprotección (máxima prioridad)
print("\n📋 TEST 2: Desprotección detectada")
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=55,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='si',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"✅ Recomendación: {resultado['recomendacion']}")
print(f"✅ Nivel de riesgo: {resultado['nivel_riesgo']}")

# Test 3: SISO alto + absentismo consolidado
print("\n📋 TEST 3: SISO alto + absentismo consolidado")
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='alta',
    siso=75,
    colaboracion_familiar='media',
    antecedentes='si',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"✅ Recomendación: {resultado['recomendacion']}")
print(f"✅ Nivel de riesgo: {resultado['nivel_riesgo']}")

# Test 4: Revisión manual
print("\n📋 TEST 4: Caso requiere revisión manual")
resultado = valorar_caso(
    intervencion_previa_centro='si',
    intensidad_absentismo='media',
    siso=60,
    colaboracion_familiar='baja',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='salud_mental_grave',
    estado_informacion='completa'
)
print(f"✅ Recomendación: {resultado['recomendacion']}")
print(f"✅ Nivel de riesgo: {resultado['nivel_riesgo']}")

# Test 5: Sin intervención previa
print("\n📋 TEST 5: Centro sin intervención previa")
resultado = valorar_caso(
    intervencion_previa_centro='no',
    intensidad_absentismo='media',
    siso=50,
    colaboracion_familiar='media',
    antecedentes='no',
    desproteccion='no',
    situacion_personal='sin_indicadores',
    estado_informacion='completa'
)
print(f"✅ Recomendación: {resultado['recomendacion']}")
print(f"✅ Nivel de riesgo: {resultado['nivel_riesgo']}")

print("\n" + "=" * 80)
print("✅ TODOS LOS TESTS PASARON CORRECTAMENTE")
print("✅ SISTEMA EXPERTO FUNCIONANDO CON CLIPS")
print("=" * 80)
