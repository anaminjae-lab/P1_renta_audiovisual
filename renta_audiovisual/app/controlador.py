"""Capa de aplicación: puerto único entre la UI y el servicio.

La UI (escritorio o web) SÓLO importa este módulo: recibe y entrega tipos
simples (``str``, ``int``, ``float``, ``dict``) y nunca toca ``sqlite3``.
"""

from datetime import date, timedelta

from ..eventos.oyentes import OyenteCola
from ..modelo.actor import Nivel, Productora
from ..modelo.elemento import Equipo
from ..servicio.servicio import ServicioRentas

Fila = dict[str, str]

TIPOS: dict[str, str] = {
    "CAM": "Camara (resolucion_mp)",
    "ILU": "Iluminacion (potencia_w)",
    "AUD": "Audio (canales)",
}
ESTADOS: tuple[str, ...] = ("ABIERTA", "EN_CURSO", "CERRADA", "CANCELADA")


class Controlador:
    """Adaptador de la UI: traduce eventos de interfaz a casos de uso."""

    def __init__(self, servicio: ServicioRentas) -> None:
        self._s = servicio
        self.eventos = OyenteCola()
        servicio.suscribir(self.eventos)

    def equipos(self) -> list[Fila]:
        return [
            {
                "clave": e.clave,
                "tipo": e.tipo,
                "nombre": e.nombre,
                "precio": f"{e.precio_base:.2f}",
                "atributo": str(e.valor_atributo()),
            }
            for e in self._s.catalogo.ordenados("clave")
        ]

    def productoras(self) -> list[Fila]:
        return [
            {"clave": a.clave, "nombre": a.nombre, "correo": a.correo, "nivel": str(a.nivel)}
            for a in self._s.productoras()
        ]

    def rentas(self) -> list[Fila]:
        return [
            {
                "clave": t.clave,
                "productora": t.productora.nombre,
                "fecha": t.fecha.isoformat(),
                "estado": t.estado,
                "lineas": str(len(t.lineas)),
                "total": f"{t.total():.2f}",
            }
            for t in self._s.rentas()
        ]

    def alta_equipo(self, tipo: str, nombre: str, precio: float, valor: int) -> str:
        e = Equipo.crear(tipo, nombre, precio, valor)
        self._s.registrar_equipo(e)
        return e.clave

    def alta_productora(self, nombre: str, correo: str, nivel: str) -> str:
        a = Productora(nombre, correo, Nivel.desde_nombre(nivel))
        self._s.registrar_productora(a)
        return a.clave

    def abrir(self, clave_productora: str) -> str:
        return self._s.abrir(clave_productora).clave

    def agregar(self, clave_renta: str, clave_equipo: str, dias: int) -> None:
        self._s.agregar_linea(clave_renta, clave_equipo, dias)

    def cambiar(self, clave_renta: str, estado: str) -> None:
        self._s.cambiar_estado(clave_renta, estado)

    def revisar(self) -> tuple[int, int]:
        return self._s.revisar()

    def reportes(self) -> dict[str, str]:
        return {
            "Conteo por estado": str(self._s.conteo_por_estado()),
            "Ingresos por tipo": str(self._s.ingresos_por_tipo()),
            "Top equipos": str(self._s.top_equipos()),
            "Ticket promedio": f"{self._s.ticket_promedio():.2f}",
        }

    def pendientes(self) -> list[str]:
        """Eventos acumulados por otros hilos (se consumen en el hilo de la UI)."""
        return [f"{e}: {d}" for e, d in self.eventos.pendientes()]


def poblar_demo(servicio: ServicioRentas) -> None:
    """Datos mínimos exigidos: 6 equipos, 3 productoras y 4 rentas (una por estado)."""
    if servicio.catalogo.todos():
        return
    ejemplos = [
        Equipo.crear("CAM", "Cámara RED Komodo", 1800.0, 60),
        Equipo.crear("CAM", "Cámara Sony FX3", 950.0, 12),
        Equipo.crear("ILU", "Panel LED Aputure", 400.0, 300),
        Equipo.crear("ILU", "Fresnel ARRI 1K", 350.0, 1000),
        Equipo.crear("AUD", "Consola Zoom F8", 600.0, 8),
        Equipo.crear("AUD", "Kit de lavalieres", 250.0, 4),
    ]
    for e in ejemplos:
        servicio.registrar_equipo(e)
    actores = [
        Productora.desde_texto("Cine Orizaba;cine0@ejemplo.mx;BASICO"),
        Productora.desde_texto("Producciones Pico;producciones1@ejemplo.mx;PLATA"),
        Productora.desde_texto("Estudio Citlaltépetl;estudio2@ejemplo.mx;ORO"),
    ]
    for a in actores:
        servicio.registrar_productora(a)
    abierta = servicio.abrir(actores[0].clave)
    servicio.agregar_linea(abierta.clave, ejemplos[0].clave, 1)
    en_curso = servicio.abrir(actores[1].clave)
    servicio.agregar_linea(en_curso.clave, ejemplos[2].clave, 2)
    servicio.cambiar_estado(en_curso.clave, "EN_CURSO")
    cerrada = servicio.abrir(actores[2].clave)
    servicio.agregar_linea(cerrada.clave, ejemplos[4].clave, 3)
    servicio.agregar_linea(cerrada.clave, ejemplos[1].clave, 1)
    servicio.cambiar_estado(cerrada.clave, "EN_CURSO")
    servicio.cambiar_estado(cerrada.clave, "CERRADA")
    cancelada = servicio.abrir(actores[0].clave)
    servicio.cambiar_estado(cancelada.clave, "CANCELADA")


def reloj_demo() -> date:
    """Reloj de ejemplo desplazado; útil para observar el monitor en la UI."""
    return date.today() + timedelta(days=ServicioRentas.PLAZO + 1)
