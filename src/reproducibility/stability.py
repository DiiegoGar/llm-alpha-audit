"""
Test de reproducibilidad / estabilidad entre ejecuciones.

Los LLM producen salidas distintas entre corridas, a veces incluso con
decodificación determinista (temperatura 0). Una evaluación de una sola pasada
puede, por tanto, ser estadísticamente poco fiable.

Este módulo ejecuta el MISMO agente con la MISMA configuración N veces y mide
cuánto varían tanto las decisiones como las métricas finales. Un agente cuyos
resultados oscilan mucho entre corridas no ofrece evidencia sólida de habilidad,
por muy bueno que sea el número de una única ejecución.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StabilityReport:
    """Resumen de dispersión entre N ejecuciones."""
    n_runs: int
    return_mean: float
    return_std: float
    return_ci95: tuple[float, float]     # intervalo de confianza 95%
    decision_agreement: float            # % medio de coincidencia de decisiones entre pares de corridas

    def is_stable(self, cv_threshold: float = 0.25) -> bool:
        """Heurística: estable si el coeficiente de variación de los retornos
        está por debajo del umbral."""
        if self.return_mean == 0:
            return False
        return abs(self.return_std / self.return_mean) < cv_threshold


def run_repeated(agent_run_fn, config: dict, n_runs: int, base_seed: int):
    """Ejecuta el agente n_runs veces variando solo la seed, recogiendo
    la serie de retornos y las decisiones de cada corrida.

    TODO:
      - Bucle de n_runs con seeds derivadas de base_seed.
      - Guardar cada corrida en results/ con su seed y config (trazabilidad).
      - Devolver la colección de resultados para analizar.
    """
    raise NotImplementedError


def analyze_stability(runs) -> "StabilityReport":
    """Calcula media, desviación, IC95% y grado de acuerdo entre decisiones.

    TODO: implementar el cálculo de dispersión y el acuerdo par a par.
    """
    raise NotImplementedError
