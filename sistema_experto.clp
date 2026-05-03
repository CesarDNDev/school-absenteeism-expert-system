;;;============================================================================
;;; Sistema Experto INTERACTIVO para Absentismo Escolar en Adolescentes
;;; Implementación en CLIPS puro con PREGUNTAS AL USUARIO
;;; Autor: César Domínguez Notario
;;; Módulo: Modelos de Inteligencia Artificial
;;; Curso: 2025-2026
;;;============================================================================

;;;============================================================================
;;; TEMPLATES PARA ALMACENAR RESPUESTAS
;;;============================================================================

(deftemplate respuesta
    (slot pregunta (type SYMBOL))
    (slot valor)
)

;;;============================================================================
;;; REGLAS PARA HACER PREGUNTAS
;;;============================================================================

;;; Regla inicial - Bienvenida
(defrule inicio
    (declare (salience 1000))
    (not (respuesta (pregunta inicio)))
    =>
    (printout t crlf)
    (printout t "========================================" crlf)
    (printout t "SISTEMA EXPERTO DE ABSENTISMO ESCOLAR" crlf)
    (printout t "========================================" crlf)
    (printout t crlf)
    (assert (respuesta (pregunta inicio) (valor si)))
)

;;; PREGUNTA 1: Intervención previa del centro
(defrule pregunta-intervencion
    (declare (salience 900))
    (respuesta (pregunta inicio) (valor si))
    (not (respuesta (pregunta intervencion)))
    =>
    (printout t "PREGUNTA 1: Intervencion previa del centro" crlf)
    (printout t "¿El centro educativo ha realizado intervencion previa?" crlf)
    (printout t "Respuesta (si/no): ")
    (bind ?resp (read))
    (assert (respuesta (pregunta intervencion) (valor ?resp)))
    (printout t crlf)
)

;;; Si no hay intervención previa, terminar
(defrule sin-intervencion-terminar
    (declare (salience 850))
    (respuesta (pregunta intervencion) (valor no))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Ampliar informacion" crlf)
    (printout t "Nivel de riesgo: No valorable" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- El centro educativo NO ha realizado intervencion previa" crlf)
    (printout t "- RECOMENDACION: Solicitar al centro que realice actuacion inicial" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; PREGUNTA 2: Estado de la información
(defrule pregunta-estado-informacion
    (declare (salience 800))
    (respuesta (pregunta intervencion) (valor si))
    (not (respuesta (pregunta estado-info)))
    =>
    (printout t "PREGUNTA 2: Estado de la informacion" crlf)
    (printout t "¿Como es la informacion disponible?" crlf)
    (printout t "Opciones: completa / incompleta / contradictoria" crlf)
    (printout t "Respuesta: ")
    (bind ?resp (read))
    (assert (respuesta (pregunta estado-info) (valor ?resp)))
    (printout t crlf)
)

;;; Si información incompleta o contradictoria, terminar
(defrule informacion-no-completa-terminar
    (declare (salience 750))
    (respuesta (pregunta estado-info) (valor ?estado))
    (test (or (eq ?estado incompleta) (eq ?estado contradictoria)))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Ampliar informacion" crlf)
    (printout t "Nivel de riesgo: No valorable" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (if (eq ?estado incompleta)
        then (printout t "- La informacion disponible es INCOMPLETA" crlf)
             (printout t "- RECOMENDACION: Solicitar datos adicionales" crlf)
        else (printout t "- La informacion disponible es CONTRADICTORIA" crlf)
             (printout t "- RECOMENDACION: Contactar con equipo de atencion primaria" crlf)
    )
    (printout t "========================================" crlf)
    (halt)
)

;;; PREGUNTA 3: Situación personal
(defrule pregunta-situacion-personal
    (declare (salience 700))
    (respuesta (pregunta estado-info) (valor completa))
    (not (respuesta (pregunta situacion)))
    =>
    (printout t "PREGUNTA 3: Situacion personal del menor" crlf)
    (printout t "¿Presenta alguna de estas situaciones?" crlf)
    (printout t "1. sin_indicadores" crlf)
    (printout t "2. salud_mental_grave" crlf)
    (printout t "3. psicopatologia" crlf)
    (printout t "4. consumo_sustancias" crlf)
    (printout t "5. conducta_disruptiva" crlf)
    (printout t "Respuesta: ")
    (bind ?resp (read))
    (assert (respuesta (pregunta situacion) (valor ?resp)))
    (printout t crlf)
)

;;; Si situación compleja, terminar
(defrule situacion-compleja-terminar
    (declare (salience 650))
    (respuesta (pregunta situacion) (valor ?sit))
    (test (or (eq ?sit salud_mental_grave) 
              (eq ?sit psicopatologia) 
              (eq ?sit consumo_sustancias)))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Revision manual obligatoria" crlf)
    (printout t "Nivel de riesgo: Requiere valoracion especializada" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- CASO COMPLEJO: Detectados indicadores que requieren" crlf)
    (printout t "  valoracion especializada" crlf)
    (printout t "- Este caso queda FUERA del sistema experto automatico" crlf)
    (printout t "- RECOMENDACION: Derivar a revision manual" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; PREGUNTA 4: Desprotección
(defrule pregunta-desproteccion
    (declare (salience 600))
    (respuesta (pregunta situacion) (valor ?sit))
    (test (or (eq ?sit sin_indicadores) (eq ?sit conducta_disruptiva)))
    (not (respuesta (pregunta desproteccion)))
    =>
    (printout t "PREGUNTA 4: Indicadores de desproteccion" crlf)
    (printout t "¿Se detectan indicadores de desproteccion del menor?" crlf)
    (printout t "Respuesta (si/no): ")
    (bind ?resp (read))
    (assert (respuesta (pregunta desproteccion) (valor ?resp)))
    (printout t crlf)
)

;;; Si hay desprotección, terminar
(defrule desproteccion-terminar
    (declare (salience 550))
    (respuesta (pregunta desproteccion) (valor si))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Intervencion ETI urgente" crlf)
    (printout t "Nivel de riesgo: Alto - Desproteccion" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- ALERTA: Detectados INDICADORES DE DESPROTECCION" crlf)
    (printout t "- El nivel de riesgo se eleva de forma INMEDIATA" crlf)
    (printout t "- RECOMENDACION: Intervencion urgente del ETI" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; PREGUNTA 5: Intensidad del absentismo
(defrule pregunta-intensidad
    (declare (salience 500))
    (respuesta (pregunta desproteccion) (valor no))
    (not (respuesta (pregunta intensidad)))
    =>
    (printout t "PREGUNTA 5: Intensidad del absentismo" crlf)
    (printout t "¿Cual es la intensidad de las faltas?" crlf)
    (printout t "Opciones: baja / media / alta" crlf)
    (printout t "Respuesta: ")
    (bind ?resp (read))
    (assert (respuesta (pregunta intensidad) (valor ?resp)))
    (printout t crlf)
)

;;; PREGUNTA 6: Puntuación SISO
(defrule pregunta-siso
    (declare (salience 400))
    (respuesta (pregunta intensidad))
    (not (respuesta (pregunta siso)))
    =>
    (printout t "PREGUNTA 6: Vulnerabilidad social (SISO)" crlf)
    (printout t "Puntuacion SISO del caso (0-100):" crlf)
    (printout t "Umbral critico: 58 puntos" crlf)
    (printout t "Respuesta: ")
    (bind ?resp (read))
    (assert (respuesta (pregunta siso) (valor ?resp)))
    (printout t crlf)
)

;;; PREGUNTA 7: Colaboración familiar
(defrule pregunta-colaboracion
    (declare (salience 300))
    (respuesta (pregunta siso))
    (not (respuesta (pregunta colaboracion)))
    =>
    (printout t "PREGUNTA 7: Colaboracion familiar" crlf)
    (printout t "¿Cual es el nivel de colaboracion de la familia?" crlf)
    (printout t "Opciones: nula / baja / media / alta" crlf)
    (printout t "Respuesta: ")
    (bind ?resp (read))
    (assert (respuesta (pregunta colaboracion) (valor ?resp)))
    (printout t crlf)
)

;;; PREGUNTA 8: Antecedentes
(defrule pregunta-antecedentes
    (declare (salience 200))
    (respuesta (pregunta colaboracion))
    (not (respuesta (pregunta antecedentes)))
    =>
    (printout t "PREGUNTA 8: Antecedentes" crlf)
    (printout t "¿Existen antecedentes de absentismo en este menor?" crlf)
    (printout t "Respuesta (si/no): ")
    (bind ?resp (read))
    (assert (respuesta (pregunta antecedentes) (valor ?resp)))
    (printout t crlf)
)

;;;============================================================================
;;; REGLAS DE DECISIÓN FINAL
;;;============================================================================

;;; Seguimiento (Riesgo bajo)
(defrule decision-seguimiento
    (declare (salience 100))
    (respuesta (pregunta intensidad) (valor baja))
    (respuesta (pregunta siso) (valor ?siso))
    (respuesta (pregunta colaboracion) (valor ?colab))
    (respuesta (pregunta antecedentes) (valor no))
    (test (<= ?siso 58))
    (test (or (eq ?colab alta) (eq ?colab media)))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Seguimiento" crlf)
    (printout t "Nivel de riesgo: Bajo" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- Caso de RIESGO BAJO: Faltas esporadicas" crlf)
    (printout t "- La familia muestra colaboracion adecuada" crlf)
    (printout t "- RECOMENDACION: Mantener seguimiento ordinario" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; Intervención preventiva
(defrule decision-preventiva
    (declare (salience 100))
    (respuesta (pregunta intensidad) (valor baja))
    (respuesta (pregunta siso) (valor ?siso))
    (respuesta (pregunta colaboracion) (valor ?colab))
    (respuesta (pregunta antecedentes) (valor no))
    (test (> ?siso 58))
    (test (or (eq ?colab alta) (eq ?colab media)))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Intervencion ETI (preventiva)" crlf)
    (printout t "Nivel de riesgo: Preventivo - Vulnerabilidad alta" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- Aunque las faltas son POCAS, existe VULNERABILIDAD" crlf)
    (printout t "  SOCIAL ELEVADA (SISO > 58)" crlf)
    (printout t "- RECOMENDACION: Intervencion del ETI preventiva" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; Intervención ETI especializada
(defrule decision-eti
    (declare (salience 100))
    (respuesta (pregunta intensidad) (valor ?intens))
    (respuesta (pregunta siso) (valor ?siso))
    (test (or (eq ?intens media) (eq ?intens alta)))
    (test (> ?siso 58))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Intervencion ETI" crlf)
    (printout t "Nivel de riesgo: Medio-Alto" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- RIESGO MEDIO-ALTO: Absentismo consolidado +" crlf)
    (printout t "  Vulnerabilidad elevada (SISO > 58)" crlf)
    (printout t "- RECOMENDACION: Intervencion del ETI" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; No cooperación familiar
(defrule decision-no-cooperacion
    (declare (salience 100))
    (respuesta (pregunta intensidad) (valor ?intens))
    (respuesta (pregunta colaboracion) (valor ?colab))
    (test (or (eq ?intens media) (eq ?intens alta)))
    (test (or (eq ?colab baja) (eq ?colab nula)))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Intervencion ETI con valoracion de derivacion" crlf)
    (printout t "Nivel de riesgo: Alto - No cooperacion familiar" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- RIESGO ALTO: Absentismo consolidado +" crlf)
    (printout t "  NO COOPERACION FAMILIAR" crlf)
    (printout t "- RECOMENDACION: Intervencion ETI. Si persisten" crlf)
    (printout t "  faltas tras 3-6 meses, valorar derivacion a Fiscalia" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; Equipo de familia
(defrule decision-familia
    (declare (salience 100))
    (respuesta (pregunta intensidad) (valor ?intens))
    (respuesta (pregunta siso) (valor ?siso))
    (respuesta (pregunta colaboracion) (valor ?colab))
    (test (or (eq ?intens media) (eq ?intens alta)))
    (test (<= ?siso 58))
    (test (or (eq ?colab alta) (eq ?colab media)))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Equipo de familia" crlf)
    (printout t "Nivel de riesgo: Medio" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- RIESGO MEDIO: Absentismo consolidado pero" crlf)
    (printout t "  vulnerabilidad moderada (SISO <= 58)" crlf)
    (printout t "- La familia muestra disposicion a colaborar" crlf)
    (printout t "- RECOMENDACION: Derivar a Equipo de Familia" crlf)
    (printout t "========================================" crlf)
    (halt)
)

;;; REGLA POR DEFECTO - Se activa si ninguna otra regla coincide
(defrule decision-default
    (declare (salience 50))
    (respuesta (pregunta antecedentes))
    =>
    (printout t "========================================" crlf)
    (printout t "RESULTADO" crlf)
    (printout t "========================================" crlf)
    (printout t "Recomendacion: Valoracion individualizada" crlf)
    (printout t "Nivel de riesgo: Requiere analisis especifico" crlf)
    (printout t crlf)
    (printout t "EXPLICACION:" crlf)
    (printout t "- Este caso no coincide exactamente con los" crlf)
    (printout t "  patrones predefinidos" crlf)
    (printout t "- RECOMENDACION: Realizar valoracion individualizada" crlf)
    (printout t "  por el equipo tecnico" crlf)
    (printout t "========================================" crlf)
    (halt)
)
