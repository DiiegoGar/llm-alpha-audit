"""
Descarga de datos de mercado (gratuitos) para la auditoría.

Dos fuentes, ambas públicas:
  1. Precios OHLCV diarios de componentes del S&P 500  -> Yahoo Finance (yfinance)
  2. Factores Fama-French (Mkt-RF, SMB, HML, RMW, CMA, RF) -> Kenneth French Data Library

Uso:
    python -m src.data.download --config configs/data.yaml

El objetivo de diseño es que TODO sea reproducible con datos que cualquiera
puede obtener sin coste ni credenciales de pago.
"""

from __future__ import annotations

import argparse
from pathlib import Path

# import yaml
# import yfinance as yf
# import pandas as pd
# from pandas_datareader.famafrench import get_available_datasets, FamaFrenchReader


def download_prices(tickers: list[str], start: str, end: str, out_dir: Path):
    """Descarga OHLCV diario para una lista de tickers y lo guarda en data/raw/.

    TODO:
      - Descargar con yfinance en lotes (evitar rate limits).
      - Guardar un CSV por ticker o un panel único parquet.
      - Registrar qué tickers fallaron (deslistados, etc.).
    """
    raise NotImplementedError


def download_factors(start: str, end: str, out_dir: Path):
    """Descarga las series diarias de factores Fama-French (3 y 5 factores).

    TODO:
      - Usar pandas_datareader para tirar de la Kenneth French Library.
      - Alinear el calendario con el de los precios.
      - Guardar en data/factors/ff5_daily.csv.
    """
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description="Descarga precios y factores")
    parser.add_argument("--config", required=True, help="Ruta al YAML de configuración")
    args = parser.parse_args()

    # TODO: cargar config, llamar a download_prices y download_factors
    print(f"[download] leyendo config desde {args.config}")
    print("[download] TODO: implementar descarga")


if __name__ == "__main__":
    main()
