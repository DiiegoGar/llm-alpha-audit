# LLM Alpha Audit

**¿La rentabilidad de los agentes de trading basados en LLM es habilidad real (alpha) o simplemente exposición a factores de mercado conocidos (beta)?**

Este proyecto no construye otro agente de trading. Coge agentes de trading basados en LLM que **ya existen** y les aplica el instrumental de las finanzas académicas para responder una única pregunta incómoda: cuando uno de estos agentes "gana al mercado", ¿es porque tiene criterio inversor transferible, o porque está capturando de forma pasiva factores de riesgo que cualquiera puede replicar con un ETF barato?

La respuesta corta de la literatura reciente es descorazonadora: buena parte del supuesto *alpha* se explica por exposición a mercado y estilo, con poca evidencia de selección de valores persistente. Este repositorio construye una auditoría **reproducible y con datos 100% gratuitos** para verificarlo de primera mano.

---

## Por qué existe este proyecto

La evaluación habitual de un agente de trading LLM se reduce a: ponlo en un mercado histórico, déjalo operar, mide cuánto gana. Ese enfoque tiene tres agujeros que este proyecto ataca de frente:

1. **Confunde beta con alpha.** Ganar dinero en un mercado alcista no es habilidad; es estar largo. La única forma de aislar la habilidad real es descomponer la rentabilidad en sus fuentes (mercado, estilo, selección) con un modelo de factores.

2. **Sufre fuga de información.** Los backtests largos solapan con el *knowledge cutoff* del modelo. Si el agente "sabe" que cierto ticker subió en 2023 porque lo memorizó durante su entrenamiento, no está analizando: está recordando.

3. **No es reproducible.** Los LLM producen decisiones distintas entre ejecuciones incluso con decodificación determinista. Una sola pasada no demuestra nada.

Este proyecto implementa una auditoría en tres frentes, uno por cada agujero.

---

## Qué hace la auditoría

| Módulo | Pregunta que responde | Método |
|---|---|---|
| **Atribución de factores** | ¿Cuánto del retorno es alpha genuino? | Regresión Fama-French (3 y 5 factores) sobre la serie de retornos del agente |
| **Test de fuga de información** | ¿El agente analiza o recuerda? | Anonimización de tickers y fechas; comparación de decisiones con/sin identificadores |
| **Test de reproducibilidad** | ¿Los resultados son estables? | N ejecuciones con misma configuración; dispersión de decisiones y métricas |

El hallazgo central que busca demostrar: **si el alpha se evapora al controlar por factores, si las decisiones cambian al ocultar los nombres, y si los resultados no se replican entre corridas, entonces el "rendimiento" reportado no es evidencia de habilidad inversora.**

---

## Datos (todos gratuitos y públicos)

- **Precios**: OHLCV diario de componentes del S&P 500 vía Yahoo Finance.
- **Factores**: series diarias de Fama-French (mercado, SMB, HML, RMW, CMA) desde la [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).
- **Agentes**: frameworks de agentes de trading LLM open-source (modo simulación, sin ejecución real).

Ninguna parte del proyecto requiere Bloomberg, CRSP ni datos de pago. Cualquiera puede reproducirlo.

---

## Estructura del repositorio

```
llm-alpha-audit/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── configs/                 # Configuración de experimentos (YAML)
├── data/
│   ├── raw/                 # Precios descargados (no versionado)
│   ├── processed/           # Retornos y paneles limpios
│   └── factors/             # Series Fama-French
├── src/
│   ├── data/                # Descarga y limpieza de precios y factores
│   ├── agents/              # Wrappers de los agentes LLM (modo simulación)
│   ├── attribution/         # Regresión de factores y descomposición de alpha
│   ├── leakage/             # Anonimización y test de fuga de información
│   ├── reproducibility/     # Ejecuciones repetidas y análisis de dispersión
│   └── utils/               # Logging, seeds, helpers
├── notebooks/               # Análisis narrados (la "historia" del proyecto)
├── reports/
│   └── figures/             # Gráficos finales para el informe
├── results/                 # Salidas de experimentos (métricas, tablas)
└── tests/                   # Tests unitarios
```

---

## Cómo reproducirlo

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Descargar datos (precios + factores)
python -m src.data.download --config configs/data.yaml

# 3. Ejecutar un agente en modo simulación
python -m src.agents.run --config configs/agent_baseline.yaml

# 4. Correr la auditoría completa
python -m src.attribution.run --config configs/audit.yaml
python -m src.leakage.run --config configs/audit.yaml
python -m src.reproducibility.run --config configs/audit.yaml

# 5. Generar el informe
jupyter notebook notebooks/03_report.ipynb
```

---

## Hallazgos

_(Esta sección se completa con los resultados reales una vez ejecutada la auditoría. Es la parte que un reclutador leerá primero: un párrafo claro + los 2-3 gráficos clave.)_

- **Descomposición alpha vs. beta**: _pendiente_
- **Sensibilidad a fuga de información**: _pendiente_
- **Estabilidad entre ejecuciones**: _pendiente_

---

## Limitaciones

Un proyecto honesto declara sus límites. Este usa datos diarios (no intradía), no modela costes de transacción de forma exhaustiva, y evalúa un número limitado de agentes sobre una ventana temporal acotada. Las conclusiones son indicativas, no definitivas — el objetivo es demostrar una **metodología de auditoría rigurosa**, no emitir un veredicto universal sobre todos los agentes de trading LLM.

---

## Sobre este proyecto

Construido como demostración de tres competencias combinadas: análisis financiero cuantitativo (atribución de factores), ingeniería de sistemas con LLMs, y criterio empírico para auditar afirmaciones de rendimiento en lugar de aceptarlas.

## Contexto académico

Este trabajo se apoya en literatura reciente sobre evaluación de agentes de trading LLM y control de fuga de información. Ver [`docs/related_work.md`](docs/related_work.md) para las referencias completas.
