"""
Casos de prueba para validar el Sistema Experto de Absentismo Escolar
Basados en los casos descritos en la Entrevista Nº3
"""

from sistema_experto import valorar_caso


def imprimir_resultado(numero_caso, descripcion, resultado):
    """Imprime el resultado de forma formateada"""
    print("\n" + "=" * 80)
    print(f"CASO {numero_caso}: {descripcion}")
    print("=" * 80)
    print(f"📊 Nivel de riesgo: {resultado['nivel_riesgo']}")
    print(f"📋 Recomendación: {resultado['recomendacion']}")
    print("\n💡 Explicación:")
    for linea in resultado['explicacion']:
        print(f"   {linea}")
    if resultado['factores_activados']:
        print("\n🔍 Factores activados:")
        for factor in resultado['factores_activados']:
            print(f"   • {factor}")


def ejecutar_casos_prueba():
    """Ejecuta todos los casos de prueba del sistema"""
    
    print("\n" + "=" * 80)
    print("SISTEMA EXPERTO DE ABSENTISMO ESCOLAR - CASOS DE PRUEBA")
    print("=" * 80)
    
    # CASO 1: Seguimiento simple (riesgo bajo)
    caso1 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='baja',
        siso=35,
        colaboracion_familiar='alta',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    imprimir_resultado(
        1,
        "Faltas esporádicas, familia colaboradora, sin antecedentes",
        caso1
    )
    
    # CASO 2: Intervención ETI especializada
    caso2 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='alta',
        siso=75,
        colaboracion_familiar='media',
        antecedentes='si',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    imprimir_resultado(
        2,
        "Absentismo alto, SISO elevado, reincidencia",
        caso2
    )
    
    # CASO 3: Revisión manual (salud mental grave)
    caso3 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=60,
        colaboracion_familiar='baja',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='salud_mental_grave',
        estado_informacion='completa'
    )
    imprimir_resultado(
        3,
        "Salud mental grave - Requiere valoración especializada",
        caso3
    )
    
    # CASO 4: Sin intervención previa del centro
    caso4 = valorar_caso(
        intervencion_previa_centro='no',
        intensidad_absentismo='media',
        siso=50,
        colaboracion_familiar='media',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    imprimir_resultado(
        4,
        "Centro no ha intervenido previamente",
        caso4
    )
    
    # CASO 5: Desprotección detectada
    caso5 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=55,
        colaboracion_familiar='baja',
        antecedentes='no',
        desproteccion='si',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    imprimir_resultado(
        5,
        "Indicadores de desprotección del menor",
        caso5
    )
    
    # CASO 6: Intervención preventiva (pocas faltas, SISO alto)
    caso6 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='baja',
        siso=65,
        colaboracion_familiar='media',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    imprimir_resultado(
        6,
        "Pocas faltas pero vulnerabilidad social elevada",
        caso6
    )
    
    # CASO 7: No cooperación familiar
    caso7 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='alta',
        siso=45,
        colaboracion_familiar='nula',
        antecedentes='si',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    imprimir_resultado(
        7,
        "Absentismo alto + familia no coopera",
        caso7
    )
    
    # CASO 8: Equipo de familia
    caso8 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=50,
        colaboracion_familiar='alta',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='completa'
    )
    imprimir_resultado(
        8,
        "Absentismo medio, SISO moderado, familia colabora",
        caso8
    )
    
    # CASO 9: Información contradictoria
    caso9 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='media',
        siso=55,
        colaboracion_familiar='media',
        antecedentes='no',
        desproteccion='no',
        situacion_personal='sin_indicadores',
        estado_informacion='contradictoria'
    )
    imprimir_resultado(
        9,
        "Información contradictoria entre fuentes",
        caso9
    )
    
    # CASO 10: Consumo de sustancias
    caso10 = valorar_caso(
        intervencion_previa_centro='si',
        intensidad_absentismo='alta',
        siso=70,
        colaboracion_familiar='baja',
        antecedentes='si',
        desproteccion='no',
        situacion_personal='consumo_sustancias',
        estado_informacion='completa'
    )
    imprimir_resultado(
        10,
        "Consumo de sustancias detectado",
        caso10
    )
    
    print("\n" + "=" * 80)
    print("✅ TODOS LOS CASOS DE PRUEBA EJECUTADOS")
    print("=" * 80)
    print("\nResumen de casos:")
    print("  • Caso 1: Seguimiento (riesgo bajo)")
    print("  • Caso 2: Intervención ETI especializada")
    print("  • Caso 3: Revisión manual (salud mental)")
    print("  • Caso 4: Ampliar información (sin intervención previa)")
    print("  • Caso 5: Intervención urgente (desprotección)")
    print("  • Caso 6: Intervención preventiva")
    print("  • Caso 7: Riesgo alto (no cooperación)")
    print("  • Caso 8: Equipo de familia")
    print("  • Caso 9: Ampliar información (contradictoria)")
    print("  • Caso 10: Revisión manual (consumo)")
    print("\n")


if __name__ == "__main__":
    ejecutar_casos_prueba()
