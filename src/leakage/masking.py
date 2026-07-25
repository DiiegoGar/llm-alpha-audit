"""
Test de fuga de información (information leakage).

Idea: si un agente LLM "acierta" porque memorizó durante su entrenamiento que
cierto ticker subió en cierta fecha, no está analizando — está recordando.

Para separar análisis de memoria, evaluamos al agente dos veces:
  A) Condición IDENTIFICADA:  ve tickers reales y fechas reales.
  B) Condición ANONIMIZADA:   ve los MISMOS datos numéricos (OHLCV) pero con
                              tickers sustituidos por alias y fechas desplazadas.

Si el comportamiento del agente cambia drásticamente entre A y B, sus
decisiones dependían de los identificadores (memoria), no de los datos (análisis).

Inspirado en protocolos de masking consistentes entre prompts y herramientas
usados en benchmarks recientes de agentes de trading LLM controlados por fuga.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MaskingMap:
    """Mapa reversible de anonimización para una ejecución."""
    ticker_alias: dict[str, str]   # AAPL -> ASSET_07
    date_offset_days: int          # desplazamiento aplicado al calendario


def build_masking_map(tickers: list[str], seed: int) -> "MaskingMap":
    """Construye un mapa de alias de tickers y un offset de fechas determinista.

    TODO:
      - Barajar alias de forma reproducible con `seed`.
      - Elegir un offset de fechas que no revele el periodo real.
    """
    raise NotImplementedError


def apply_masking(panel, mapping: "MaskingMap"):
    """Aplica el mapa de anonimización a un panel de datos de mercado.

    Importante: el masking debe ser CONSISTENTE en todo lo que ve el agente
    (prompt, herramientas, memoria), o la fuga se cuela por otra vía.
    """
    raise NotImplementedError


def compare_conditions(decisions_identified, decisions_masked) -> dict:
    """Compara decisiones entre condición identificada y anonimizada.

    Devuelve métricas de divergencia, p. ej.:
      - % de decisiones que cambian de signo (comprar/vender/mantener)
      - correlación entre las series de posiciones
      - caída de rendimiento al anonimizar

    TODO: definir e implementar las métricas de divergencia.
    """
    raise NotImplementedError
