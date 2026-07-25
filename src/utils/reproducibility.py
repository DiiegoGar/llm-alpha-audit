"""
Utilidades para que cada experimento sea trazable y reproducible.

Dos principios que un reclutador técnico valora inmediatamente:
  1. Toda ejecución guarda su configuración y su seed.
  2. Ningún resultado existe sin un registro de cómo se generó.
"""

from __future__ import annotations

import json
import random
from datetime import datetime
from pathlib import Path

# import numpy as np


def set_all_seeds(seed: int):
    """Fija las semillas de todas las fuentes de aleatoriedad relevantes.

    Nota: los LLM vía API pueden seguir siendo no deterministas aunque se fije
    la seed local; precisamente por eso existe el módulo de reproducibilidad,
    que mide esa variabilidad en lugar de asumir que no existe.
    """
    random.seed(seed)
    # np.random.seed(seed)


def log_experiment(results_dir: Path, config: dict, metrics: dict, seed: int):
    """Guarda un registro JSON de un experimento: config + seed + métricas + timestamp.

    Esto es lo que hace que los resultados sean auditables por terceros.
    """
    results_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    record = {
        "timestamp_utc": stamp,
        "seed": seed,
        "config": config,
        "metrics": metrics,
    }
    out = results_dir / f"run_{stamp}_seed{seed}.json"
    out.write_text(json.dumps(record, indent=2))
    return out
