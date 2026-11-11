# TODO — Renta de equipo audiovisual

Total: **146** tareas en 16 grupos.

| Grupo | Tema | Tareas | Semana |
|---|---|---|---|
| E01 | Configuración del proyecto | 3 | 1 |
| E02 | Contrato raíz (abstracción) | 4 | 1 |
| E03 | Clave (identidad) | 3 | 1 |
| E04 | Clase base abstracta | 7 | 1 |
| E05 | Subtipos y capacidades (herencia múltiple) | 30 | 2 |
| E06 | Actor y niveles (Singleton) | 15 | 2 |
| E07 | Transacción, estados y composición | 16 | 2 |
| E08 | Totales | 4 | 2 |
| E09 | Catálogo (agregación) | 8 | 3 |
| E10 | Tipos anidados y locales | 1 | 3 |
| E11 | Programación funcional | 8 | 3 |
| E12 | Concurrencia y monitor | 8 | 3 |
| E13 | Persistencia SQLite | 15 | 4 |
| E14 | Respaldo pickle | 5 | 4 |
| E15 | Servicio y eventos | 15 | 4 |
| E16 | Reportes | 4 | 4 |

## Detalle

| Grupo | Archivo | Línea | Tarea |
|---|---|---|---|
| E01 | `pyproject.toml` | 6 | escribe tu nombre y correo institucional |
| E01 | `pyproject.toml` | 11 | conserva sólo la tecnología de UI que elijas (tkinter viene con Python) |
| E01 | `renta_audiovisual/__init__.py` | 13 | implementar `info` |
| E02 | `renta_audiovisual/modelo/contrato.py` | 25 | implementar `Tarifable.cotizar` |
| E02 | `renta_audiovisual/modelo/contrato.py` | 30 | implementar `Tarifable.cotizar_con_iva` |
| E02 | `renta_audiovisual/modelo/contrato.py` | 40 | implementar `Tarifable.redondear` |
| E02 | `renta_audiovisual/modelo/contrato.py` | 46 | implementar `Tarifable.moneda` |
| E03 | `renta_audiovisual/modelo/clave.py` | 20 | implementar `Clave.es_valida` |
| E03 | `renta_audiovisual/modelo/clave.py` | 30 | implementar `Clave.siguiente` |
| E03 | `renta_audiovisual/modelo/clave.py` | 36 | implementar `Clave.registrar` |
| E04 | `renta_audiovisual/modelo/elemento.py` | 23 | implementar `Equipo.__init__` |
| E04 | `renta_audiovisual/modelo/elemento.py` | 29 | implementar `Equipo.clave` |
| E04 | `renta_audiovisual/modelo/elemento.py` | 35 | implementar `Equipo.nombre` |
| E04 | `renta_audiovisual/modelo/elemento.py` | 40 | implementar `Equipo.nombre` |
| E04 | `renta_audiovisual/modelo/elemento.py` | 46 | implementar `Equipo.precio_base` |
| E04 | `renta_audiovisual/modelo/elemento.py` | 51 | implementar `Equipo.precio_base` |
| E04 | `renta_audiovisual/modelo/elemento.py` | 73 | implementar `Equipo._calcular` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 78 | implementar `Equipo.copiar` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 90 | implementar `Equipo.crear` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 112 | valor por deducir de los ejemplos (§6) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 115 | implementar `Asegurable.recargo` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 119 | implementar `Asegurable.etiquetas` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 126 | valor por deducir de los ejemplos (§6) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 129 | implementar `Transportable.recargo` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 133 | implementar `Transportable.etiquetas` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 140 | declarar las capacidades que hereda y su orden (§6 y prueba 05) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 145 | valor por deducir de los ejemplos (§6) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 148 | implementar `Camara.__init__` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 154 | implementar `Camara.resolucion_mp` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 159 | implementar `Camara.resolucion_mp` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 164 | implementar `Camara.factor` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 168 | implementar `Camara.valor_atributo` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 175 | declarar las capacidades que hereda y su orden (§6 y prueba 05) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 180 | valor por deducir de los ejemplos (§6) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 183 | implementar `Iluminacion.__init__` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 189 | implementar `Iluminacion.potencia_w` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 194 | implementar `Iluminacion.potencia_w` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 199 | implementar `Iluminacion.factor` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 203 | implementar `Iluminacion.valor_atributo` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 210 | declarar las capacidades que hereda y su orden (§6 y prueba 05) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 215 | valor por deducir de los ejemplos (§6) |
| E05 | `renta_audiovisual/modelo/elemento.py` | 218 | implementar `Audio.__init__` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 224 | implementar `Audio.canales` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 229 | implementar `Audio.canales` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 234 | implementar `Audio.factor` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 238 | implementar `Audio.valor_atributo` |
| E05 | `renta_audiovisual/modelo/elemento.py` | 243 | implementar `Audio.recargo` |
| E06 | `renta_audiovisual/modelo/actor.py` | 22 | implementar `Nivel.__new__` |
| E06 | `renta_audiovisual/modelo/actor.py` | 32 | implementar `Nivel.desde_nombre` |
| E06 | `renta_audiovisual/modelo/actor.py` | 46 | implementar `Basico.descuento` |
| E06 | `renta_audiovisual/modelo/actor.py` | 57 | implementar `Plata.descuento` |
| E06 | `renta_audiovisual/modelo/actor.py` | 68 | implementar `Oro.descuento` |
| E06 | `renta_audiovisual/modelo/actor.py` | 81 | implementar `Productora.__init__` |
| E06 | `renta_audiovisual/modelo/actor.py` | 87 | implementar `Productora.desde_texto` |
| E06 | `renta_audiovisual/modelo/actor.py` | 92 | implementar `Productora.clave` |
| E06 | `renta_audiovisual/modelo/actor.py` | 97 | implementar `Productora.nombre` |
| E06 | `renta_audiovisual/modelo/actor.py` | 102 | implementar `Productora.nombre` |
| E06 | `renta_audiovisual/modelo/actor.py` | 107 | implementar `Productora.correo` |
| E06 | `renta_audiovisual/modelo/actor.py` | 112 | implementar `Productora.correo` |
| E06 | `renta_audiovisual/modelo/actor.py` | 117 | implementar `Productora.nivel` |
| E06 | `renta_audiovisual/modelo/actor.py` | 122 | implementar `Productora.nivel` |
| E06 | `renta_audiovisual/modelo/actor.py` | 127 | implementar `Productora.descuento` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 26 | traducir el diagrama de estados (§6) a una tabla de transiciones |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 33 | implementar `Renta.Linea.__init__` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 39 | implementar `Renta.Linea.contenedora` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 44 | implementar `Renta.Linea.equipo` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 49 | implementar `Renta.Linea.dias` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 65 | implementar `Renta.__init__` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 70 | implementar `Renta.clave` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 75 | implementar `Renta.productora` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 80 | implementar `Renta.fecha` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 85 | implementar `Renta.estado` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 91 | implementar `Renta.lineas` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 96 | implementar `Renta.agregar` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 101 | implementar `Renta._restaurar_linea` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 110 | implementar `Renta.cambiar_estado` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 115 | implementar `Renta.antiguedad` |
| E07 | `renta_audiovisual/modelo/transaccion.py` | 144 | implementar `Renta.__str__` |
| E08 | `renta_audiovisual/modelo/transaccion.py` | 54 | implementar `Renta.Linea.importe` |
| E08 | `renta_audiovisual/modelo/transaccion.py` | 120 | implementar `Renta.subtotal` |
| E08 | `renta_audiovisual/modelo/transaccion.py` | 125 | implementar `Renta.descuento` |
| E08 | `renta_audiovisual/modelo/transaccion.py` | 130 | implementar `Renta.total` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 15 | implementar `Inventario.__init__` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 20 | implementar `Inventario.agregar` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 25 | implementar `Inventario.obtener` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 29 | implementar `Inventario.quitar` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 34 | implementar `Inventario.todos` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 38 | implementar `Inventario.__len__` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 47 | implementar `Inventario.buscar` |
| E09 | `renta_audiovisual/modelo/catalogo.py` | 52 | implementar `Inventario.ordenados` |
| E10 | `renta_audiovisual/modelo/catalogo.py` | 67 | implementar `Inventario.resumen_por_tipo` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 23 | implementar `Regla.__call__` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 28 | implementar `Regla.y` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 33 | implementar `Regla.o` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 38 | implementar `Regla.negar` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 47 | implementar `precio_maximo` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 53 | implementar `de_tipo` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 59 | implementar `filtrar` |
| E11 | `renta_audiovisual/funcional/reglas.py` | 65 | implementar `aplicar` |
| E12 | `renta_audiovisual/concurrencia/tarea.py` | 15 | implementar `TareaPeriodica.__init__` |
| E12 | `renta_audiovisual/concurrencia/tarea.py` | 20 | implementar `TareaPeriodica.run` |
| E12 | `renta_audiovisual/concurrencia/tarea.py` | 25 | implementar `TareaPeriodica.detener` |
| E12 | `renta_audiovisual/servicio/servicio.py` | 39 | implementar `ServicioRentas.Monitor.__init__` |
| E12 | `renta_audiovisual/servicio/servicio.py` | 43 | implementar `ServicioRentas.Monitor.ejecutar` |
| E12 | `renta_audiovisual/servicio/servicio.py` | 125 | implementar `ServicioRentas.revisar` |
| E12 | `renta_audiovisual/servicio/servicio.py` | 129 | implementar `ServicioRentas.iniciar_monitor` |
| E12 | `renta_audiovisual/servicio/servicio.py` | 133 | implementar `ServicioRentas.detener_monitor` |
| E13 | `renta_audiovisual/persistencia/conexion.py` | 42 | implementar `abrir` |
| E13 | `renta_audiovisual/persistencia/conexion.py` | 49 | implementar `transaccion` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 55 | implementar `RepositorioEquipo.guardar` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 60 | implementar `RepositorioEquipo.guardar_varios` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 64 | implementar `RepositorioEquipo.obtener` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 68 | implementar `RepositorioEquipo.todos` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 73 | implementar `RepositorioEquipo._mapear` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 81 | implementar `RepositorioProductora.guardar` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 85 | implementar `RepositorioProductora.obtener` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 89 | implementar `RepositorioProductora.todos` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 93 | implementar `RepositorioProductora._mapear` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 112 | implementar `RepositorioRenta.guardar` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 116 | implementar `RepositorioRenta.obtener` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 120 | implementar `RepositorioRenta.todos` |
| E13 | `renta_audiovisual/persistencia/repositorios.py` | 125 | implementar `RepositorioRenta._mapear` |
| E14 | `renta_audiovisual/modelo/transaccion.py` | 135 | implementar `Renta.__getstate__` |
| E14 | `renta_audiovisual/modelo/transaccion.py` | 140 | implementar `Renta.__setstate__` |
| E14 | `renta_audiovisual/persistencia/respaldo.py` | 16 | implementar `respaldar` |
| E14 | `renta_audiovisual/persistencia/respaldo.py` | 26 | implementar `restaurar` |
| E14 | `renta_audiovisual/servicio/servicio.py` | 142 | implementar `ServicioRentas.respaldar` |
| E15 | `renta_audiovisual/eventos/oyentes.py` | 26 | implementar `OyenteMemoria.notificar` |
| E15 | `renta_audiovisual/eventos/oyentes.py` | 37 | implementar `OyenteCola.notificar` |
| E15 | `renta_audiovisual/eventos/oyentes.py` | 42 | implementar `OyenteCola.pendientes` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 61 | implementar `ServicioRentas.__enter__` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 70 | implementar `ServicioRentas.__exit__` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 75 | implementar `ServicioRentas.suscribir` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 79 | implementar `ServicioRentas._emitir` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 84 | implementar `ServicioRentas.registrar_equipo` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 88 | implementar `ServicioRentas.registrar_productora` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 92 | implementar `ServicioRentas.productoras` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 97 | implementar `ServicioRentas.abrir` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 101 | implementar `ServicioRentas.agregar_linea` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 105 | implementar `ServicioRentas.cambiar_estado` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 110 | implementar `ServicioRentas.rentas` |
| E15 | `renta_audiovisual/servicio/servicio.py` | 114 | implementar `ServicioRentas._requerir` |
| E16 | `renta_audiovisual/servicio/servicio.py` | 148 | implementar `ServicioRentas.conteo_por_estado` |
| E16 | `renta_audiovisual/servicio/servicio.py` | 153 | implementar `ServicioRentas.ingresos_por_tipo` |
| E16 | `renta_audiovisual/servicio/servicio.py` | 158 | implementar `ServicioRentas.top_equipos` |
| E16 | `renta_audiovisual/servicio/servicio.py` | 163 | implementar `ServicioRentas.ticket_promedio` |
