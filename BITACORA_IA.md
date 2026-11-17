# Bitácora de uso de IA — Renta de equipo audiovisual

El uso de asistentes de IA está **permitido y debe declararse**. Esta bitácora no se califica por
la cantidad de uso, sino por la **calidad de tu juicio**: qué pediste, qué recibiste, qué estaba mal
y cómo lo comprobaste. Sin bitácora, todo código se considera no declarado.

## 1. Registro de interacciones

| # | Fecha | Grupo | Herramienta | Qué pediste (resumen del prompt) | Qué aceptaste / rechazaste / modificaste y por qué | Evidencia de verificación (prueba, mypy, traza, ejecución) |
|---|---|---|---|---|---|---|
| 1 | 2026-11-11 | E01.2 | ChatGPT | Ventajas y desventajas de cada tecnología. | Se eligió Tkinter + ttk por su integración con Python y sus componentes gráficos. | Se ejecutó py -3.13 -m tkinter y se abrió la ventana de prueba.|
| 2 | 2026-11-16 | E02 | ChatGPT | Explicación de los métodos ya implementados en contrato.py e implementación de Tarifable. | Acepté utilizar cotizar() para validar los días y delegar el cálculo a _calcular(), porque permite que cada subtipo defina su tarifa sin repetir la validación. | contrato.py; pruebas manuales: 900.0, 1044.0, 125.68 y MXN. pytest: 14 fallidas por TODO de grupos posteriores. |
| 3 | 2026-11-16 | E03 | ChatGPT | Explicación e implementación paso a paso de Clave.siguiente() y Clave.registrar()| Acepté la validación del formato PPP-0000, los contadores independientes por prefijo, el uso de threading.Lock y max() para impedir retrocesos. Corregí un error de transcripción en la comparación de letras. Rechacé ejecutar pruebas generales que fallarían por implementaciones pendientes | Pruebas manuales: es_valida() → True, False, False; siguiente() → CAM-0001, CAM-0002, AUD-0001; registrar() → CAM-0026, CAM-0027, AUD-0001. Pendientes: pruebas oficiales y concurrencia. |
## 2. Contraejemplos: errores del LLM que detectaste (mínimo 3)

Para cada uno: la afirmación o el código del LLM, por qué era incorrecto según el modelo de objetos
de Booch o la especificación, cómo lo detectaste (prueba sellada, mypy, traza manual) y la corrección.

| # | Grupo | Lo que propuso el LLM | Por qué era incorrecto | Cómo lo detectaste | Corrección aplicada |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

## 3. Deducciones propias (sin IA)

Constantes y reglas que dedujiste de los ejemplos de la especificación (ESCALA, recargos, regla de
colisión, descuentos, transiciones, tabla `lineas`): procedimiento seguido y prueba que lo confirmó.

| Elemento | Hipótesis | Ejemplos usados | Resultado de la prueba |
|---|---|---|---|
| | | | |

## 4. Declaración

Declaro que puedo explicar y modificar, sin asistencia, cada línea de este repositorio.

Nombre: ______________________  Número de control: ____________  Fecha: __________
