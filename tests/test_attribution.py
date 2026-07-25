"""
Tests del módulo de atribución de factores.

Estrategia clave: probar con datos SINTÉTICOS de propiedades conocidas.
Si construyo una serie de retornos que es EXACTAMENTE 1.0*mercado + ruido cero,
la regresión debe devolver beta_mkt≈1 y alpha≈0. Si construyo una serie con un
alpha inyectado de X, la regresión debe recuperar ≈X. Esto valida que el
instrumento mide lo que dice medir antes de aplicarlo a agentes reales.
"""

import pytest

# from src.attribution.factor_model import run_factor_regression


@pytest.mark.skip(reason="pendiente de implementar run_factor_regression")
def test_recovers_zero_alpha_for_pure_beta():
    """Una cartera que es puro mercado no debe mostrar alpha significativo."""
    # TODO:
    #   - Generar factores sintéticos.
    #   - Construir agent_returns = 1.0 * Mkt-RF + rf (sin alpha).
    #   - Verificar que alpha no es significativo y beta_mkt ≈ 1.
    pass


@pytest.mark.skip(reason="pendiente de implementar run_factor_regression")
def test_recovers_injected_alpha():
    """Si inyecto un alpha conocido, la regresión debe recuperarlo."""
    # TODO:
    #   - agent_returns = 0.0002 (alpha diario) + 1.0 * Mkt-RF + rf.
    #   - Verificar que el alpha estimado ≈ 0.0002 y es significativo.
    pass
