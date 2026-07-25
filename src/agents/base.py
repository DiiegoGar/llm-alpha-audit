"""
Interfaz común para los agentes de trading que auditamos.

No implementamos un agente propio: envolvemos agentes existentes (open-source)
detrás de una interfaz uniforme para poder auditarlos todos igual. Cada agente
concreto (p. ej. un framework multi-agente estilo "AI Hedge Fund") se adapta
implementando esta interfaz.

Regla de oro del proyecto: SIMULACIÓN ÚNICAMENTE. Ningún agente ejecuta
operaciones reales ni mueve dinero. Solo produce decisiones sobre datos
históricos.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"


@dataclass
class Decision:
    """Decisión del agente para un activo en una fecha dada."""
    date: str
    asset: str
    action: Action
    weight: float          # peso objetivo en cartera (0..1)
    rationale: str = ""    # razonamiento del agente (útil para el test de fuga)


class TradingAgent(ABC):
    """Interfaz que todo agente auditado debe implementar."""

    def __init__(self, name: str, config: dict, seed: int):
        self.name = name
        self.config = config
        self.seed = seed

    @abstractmethod
    def decide(self, market_view) -> list[Decision]:
        """Dado el estado de mercado observable en una fecha (SOLO información
        point-in-time, nada del futuro), devuelve decisiones de cartera.

        La implementación concreta llamará al LLM del framework subyacente.
        """
        raise NotImplementedError

    def reset(self):
        """Reinicia el estado interno del agente entre ejecuciones."""
        pass
