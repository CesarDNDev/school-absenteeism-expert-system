"""
Sistema Experto para Absentismo Escolar
Basado en CLIPS (clipspy)
Autor: César Domínguez Notario
"""

import clips
from typing import Dict, List


class SistemaAbsentismoEscolar:
    """
    Motor de inferencia CLIPS para valoración inicial de casos de absentismo escolar.
    Basado en las reglas extraídas de entrevistas con expertos.
    """
    
    def __init__(self):
        self.env = clips.Environment()
        self.recomendacion = None
        self.nivel_riesgo = None
        self.explicacion = []
        self.factores_activados = []
        self._definir_templates()
        self._definir_reglas()
    
    def _definir_templates(self):
        """Define los templates (plantillas) de hechos en CLIPS"""
        
        # Template para el caso
        self.env.build("""
            (deftemplate caso
                (slot intervencion-previa-centro (type SYMBOL))
                (slot intensidad-absentismo (type SYMBOL))
                (slot siso (type INTEGER))
                (slot colaboracion-familiar (type SYMBOL))
                (slot antecedentes (type SYMBOL))
                (slot desproteccion (type SYMBOL))
                (slot situacion-personal (type SYMBOL))
                (slot estado-informacion (type SYMBOL))
            )
        """)
        
        # Template para resultados
        self.env.build("""
            (deftemplate resultado
                (slot recomendacion (type STRING))
                (slot nivel-riesgo (type STRING))
            )
        """)
    
    def _definir_reglas(self):
        """Define las reglas de producción del sistema experto"""
        
        # REGLA 1: Sin intervención previa del centro
        self.env.build("""
            (defrule sin-intervencion-previa
                (caso (intervencion-previa-centro no))
                =>
                (assert (resultado 
                    (recomendacion "Ampliar información")
                    (nivel-riesgo "No valorable")))
                (assert (explicacion "El centro educativo NO ha realizado intervención previa"))
                (assert (explicacion "RECOMENDACIÓN: Solicitar al centro que realice actuación inicial"))
                (assert (factor "Sin intervención previa del centro"))
            )
        """)
        
        # REGLA 2: Casos que requieren revisión manual (salud mental grave)
        self.env.build("""
            (defrule revision-manual-salud-mental
                (caso (intervencion-previa-centro si)
                      (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias))
                =>
                (assert (resultado 
                    (recomendacion "Revisión manual obligatoria")
                    (nivel-riesgo "Requiere valoración especializada")))
                (assert (explicacion "CASO COMPLEJO: Detectados indicadores que requieren valoración especializada"))
                (assert (explicacion "Este caso queda FUERA del sistema experto automático"))
                (assert (explicacion "RECOMENDACIÓN: Derivar a revisión manual por profesional especializado"))
                (assert (factor "Situación personal compleja"))
            )
        """)
        
        # REGLA 3: Información contradictoria
        self.env.build("""
            (defrule informacion-contradictoria
                (caso (intervencion-previa-centro si)
                      (estado-informacion contradictoria))
                =>
                (assert (resultado 
                    (recomendacion "Ampliar información")
                    (nivel-riesgo "No valorable")))
                (assert (explicacion "La información disponible es CONTRADICTORIA entre fuentes"))
                (assert (explicacion "RECOMENDACIÓN: Contactar con equipo de atención primaria"))
                (assert (factor "Información contradictoria"))
            )
        """)
        
        # REGLA 4: Información incompleta
        self.env.build("""
            (defrule informacion-incompleta
                (caso (intervencion-previa-centro si)
                      (estado-informacion incompleta))
                =>
                (assert (resultado 
                    (recomendacion "Ampliar información")
                    (nivel-riesgo "No valorable")))
                (assert (explicacion "La información disponible es INCOMPLETA"))
                (assert (explicacion "RECOMENDACIÓN: Solicitar datos adicionales al centro educativo"))
                (assert (factor "Información incompleta"))
            )
        """)
        
        # REGLA 5: Desprotección detectada (máxima prioridad)
        self.env.build("""
            (defrule desproteccion-detectada
                (declare (salience 100))
                (caso (intervencion-previa-centro si)
                      (desproteccion si)
                      (estado-informacion completa))
                (not (caso (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias)))
                =>
                (assert (resultado 
                    (recomendacion "Intervención ETI urgente")
                    (nivel-riesgo "Alto - Desprotección")))
                (assert (explicacion "ALERTA: Detectados INDICADORES DE DESPROTECCIÓN del menor"))
                (assert (explicacion "El nivel de riesgo se eleva de forma INMEDIATA"))
                (assert (explicacion "RECOMENDACIÓN: Intervención urgente del Equipo Técnico de Inclusión (ETI)"))
                (assert (factor "Desprotección del menor"))
            )
        """)
        
        # REGLA 6: Seguimiento simple (riesgo bajo)
        self.env.build("""
            (defrule seguimiento-simple
                (caso (intervencion-previa-centro si)
                      (intensidad-absentismo baja)
                      (colaboracion-familiar alta|media)
                      (antecedentes no)
                      (desproteccion no)
                      (estado-informacion completa))
                (not (caso (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias)))
                =>
                (assert (resultado 
                    (recomendacion "Seguimiento")
                    (nivel-riesgo "Bajo")))
                (assert (explicacion "Caso de RIESGO BAJO: Faltas esporádicas sin consolidación"))
                (assert (explicacion "La familia muestra colaboración adecuada"))
                (assert (explicacion "RECOMENDACIÓN: Mantener seguimiento ordinario desde el centro educativo"))
                (assert (factor "Intensidad baja"))
                (assert (factor "Familia colaboradora"))
                (assert (factor "Sin antecedentes"))
            )
        """)
        
        # REGLA 7: Intervención preventiva (SISO alto, pocas faltas)
        self.env.build("""
            (defrule prevencion-vulnerabilidad-alta
                (caso (intervencion-previa-centro si)
                      (intensidad-absentismo baja)
                      (siso ?s&:(> ?s 58))
                      (desproteccion no)
                      (estado-informacion completa))
                (not (caso (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias)))
                =>
                (assert (resultado 
                    (recomendacion "Intervención ETI (preventiva)")
                    (nivel-riesgo "Preventivo - Vulnerabilidad alta")))
                (assert (explicacion "Aunque las faltas son POCAS, existe VULNERABILIDAD SOCIAL ELEVADA (SISO > 58)"))
                (assert (explicacion "Se recomienda INTERVENCIÓN PREVENTIVA para evitar desprotección futura"))
                (assert (explicacion "RECOMENDACIÓN: Intervención del ETI con enfoque preventivo"))
                (assert (factor "Vulnerabilidad SISO > 58"))
                (assert (factor "Intervención preventiva necesaria"))
            )
        """)
        
        # REGLA 8: Intervención ETI especializada (SISO alto + absentismo consolidado)
        self.env.build("""
            (defrule intervencion-eti-especializada
                (caso (intervencion-previa-centro si)
                      (intensidad-absentismo media|alta)
                      (siso ?s&:(> ?s 58))
                      (desproteccion no)
                      (estado-informacion completa))
                (not (caso (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias)))
                =>
                (assert (resultado 
                    (recomendacion "Intervención ETI")
                    (nivel-riesgo "Medio-Alto")))
                (assert (explicacion "RIESGO MEDIO-ALTO: Absentismo consolidado + Vulnerabilidad elevada (SISO > 58)"))
                (assert (explicacion "RECOMENDACIÓN: Intervención del Equipo Técnico de Inclusión (ETI)"))
                (assert (factor "Absentismo consolidado"))
                (assert (factor "Vulnerabilidad SISO > 58"))
            )
        """)
        
        # REGLA 9: No cooperación familiar (riesgo alto)
        self.env.build("""
            (defrule no-cooperacion-familiar
                (caso (intervencion-previa-centro si)
                      (intensidad-absentismo media|alta)
                      (siso ?s&:(<= ?s 58))
                      (colaboracion-familiar baja|nula)
                      (desproteccion no)
                      (estado-informacion completa))
                (not (caso (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias)))
                =>
                (assert (resultado 
                    (recomendacion "Intervención ETI con valoración de derivación")
                    (nivel-riesgo "Alto - No cooperación familiar")))
                (assert (explicacion "RIESGO ALTO: Absentismo consolidado + NO COOPERACIÓN FAMILIAR"))
                (assert (explicacion "RECOMENDACIÓN: Intervención ETI. Si persisten faltas tras 3-6 meses, valorar derivación a Fiscalía"))
                (assert (factor "No cooperación familiar"))
                (assert (factor "Riesgo de derivación judicial"))
            )
        """)
        
        # REGLA 10: Equipo de familia (SISO moderado, familia colabora)
        self.env.build("""
            (defrule equipo-familia
                (caso (intervencion-previa-centro si)
                      (intensidad-absentismo media|alta)
                      (siso ?s&:(<= ?s 58))
                      (colaboracion-familiar alta|media)
                      (desproteccion no)
                      (estado-informacion completa))
                (not (caso (situacion-personal salud_mental_grave|psicopatologia|consumo_sustancias)))
                =>
                (assert (resultado 
                    (recomendacion "Equipo de familia")
                    (nivel-riesgo "Medio")))
                (assert (explicacion "RIESGO MEDIO: Absentismo consolidado pero vulnerabilidad moderada (SISO <= 58)"))
                (assert (explicacion "La familia muestra disposición a colaborar"))
                (assert (explicacion "RECOMENDACIÓN: Derivar a Equipo de Familia para intervención ordinaria"))
                (assert (factor "Absentismo consolidado"))
                (assert (factor "Familia colaboradora"))
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
        Valora un caso de absentismo escolar usando el motor CLIPS
        
        Returns:
            Dict con recomendación, nivel de riesgo, explicación y factores activados
        """
        
        # Resetear el entorno
        self.env.reset()
        
        # Convertir guiones bajos a guiones para CLIPS (mantener formato original)
        situacion_personal_clips = situacion_personal
        
        # Crear el hecho del caso
        fact_string = f"""
            (caso 
                (intervencion-previa-centro {intervencion_previa_centro})
                (intensidad-absentismo {intensidad_absentismo})
                (siso {siso})
                (colaboracion-familiar {colaboracion_familiar})
                (antecedentes {antecedentes})
                (desproteccion {desproteccion})
                (situacion-personal {situacion_personal_clips})
                (estado-informacion {estado_informacion})
            )
        """
        
        self.env.assert_string(fact_string)
        
        # Ejecutar el motor de inferencia
        self.env.run()
        
        # Extraer resultados
        recomendacion = "No se pudo determinar"
        nivel_riesgo = "No determinado"
        explicaciones = []
        factores = []
        
        for fact in self.env.facts():
            if fact.template.name == 'resultado':
                recomendacion = fact['recomendacion']
                nivel_riesgo = fact['nivel-riesgo']
            elif fact.template.name == 'explicacion':
                explicaciones.append(str(fact[0]))
            elif fact.template.name == 'factor':
                factores.append(str(fact[0]))
        
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
