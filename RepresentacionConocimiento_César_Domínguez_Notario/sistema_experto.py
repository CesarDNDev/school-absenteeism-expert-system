"""
Sistema Experto para Absentismo Escolar
Basado en CLIPS (clipspy) usando VECTORES ORDENADOS
Sin usar deftemplate - Solo hechos ordenados
Autor: César Domínguez Notario
"""

import clips
from typing import Dict, List


class SistemaAbsentismoEscolar:
    """
    Motor de inferencia CLIPS para valoración inicial de casos de absentismo escolar.
    Implementación con VECTORES ORDENADOS (ordered facts) en lugar de deftemplates.
    """
    
    def __init__(self):
        self.env = clips.Environment()
        self._definir_reglas()
    
    def _definir_reglas(self):
        """
        Define las reglas de producción del sistema experto.
        Los hechos son vectores ordenados: (caso intervencion intensidad siso colaboracion antecedentes desproteccion situacion estado)
        Posiciones del vector:
        0: "caso" (identificador)
        1: intervencion-previa-centro (si/no)
        2: intensidad-absentismo (baja/media/alta)
        3: siso (número 0-100)
        4: colaboracion-familiar (nula/baja/media/alta)
        5: antecedentes (si/no)
        6: desproteccion (si/no)
        7: situacion-personal (sin_indicadores/salud_mental_grave/psicopatologia/consumo_sustancias/conducta_disruptiva)
        8: estado-informacion (completa/incompleta/contradictoria)
        """
        
        # REGLA 1: Sin intervención previa del centro (PRIORIDAD MÁXIMA)
        self.env.build("""
            (defrule sin-intervencion-previa
                (declare (salience 100))
                (caso ?interv ?intens ?siso ?colab ?ant ?desp ?sit ?est)
                (test (eq ?interv no))
                =>
                (assert (resultado "Ampliar información" "No valorable"))
                (assert (explicacion "El centro educativo NO ha realizado intervención previa"))
                (assert (explicacion "RECOMENDACIÓN: Solicitar al centro que realice actuación inicial"))
                (assert (factor "Sin intervención previa del centro"))
            )
        """)
        
        # REGLA 2: Casos que requieren revisión manual (PRIORIDAD 90)
        self.env.build("""
            (defrule revision-manual-compleja
                (declare (salience 90))
                (caso si ?intens ?siso ?colab ?ant ?desp ?sit ?est)
                (test (or (eq ?sit salud_mental_grave) 
                          (eq ?sit psicopatologia) 
                          (eq ?sit consumo_sustancias)))
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Revisión manual obligatoria" "Requiere valoración especializada"))
                (assert (explicacion "CASO COMPLEJO: Detectados indicadores que requieren valoración especializada"))
                (assert (explicacion "Este caso queda FUERA del sistema experto automático"))
                (assert (explicacion "RECOMENDACIÓN: Derivar a revisión manual por profesional especializado"))
                (assert (factor "Situación personal compleja"))
            )
        """)
        
        # REGLA 3: Información contradictoria (PRIORIDAD 85)
        self.env.build("""
            (defrule informacion-contradictoria
                (declare (salience 85))
                (caso si ?intens ?siso ?colab ?ant ?desp ?sit contradictoria)
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Ampliar información" "No valorable"))
                (assert (explicacion "La información disponible es CONTRADICTORIA entre fuentes"))
                (assert (explicacion "RECOMENDACIÓN: Contactar con equipo de atención primaria"))
                (assert (factor "Información contradictoria"))
            )
        """)
        
        # REGLA 4: Información incompleta (PRIORIDAD 80)
        self.env.build("""
            (defrule informacion-incompleta
                (declare (salience 80))
                (caso si ?intens ?siso ?colab ?ant ?desp ?sit incompleta)
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Ampliar información" "No valorable"))
                (assert (explicacion "La información disponible es INCOMPLETA"))
                (assert (explicacion "RECOMENDACIÓN: Solicitar datos adicionales al centro educativo y/o familia"))
                (assert (factor "Información incompleta"))
            )
        """)
        
        # REGLA 5: Desprotección del menor (PRIORIDAD 100)
        self.env.build("""
            (defrule desproteccion-menor
                (declare (salience 100))
                (caso si ?intens ?siso ?colab ?ant si ?sit completa)
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Intervención ETI urgente" "Alto - Desprotección"))
                (assert (explicacion "ALERTA: Detectados INDICADORES DE DESPROTECCIÓN del menor"))
                (assert (explicacion "El nivel de riesgo se eleva de forma INMEDIATA"))
                (assert (explicacion "RECOMENDACIÓN: Intervención urgente del Equipo Técnico de Inclusión (ETI)"))
                (assert (factor "Desprotección del menor"))
            )
        """)
        
        # REGLA 6: Seguimiento (Riesgo bajo) (PRIORIDAD 10)
        self.env.build("""
            (defrule seguimiento-riesgo-bajo
                (declare (salience 10))
                (caso si baja ?siso ?colab no no ?sit completa)
                (test (or (eq ?colab alta) (eq ?colab media)))
                (test (<= ?siso 58))
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Seguimiento" "Bajo"))
                (assert (explicacion "Caso de RIESGO BAJO: Faltas esporádicas sin consolidación"))
                (assert (explicacion "La familia muestra colaboración adecuada"))
                (assert (explicacion "RECOMENDACIÓN: Mantener seguimiento ordinario desde el centro educativo"))
                (assert (factor "Intensidad baja"))
                (assert (factor "Familia colaboradora"))
                (assert (factor "Sin antecedentes"))
            )
        """)
        
        # REGLA 7: Intervención preventiva (SISO alto, pocas faltas) (PRIORIDAD 20)
        self.env.build("""
            (defrule intervencion-preventiva
                (declare (salience 20))
                (caso si baja ?siso ?colab no no ?sit completa)
                (test (or (eq ?colab alta) (eq ?colab media)))
                (test (> ?siso 58))
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Intervención ETI (preventiva)" "Preventivo - Vulnerabilidad alta"))
                (assert (explicacion "Aunque las faltas son POCAS, existe VULNERABILIDAD SOCIAL ELEVADA (SISO > 58)"))
                (assert (explicacion "Se recomienda INTERVENCIÓN PREVENTIVA para evitar desprotección futura"))
                (assert (explicacion "RECOMENDACIÓN: Intervención del ETI con enfoque preventivo"))
                (assert (factor "Vulnerabilidad SISO > 58"))
                (assert (factor "Intervención preventiva necesaria"))
            )
        """)
        
        # REGLA 8: Intervención ETI especializada (PRIORIDAD 30)
        self.env.build("""
            (defrule intervencion-eti-especializada
                (declare (salience 30))
                (caso si ?intens ?siso ?colab ?ant no ?sit completa)
                (test (or (eq ?intens media) (eq ?intens alta)))
                (test (> ?siso 58))
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Intervención ETI" "Medio-Alto"))
                (assert (explicacion "RIESGO MEDIO-ALTO: Absentismo consolidado + Vulnerabilidad elevada (SISO > 58)"))
                (assert (explicacion "RECOMENDACIÓN: Intervención del Equipo Técnico de Inclusión (ETI)"))
                (assert (factor "Absentismo consolidado"))
                (assert (factor "Vulnerabilidad SISO > 58"))
            )
        """)
        
        # REGLA 9: No cooperación familiar (PRIORIDAD 40)
        self.env.build("""
            (defrule no-cooperacion-familiar
                (declare (salience 40))
                (caso si ?intens ?siso ?colab ?ant no ?sit completa)
                (test (or (eq ?intens media) (eq ?intens alta)))
                (test (or (eq ?colab baja) (eq ?colab nula)))
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Intervención ETI con valoración de derivación" "Alto - No cooperación familiar"))
                (assert (explicacion "RIESGO ALTO: Absentismo consolidado + NO COOPERACIÓN FAMILIAR"))
                (assert (explicacion "RECOMENDACIÓN: Intervención ETI. Si persisten faltas tras 3-6 meses, valorar derivación a Fiscalía"))
                (assert (factor "No cooperación familiar"))
                (assert (factor "Riesgo de derivación judicial"))
            )
        """)
        
        # REGLA 10: Equipo de familia (PRIORIDAD 25)
        self.env.build("""
            (defrule equipo-familia
                (declare (salience 25))
                (caso si ?intens ?siso ?colab ?ant no ?sit completa)
                (test (or (eq ?intens media) (eq ?intens alta)))
                (test (<= ?siso 58))
                (test (or (eq ?colab alta) (eq ?colab media)))
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Equipo de familia" "Medio"))
                (assert (explicacion "RIESGO MEDIO: Absentismo consolidado pero vulnerabilidad moderada (SISO <= 58)"))
                (assert (explicacion "La familia muestra disposición a colaborar"))
                (assert (explicacion "RECOMENDACIÓN: Derivar a Equipo de Familia para intervención ordinaria"))
                (assert (factor "Absentismo consolidado"))
                (assert (factor "Familia colaboradora"))
            )
        """)
        
        # REGLA DEFAULT: Valoración individualizada (PRIORIDAD 0)
        self.env.build("""
            (defrule valoracion-individualizada
                (declare (salience 0))
                (caso si ?intens ?siso ?colab ?ant no ?sit completa)
                (not (resultado ?rec ?nivel))
                =>
                (assert (resultado "Valoración individualizada" "Requiere análisis específico"))
                (assert (explicacion "Este caso no coincide exactamente con los patrones predefinidos"))
                (assert (explicacion "RECOMENDACIÓN: Realizar valoración individualizada por el equipo técnico"))
            )
        """)
    
    def valorar_caso(self,
                     intervencion_previa_centro: str,
                     intensidad_absentismo: str,
                     siso: int,
                     colaboracion_familiar: str,
                     antecedentes: str,
                     desproteccion: str,
                     situacion_personal: str,
                     estado_informacion: str) -> Dict:
        """
        Valora un caso de absentismo escolar usando el motor CLIPS con vectores ordenados
        
        Returns:
            Dict con recomendación, nivel de riesgo, explicación y factores activados
        """
        
        # Resetear el entorno
        self.env.reset()
        
        # Crear el hecho como VECTOR ORDENADO
        # Formato: (caso intervencion intensidad siso colaboracion antecedentes desproteccion situacion estado)
        fact_string = f"(caso {intervencion_previa_centro} {intensidad_absentismo} {siso} {colaboracion_familiar} {antecedentes} {desproteccion} {situacion_personal} {estado_informacion})"
        
        self.env.assert_string(fact_string)
        
        # Ejecutar el motor de inferencia
        self.env.run()
        
        # Extraer resultados
        recomendacion = "No se pudo determinar"
        nivel_riesgo = "No determinado"
        explicaciones = []
        factores = []
        
        for fact in self.env.facts():
            fact_str = str(fact)
            
            # Resultado: (resultado "recomendacion" "nivel-riesgo")
            if fact_str.startswith("(resultado "):
                parts = fact_str[11:-1].split('" "')
                if len(parts) >= 2:
                    recomendacion = parts[0].strip('"')
                    nivel_riesgo = parts[1].strip('"')
            
            # Explicación: (explicacion "texto")
            elif fact_str.startswith("(explicacion "):
                explicacion_text = fact_str[13:-1].strip('"')
                explicaciones.append(explicacion_text)
            
            # Factor: (factor "texto")
            elif fact_str.startswith("(factor "):
                factor_text = fact_str[8:-1].strip('"')
                factores.append(factor_text)
        
        return {
            'recomendacion': recomendacion,
            'nivel_riesgo': nivel_riesgo,
            'explicacion': explicaciones if explicaciones else ["No se generó explicación"],
            'factores_activados': factores if factores else []
        }


def valorar_caso(
    intervencion_previa_centro: str,
    intensidad_absentismo: str,
    siso: int,
    colaboracion_familiar: str,
    antecedentes: str,
    desproteccion: str,
    situacion_personal: str,
    estado_informacion: str
) -> Dict:
    """Función de conveniencia para valorar un caso"""
    sistema = SistemaAbsentismoEscolar()
    return sistema.valorar_caso(
        intervencion_previa_centro,
        intensidad_absentismo,
        siso,
        colaboracion_familiar,
        antecedentes,
        desproteccion,
        situacion_personal,
        estado_informacion
    )
