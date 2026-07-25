"""
Atribución de rendimiento por factores: el corazón de la auditoría.

Toma la serie de retornos (en exceso) de un agente y la descompone en:
  - exposición al mercado (beta de mercado)
  - exposición a estilo (SMB = tamaño, HML = value, y opc. RMW/CMA)
  - alpha residual = lo que NO explican los factores

La pregunta central del proyecto se responde aquí: si alpha no es
estadísticamente distinto de cero tras controlar por factores, el "rendimiento"
del agente es exposición pasiva a factores, no habilidad inversora.

Referencia metodológica: modelo de 3 factores (Fama & French, 1993) y
de 5 factores (Fama & French, 2015). Errores estándar robustos a
autocorrelación y heterocedasticidad (Newey-West).
"""

from __future__ import annotations

from dataclasses import dataclass

# import numpy as np
# import pandas as pd
# import statsmodels.api as sm


@dataclass
class AttributionResult:
    """Resultado de una regresión de factores para un agente."""
    alpha: float                 # intercepto (alpha anualizado)
    alpha_tstat: float           # t-stat del alpha (¿es significativo?)
    alpha_pvalue: float
    betas: dict[str, float]      # coeficiente por factor
    r_squared: float             # cuánto explican los factores
    n_obs: int

    def alpha_is_significant(self, level: float = 0.05) -> bool:
        """True si el alpha es estadísticamente distinto de cero."""
        return self.alpha_pvalue < level


def run_factor_regression(
    agent_excess_returns,   # pd.Series indexada por fecha
    factors,                # pd.DataFrame con columnas Mkt-RF, SMB, HML, [RMW, CMA]
    model: str = "ff5",     # "ff3" o "ff5"
) -> "AttributionResult":
    """Regresa los retornos en exceso del agente sobre los factores.

    r_agent - rf = alpha + b_mkt*(Mkt-RF) + b_smb*SMB + b_hml*HML [+ ...] + e

    TODO:
      - Alinear fechas agente/factores.
      - Seleccionar columnas según `model`.
      - Ajustar OLS con statsmodels y errores Newey-West.
      - Anualizar el alpha y empaquetar en AttributionResult.
    """
    raise NotImplementedError


def summarize_attribution(result: "AttributionResult") -> str:
    """Devuelve un resumen legible del tipo:
    'Alpha anualizado 2.1% (t=0.8, no significativo). El 94% de la varianza
     se explica por exposición a mercado y estilo.'
    """
    raise NotImplementedError
