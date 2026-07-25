# Fundamentos: lo que necesitas entender antes de programar

Esta guía cubre los tres conceptos sobre los que gira toda la auditoría. Está
escrita para leerse de una sentada. Si entiendes esto, entiendes el 90% de tu
propio proyecto — y puedes defenderlo en una entrevista.

---

## 1. Alpha vs. Beta: la distinción que lo es todo

Imagina que un amigo presume de haber ganado un 20% invirtiendo este año. Antes
de admirarlo, hazte una pregunta: **¿cuánto subió el mercado entero ese año?**

Si el mercado subió un 20%, tu amigo no hizo nada especial. Podría haber
comprado un fondo índice barato, irse a la playa, y obtener lo mismo. Su
rentabilidad no vino de habilidad, vino de **estar dentro del mercado**.

Esta es la distinción central de todas las finanzas de inversión:

- **Beta (β)** = la parte de tu rentabilidad que viene de exposición al mercado.
  Es "gratis" en el sentido de que no requiere habilidad: solo requiere estar
  invertido. Si el mercado sube, tú subes; si baja, bajas. Un beta de 1 significa
  que te mueves igual que el mercado. Un beta de 1.5 significa que amplificas sus
  movimientos (más riesgo).

- **Alpha (α)** = la parte de tu rentabilidad que NO se explica por el mercado.
  Es el rendimiento extra atribuible a habilidad real: elegir bien qué comprar,
  cuándo entrar y salir. Alpha es lo escaso, lo valioso, lo que justifica pagar
  a un gestor.

**Por qué esto es el corazón de tu proyecto:** cuando un agente de trading LLM
"gana dinero", la pregunta que nadie se hace es si ese dinero es alpha (habilidad
del agente) o beta (simplemente estaba largo en un mercado que subía). Tu
auditoría existe para separar las dos cosas. Si toda la ganancia del agente es
beta, entonces el agente no aporta nada que un ETF de 5€ no diera ya.

> **Analogía para la entrevista:** un surfista que llega lejos puede ser muy
> bueno (alpha) o puede que simplemente venía una ola enorme que empujaba a todos
> (beta). Para saber si es bueno, tienes que medir cuánto avanzó *más allá* de lo
> que la ola explicaba.

---

## 2. Factores Fama-French: beta, pero más fino

En los años 90, dos economistas (Eugene Fama y Kenneth French) descubrieron algo
incómodo: gran parte de lo que parecía "habilidad" de los gestores no era alpha,
era exposición a un puñado de **factores** sistemáticos. Es decir: había más
tipos de "beta" de los que se creía.

Los factores clásicos (modelo de 3 factores):

1. **Mercado (Mkt-RF)** — el beta clásico: exposición al mercado en su conjunto,
   por encima del tipo sin riesgo.
2. **Tamaño (SMB, "Small Minus Big")** — históricamente, las empresas pequeñas
   han rendido distinto a las grandes. Si tu cartera carga en small caps, parte
   de tu rentabilidad viene de este factor, no de tu genialidad.
3. **Valor (HML, "High Minus Low")** — las empresas "baratas" (value) rinden
   distinto a las "caras" (growth). Otra fuente de rentabilidad sistemática.

El modelo de 5 factores añade dos más: **rentabilidad operativa (RMW)** e
**inversión (CMA)**.

**La idea clave:** un gestor puede parecer brillante simplemente porque su cartera
está cargada de acciones pequeñas y baratas en un año en que esos factores
funcionaron. Eso no es alpha: es beta a factores conocidos, replicable por
cualquiera sin talento especial.

**Cómo lo usa tu proyecto:** coges la serie de rentabilidades de un agente LLM y
la "explicas" con estos factores mediante una regresión:

```
retorno_agente - tipo_sin_riesgo  =  α  +  β_mkt·Mercado  +  β_smb·SMB  +  β_hml·HML  +  ...  +  error
```

Lo que buscas es el **α (el intercepto)**. Si tras controlar por todos los
factores, α es estadísticamente indistinguible de cero, tu conclusión es
demoledora y honesta: *el agente no genera habilidad; su rendimiento es
exposición a factores que cualquiera puede replicar.* Si α es positivo y
significativo, el agente aporta algo real y eso también es un hallazgo valioso.

> Los factores Fama-French son **públicos y gratuitos** en la Kenneth French Data
> Library. No necesitas Bloomberg. Por eso tu proyecto es 100% reproducible.

---

## 3. Look-ahead bias y fuga de información: cómo un LLM "hace trampa"

**Look-ahead bias** es usar, al tomar una decisión en una fecha pasada,
información que en esa fecha todavía no existía. Es la trampa clásica de todo
backtest: si en tu simulación de enero de 2023 el agente "sabe" cómo cerró el año,
sus resultados son ficción.

Con agentes LLM hay una versión especialmente traicionera: **fuga por
memorización**. Un LLM se entrenó con textos de internet hasta cierta fecha (su
*knowledge cutoff*). Si le pides que "analice" una acción en un periodo que cae
DENTRO de su entrenamiento, puede que no esté analizando los datos que le das:
puede estar **recordando** lo que leyó sobre esa empresa y ese periodo. Sabe que
la acción X subió en 2023 porque lo memorizó, no porque lo dedujera.

Eso infla artificialmente su rendimiento y no se transfiere al futuro real, donde
no hay nada memorizado que recordar.

**Cómo lo caza tu proyecto (módulo `leakage/`):** evalúas al agente dos veces con
los mismos datos numéricos, pero:
- una vez con los **nombres reales** (AAPL, fechas reales),
- otra vez **anonimizado** (ASSET_07, fechas desplazadas).

Si el agente decide bien con los nombres reales pero se desmorona cuando los
ocultas, estaba tirando de memoria, no de análisis. Ese contraste es una de las
evidencias más contundentes que puedes presentar.

---

## 4. Por qué la reproducibilidad importa (y por qué es un hallazgo, no un detalle)

Los LLM pueden dar respuestas distintas cada vez que los ejecutas, incluso con la
configuración fijada para ser determinista. Esto significa que un resultado de
**una sola ejecución** no demuestra nada: podría ser suerte de esa corrida.

Tu módulo `reproducibility/` ejecuta el mismo agente N veces y mide cuánto varían
los resultados. Si oscilan mucho, ningún número aislado es fiable. Para una
audiencia de finanzas serias, señalar esto es señal de madurez: no te tragas un
buen resultado sin comprobar que es estable.

---

## Resumen en una frase

Tu proyecto coge agentes de trading LLM y les hace tres preguntas que sus propios
autores no suelen hacerse: **(1)** ¿tu rentabilidad es alpha o solo beta a
factores conocidos?, **(2)** ¿analizas de verdad o recuerdas lo que memorizaste?,
y **(3)** ¿tus resultados se repiten o son ruido de una sola corrida? Responder
esto con rigor y datos gratuitos es exactamente el tipo de escepticismo empírico
que valora un banco de inversión o una business school.

---

## Para profundizar (opcional, por tu cuenta)

- Modelo de 3 factores: Fama & French (1993).
- Modelo de 5 factores: Fama & French (2015).
- Datos de factores: Kenneth French Data Library (búscala; es gratuita).
- Conceptos de backtesting y look-ahead bias: cualquier manual de finanzas
  cuantitativas los cubre en el capítulo de evaluación de estrategias.
