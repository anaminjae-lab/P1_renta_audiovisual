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

Para el desarrollo de la interfaz gráfica del sistema de renta de equipo audiovisual se seleccionó **Tkinter con ttk**, utilizando Python 3.13.

La elección fue en base a los siguientes aspectos:

1. **Integración con Python:** Tkinter forma parte de la biblioteca estándar de Python, por lo que no requiere instalar un framework gráfico adicional.

2. **Componentes de interfaz:** el módulo `ttk` proporciona widgets temáticos como botones, formularios, listas y `Treeview`, que permitirán visualizar el inventario, las productoras y las rentas.

3. **Separación de responsabilidades:** la interfaz se comunicará exclusivamente con `app.controlador`, evitando incluir consultas SQL o reglas de negocio en las ventanas.

4. **Manejo de concurrencia:** los eventos generados por el monitor se recibirán mediante una cola y se procesarán desde el hilo de la interfaz utilizando `root.after(500, sondear)`, de acuerdo con la especificación del proyecto.

5. **Mantenimiento y aprendizaje:** esta tecnología permite desarrollar una aplicación de escritorio sin introducir la complejidad adicional de un servidor web, facilitando la comprensión del código.

**Conclusión:** Tkinter con ttk cumple los requisitos de interfaz establecidos para el miniproyecto y permite concentrar el desarrollo en el modelo de objetos, la persistencia y la concurrencia.

**Referencia:** Python Software Foundation. *tkinter — Python interface to Tcl/Tk*. Documentación oficial de Python 3.13. https://docs.python.org/3.13/library/tkinter.html

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
