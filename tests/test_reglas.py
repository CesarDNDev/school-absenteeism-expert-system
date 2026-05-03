"""
Tests unitarios para las reglas del sistema experto
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sistema_experto import valorar_caso


def test_regla_sin_intervencion_previa():
    """Test REGLA 1: Sin intervención previa del centro"""
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
    assert resultado['recomendacion'] == 'Ampliar información'
    assert resultado['nivel_riesgo'] == 'No valorable'
    print("✅ REGLA 1: Sin intervención previa - OK")


def test_regla_revision_manual():
    """Test REGLA 2: Casos que requieren revisión manual"""
    casos = ['salud_mental_grave', 'psicopatologia', 'consumo_sustancias']
    for situacion in casos:
        resultado = valorar_caso(
            intervencion_previa_centro='si',
            intensidad_absentismo='media',
            siso=60,
            colaboracion_familiar='media',
            antecedentes='no',
            desproteccion='no',
            situacion_personal=situacion,
            estado_informacion='completa'
        )
        assert resultado['recomendacion'] == 'Revisión manual obligatoria'
        assert resultado['nivel_riesgo'] == 'Requiere valoración especializada'
    print("✅ REGLA 2: Revisión manual - OK")


def test_regla_informacion_contradictoria():
    """Test REGLA 3: Información contradictoria"""
    resultado = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=55,
        colaboracion_familiar='media',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='contradictoria'
    )
    assert resultado['recomendacion'] == 'Ampliar información'
    assert resultado['nivel_riesgo'] == 'No valorable'
    print("✅ REGLA 3: Información contradictoria - OK")


def test_regla_informacion_incompleta():
    """Test REGLA 4: Información incompleta"""
    resultado = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=55,
        colaboracion_familiar='media',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='incompleta'
    )
    assert resultado['recomendacion'] == 'Ampliar información'
    assert resultado['nivel_riesgo'] == 'No valorable'
    print("✅ REGLA 4: Información incompleta - OK")


def test_regla_desproteccion():
    """Test REGLA 5: Desprotección del menor (máxima prioridad)"""
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
    assert resultado['recomendacion'] == 'Intervención ETI urgente'
    assert resultado['nivel_riesgo'] == 'Alto - Desprotección'
    print("✅ REGLA 5: Desprotección (prioridad 100) - OK")


def test_regla_seguimiento():
    """Test REGLA 6: Seguimiento (riesgo bajo)"""
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
    assert resultado['recomendacion'] == 'Seguimiento'
    assert resultado['nivel_riesgo'] == 'Bajo'
    print("✅ REGLA 6: Seguimiento - OK")


def test_regla_prevencion_vulnerabilidad():
    """Test REGLA 7: Intervención preventiva"""
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
    assert resultado['recomendacion'] == 'Intervención ETI (preventiva)'
    assert 'Preventivo' in resultado['nivel_riesgo']
    print("✅ REGLA 7: Intervención preventiva (SISO > 58) - OK")


def test_regla_eti_especializada():
    """Test REGLA 8: Intervención ETI especializada"""
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
    assert resultado['recomendacion'] == 'Intervención ETI'
    assert 'Medio-Alto' in resultado['nivel_riesgo']
    print("✅ REGLA 8: Intervención ETI especializada - OK")


def test_regla_no_cooperacion():
    """Test REGLA 9: No cooperación familiar"""
    resultado = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='alta',
        siso=45,
        colaboracion_familiar='nula',
        antecedentes='si',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    assert 'derivación' in resultado['recomendacion'].lower()
    assert 'Alto' in resultado['nivel_riesgo']
    print("✅ REGLA 9: No cooperación familiar - OK")


def test_regla_equipo_familia():
    """Test REGLA 10: Equipo de familia"""
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
    assert resultado['recomendacion'] == 'Equipo de familia'
    assert resultado['nivel_riesgo'] == 'Medio'
    print("✅ REGLA 10: Equipo de familia - OK")


def test_umbral_siso():
    """Test del umbral SISO = 58"""
    # SISO <= 58 con absentismo medio/alto y familia colaboradora -> Equipo familia
    resultado_bajo = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=58,
        colaboracion_familiar='alta',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    
    # SISO > 58 con absentismo medio/alto -> ETI
    resultado_alto = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=59,
        colaboracion_familiar='alta',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    
    assert resultado_bajo['recomendacion'] == 'Equipo de familia'
    assert resultado_alto['recomendacion'] == 'Intervención ETI'
    print("✅ TEST UMBRAL: SISO = 58 - OK")


if __name__ == '__main__':
    print("=" * 80)
    print("TESTS UNITARIOS DE REGLAS DEL SISTEMA EXPERTO")
    print("=" * 80)
    print()
    
    test_regla_sin_intervencion_previa()
    test_regla_revision_manual()
    test_regla_informacion_contradictoria()
    test_regla_informacion_incompleta()
    test_regla_desproteccion()
    test_regla_seguimiento()
    test_regla_prevencion_vulnerabilidad()
    test_regla_eti_especializada()
    test_regla_no_cooperacion()
    test_regla_equipo_familia()
    test_umbral_siso()
    
    print()
    print("=" * 80)
    print("✅ TODOS LOS TESTS UNITARIOS PASARON")
    print("=" * 80)
