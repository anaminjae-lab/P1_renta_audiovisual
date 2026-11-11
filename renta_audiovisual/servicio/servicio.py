"""E15–E16 y E12. Fachada única del dominio Renta de equipo audiovisual.

Referencias: p23_contexto3.py (``__enter__``/``__exit__``), jerarquia13.py
(clase anidada ``Monitor``), thread07.py (hilo como clase), construccion09.py.
"""

import threading
from collections.abc import Callable
from datetime import date
from pathlib import Path
from types import TracebackType
from typing import ClassVar

from ..concurrencia.tarea import TareaPeriodica
from ..eventos.oyentes import Oyente
from ..modelo.actor import Productora
from ..modelo.catalogo import Inventario
from ..modelo.elemento import Equipo
from ..modelo.transaccion import Renta
from ..persistencia import respaldo
from ..persistencia.conexion import abrir
from ..persistencia.repositorios import (
    RepositorioEquipo,
    RepositorioProductora,
    RepositorioRenta,
)


class ServicioRentas:
    """Fachada: casos de uso, eventos, monitor y reportes."""

    PLAZO: ClassVar[int] = 3
    """Días máximos que una renta puede permanecer EN_CURSO."""

    class Monitor(TareaPeriodica):
        """Hilo vigilante: clase anidada con referencia explícita a su servicio."""

        def __init__(self, servicio: "ServicioRentas", periodo: float) -> None:
            # TODO E12: implementar `ServicioRentas.Monitor.__init__`
            raise NotImplementedError

        def ejecutar(self) -> None:
            # TODO E12: implementar `ServicioRentas.Monitor.ejecutar`
            raise NotImplementedError

    def __init__(
        self,
        ruta_bd: str = ":memory:",
        reloj: Callable[[], date] = date.today,
    ) -> None:
        """``reloj`` inyectable para pruebas deterministas."""
        self._ruta_bd = ruta_bd
        self._reloj = reloj
        self._oyentes: list[Oyente] = []
        self._candado = threading.Lock()
        self._monitor: ServicioRentas.Monitor | None = None
        self.catalogo = Inventario()

    # ---------------------------------------------------------------- ciclo de vida
    def __enter__(self) -> "ServicioRentas":
        # TODO E15: implementar `ServicioRentas.__enter__`
        raise NotImplementedError

    def __exit__(
        self,
        tipo: type[BaseException] | None,
        valor: BaseException | None,
        traza: TracebackType | None,
    ) -> None:
        # TODO E15: implementar `ServicioRentas.__exit__`
        raise NotImplementedError

    # ---------------------------------------------------------------- eventos
    def suscribir(self, oyente: Oyente) -> None:
        # TODO E15: implementar `ServicioRentas.suscribir`
        raise NotImplementedError

    def _emitir(self, evento: str, detalle: str) -> None:
        # TODO E15: implementar `ServicioRentas._emitir`
        raise NotImplementedError

    # ---------------------------------------------------------------- casos de uso
    def registrar_equipo(self, equipo: Equipo) -> None:
        # TODO E15: implementar `ServicioRentas.registrar_equipo`
        raise NotImplementedError

    def registrar_productora(self, productora: Productora) -> None:
        # TODO E15: implementar `ServicioRentas.registrar_productora`
        raise NotImplementedError

    def productoras(self) -> list[Productora]:
        # TODO E15: implementar `ServicioRentas.productoras`
        raise NotImplementedError

    def abrir(self, clave_productora: str) -> Renta:
        """Abre una renta con la fecha del reloj inyectado."""
        # TODO E15: implementar `ServicioRentas.abrir`
        raise NotImplementedError

    def agregar_linea(self, clave_renta: str, clave_equipo: str, dias: int) -> Renta:
        # TODO E15: implementar `ServicioRentas.agregar_linea`
        raise NotImplementedError

    def cambiar_estado(self, clave_renta: str, nuevo: str) -> Renta:
        # TODO E15: implementar `ServicioRentas.cambiar_estado`
        raise NotImplementedError

    def rentas(self, estado: str | None = None) -> list[Renta]:
        """Todas o sólo las del estado indicado."""
        # TODO E15: implementar `ServicioRentas.rentas`
        raise NotImplementedError

    def _requerir(self, clave: str) -> Renta:
        # TODO E15: implementar `ServicioRentas._requerir`
        raise NotImplementedError

    # ---------------------------------------------------------------- monitor
    def revisar(self) -> tuple[int, int]:
        """Reglas del monitor; devuelve (canceladas, alertas emitidas).

        1. ABIERTA sin líneas con antigüedad >= 1 día → CANCELADA.
        2. EN_CURSO con antigüedad > PLAZO y sin alerta previa → alerta ÚNICA
           (el indicador ``alertada`` se persiste).
        """
        # TODO E12: implementar `ServicioRentas.revisar`
        raise NotImplementedError

    def iniciar_monitor(self, periodo: float = 60.0) -> None:
        # TODO E12: implementar `ServicioRentas.iniciar_monitor`
        raise NotImplementedError

    def detener_monitor(self) -> None:
        # TODO E12: implementar `ServicioRentas.detener_monitor`
        raise NotImplementedError

    @property
    def monitor(self) -> "ServicioRentas.Monitor | None":
        return self._monitor

    # ---------------------------------------------------------------- respaldo
    def respaldar(self, ruta: str | Path) -> int:
        # TODO E14: implementar `ServicioRentas.respaldar`
        raise NotImplementedError

    # ---------------------------------------------------------------- reportes
    def conteo_por_estado(self) -> dict[str, int]:
        """Número de rentas por estado (los 4 estados siempre presentes)."""
        # TODO E16: implementar `ServicioRentas.conteo_por_estado`
        raise NotImplementedError

    def ingresos_por_tipo(self) -> dict[str, float]:
        """Suma de importes de rentas CERRADAS agrupada por tipo de equipo."""
        # TODO E16: implementar `ServicioRentas.ingresos_por_tipo`
        raise NotImplementedError

    def top_equipos(self, n: int = 3) -> list[tuple[str, int]]:
        """Los ``n`` equipos más usados (clave, días acumulados), descendente."""
        # TODO E16: implementar `ServicioRentas.top_equipos`
        raise NotImplementedError

    def ticket_promedio(self) -> float:
        """Promedio del total de las rentas CERRADAS (0.0 si no hay)."""
        # TODO E16: implementar `ServicioRentas.ticket_promedio`
        raise NotImplementedError
