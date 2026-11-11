# Renta de equipo audiovisual — ESQUELETO para el estudiante

Miniproyecto individual de 4 semanas · Tecnologías de Programación · Maestría en Sistemas
Computacionales · TecNM, Instituto Tecnológico de Orizaba.

## Dominio
Una casa de renta de equipo audiovisual presta cámaras, luminarias y equipo de audio a productoras por días. Requiere controlar inventario, rentas, descuentos por nivel de cliente y detectar rentas que excedan el plazo pactado.

| Elemento | Concreción |
|---|---|
| Base abstracta | `Equipo` |
| Subtipos | `Camara` [CAM], `Iluminacion` [ILU], `Audio` [AUD] |
| Capacidades | `Asegurable`, `Transportable` (recargos por deducir: §6 del DOCX) |
| Actor | `Productora` [PRD] con niveles BASICO / PLATA / ORO |
| Transacción | `Renta` [REN] con `Renta.Linea` anidada |
| Catálogo | `Inventario` |
| Fachada | `ServicioRentas` (plazo: 3 días) |

## Instrucciones
```bash
python3.13 -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"            # agrega ,web si usas NiceGUI
pytest                              # 14 pruebas de aceptación (pruebas_modelo.py)
ruff check . && mypy                # calidad: ambos sin errores
python -m renta_audiovisual.app datos.db   # crea la base de demostración
python -m renta_audiovisual.ui.<tu_ui>     # ejecuta tu interfaz
```

## Video de demostración (OBLIGATORIO)
Enlace: **<pega aquí el enlace al video de máximo 5 minutos>**

## Justificación de la tecnología de UI
<Explica qué tecnología elegiste, por qué, y cómo llevas los eventos del hilo monitor al hilo de UI.>

## Decisiones de diseño
<Describe al menos 5 decisiones: p. ej. por qué `Linea` es anidada, cómo resolviste la colisión de
`recargo()`, por qué `Nivel` es Singleton, cómo garantizas que la UI no ejecuta SQL.>

## Decisiones deducidas (pensamiento crítico)
<La especificación NO da las fórmulas cerradas: da ejemplos resueltos (§6 del DOCX) y las pruebas
comparan huellas selladas. Para cada constante o regla deducida (ESCALA de cada subtipo, recargos,
regla de colisión, descuentos, tabla de transiciones, tabla `lineas`), escribe: hipótesis inicial,
ejemplos con los que la contrastaste, prueba que la confirmó y, si la hubo, la respuesta errónea de
un LLM y cómo la detectaste.>

## Capturas
<Inserta capturas de la UI mostrando los 4 estados y una alerta del monitor.>

## Requisitos de entrega
1. Todo en Git salvo el video (su enlace va arriba).
2. Al menos un commit por grupo E02–E16 y etiquetas `s1`, `s2`, `s3`.
3. Diagrama de clases ACTUALIZADO en `diagramas/` y `BITACORA_IA.md` completa.
4. `datos.db` con ≥ 6 equipos, 3 productoras y 4 rentas (una por estado).
5. El docente ejecutará SU copia original de `pruebas_modelo.py`.
