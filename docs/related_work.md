# Contexto académico y trabajo relacionado

Este proyecto se sitúa en la literatura reciente sobre evaluación de agentes de
trading basados en LLM. El propósito de este documento es doble: dar crédito a
los trabajos de los que parte la metodología, y dejar claro cuál es el ángulo
propio de esta auditoría.

## El problema que motiva el proyecto

La evaluación ingenua de un agente de trading LLM ("ponlo en un mercado
histórico y mide cuánto gana") es vulnerable a tres fallos bien documentados:

1. **Confusión alpha/beta.** Los retornos positivos pueden venir de exposición
   pasiva a factores (mercado, tamaño, value) en lugar de habilidad de selección.
   El instrumental clásico para separarlos es el modelo de factores de
   Fama-French (3 factores, 1993; 5 factores, 2015).

2. **Fuga de información / look-ahead bias.** Los backtests largos solapan con
   el knowledge cutoff del modelo, permitiendo que tickers, fechas y narrativas
   memorizadas sustituyan al razonamiento inversor. Trabajos recientes proponen
   protocolos de masking consistente para controlarlo.

3. **Crisis de reproducibilidad.** Los LLM producen decisiones distintas entre
   ejecuciones incluso con decodificación determinista, lo que hace poco fiables
   las evaluaciones de una sola pasada.

## Familias de trabajo relacionadas

- **Benchmarks de agentes de trading LLM**: evalúan si estos agentes operan de
  forma rentable en mercados realistas, con entornos de back-trading y
  arquitecturas multi-agente.
- **Control de fuga de información**: benchmarks que anonimizan identificadores
  y controlan el knowledge cutoff, y que muestran que buena parte del
  rendimiento aparente se explica por exposición a factores más que por alpha.
- **Reproducibilidad y supuestos de ejecución**: revisiones que codifican qué
  detalles (costes, timing, versión del modelo, release de prompts) determinan
  la validez de una afirmación de rendimiento.
- **Frameworks de agentes open-source**: sistemas proof-of-concept multi-agente
  que sirven como sujetos de la auditoría (modo simulación).

> Nota de trazabilidad: las referencias bibliográficas completas (con autores,
> año y enlace) se añaden aquí a medida que se fichan en la Fase 1. Cada
> afirmación metodológica del proyecto debe poder rastrearse a una fuente
> concreta o marcarse explícitamente como supuesto propio a validar.

## Qué aporta este proyecto

No propone un agente nuevo ni un benchmark nuevo. Aporta una **auditoría
reproducible con datos 100% gratuitos** que combina los tres controles
anteriores (atribución de factores + test de fuga + test de estabilidad) sobre
agentes ya existentes, con el objetivo de responder de forma directa: ¿el
rendimiento reportado es habilidad transferible o exposición pasiva a factores?
