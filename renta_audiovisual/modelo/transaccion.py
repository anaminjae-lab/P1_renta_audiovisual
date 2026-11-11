"""E07–E08 y E14. Transacción con estados, composición de líneas y totales.

Referencias: demo.py y jerarquia13.py (clase anidada), construccion13.py
(la parte la crea el todo), thread07.py (sección crítica), persistencia03.py
(pickle de objetos).
"""

import threading
from datetime import date
from typing import ClassVar

from .actor import Productora
from .clave import Clave
from .contrato import Tarifable
from .elemento import Equipo


class Renta:
    """Transacción del dominio: renta de uno o más equipos."""

    PREFIJO: ClassVar[str] = "REN"
    ABIERTA: ClassVar[str] = "ABIERTA"
    EN_CURSO: ClassVar[str] = "EN_CURSO"
    CERRADA: ClassVar[str] = "CERRADA"
    CANCELADA: ClassVar[str] = "CANCELADA"
    # TODO E07: traducir el diagrama de estados (§6) a una tabla de transiciones
    TRANSICIONES: ClassVar[dict[str, tuple[str, ...]]]

    class Linea:
        """Parte de la composición: sólo existe dentro de su transacción."""

        def __init__(self, contenedora: "Renta", equipo: Equipo, dias: int) -> None:
            # TODO E07: implementar `Renta.Linea.__init__`
            raise NotImplementedError

        @property
        def contenedora(self) -> "Renta":
            """Referencia explícita al todo."""
            # TODO E07: implementar `Renta.Linea.contenedora`
            raise NotImplementedError

        @property
        def equipo(self) -> Equipo:
            # TODO E07: implementar `Renta.Linea.equipo`
            raise NotImplementedError

        @property
        def dias(self) -> int:
            # TODO E07: implementar `Renta.Linea.dias`
            raise NotImplementedError

        def importe(self) -> float:
            """Importe de la línea = cotización polimórfica del equipo."""
            # TODO E08: implementar `Renta.Linea.importe`
            raise NotImplementedError

    def __init__(
        self,
        productora: Productora,
        fecha: date,
        clave: str | None = None,
        estado: str = "ABIERTA",
        alertada: bool = False,
    ) -> None:
        # TODO E07: implementar `Renta.__init__`
        raise NotImplementedError

    @property
    def clave(self) -> str:
        # TODO E07: implementar `Renta.clave`
        raise NotImplementedError

    @property
    def productora(self) -> Productora:
        # TODO E07: implementar `Renta.productora`
        raise NotImplementedError

    @property
    def fecha(self) -> date:
        # TODO E07: implementar `Renta.fecha`
        raise NotImplementedError

    @property
    def estado(self) -> str:
        # TODO E07: implementar `Renta.estado`
        raise NotImplementedError

    @property
    def lineas(self) -> tuple["Renta.Linea", ...]:
        """Vista inmutable de las líneas."""
        # TODO E07: implementar `Renta.lineas`
        raise NotImplementedError

    def agregar(self, equipo: Equipo, dias: int) -> "Renta.Linea":
        """Crea y posee una línea; sólo en estado ABIERTA. Sección crítica."""
        # TODO E07: implementar `Renta.agregar`
        raise NotImplementedError

    def _restaurar_linea(self, equipo: Equipo, dias: int) -> None:
        """Uso exclusivo de persistencia: agrega sin validar el estado."""
        # TODO E07: implementar `Renta._restaurar_linea`
        raise NotImplementedError

    def cambiar_estado(self, nuevo: str) -> None:
        """Aplica una transición válida de TRANSICIONES.

        Raises:
            ValueError: transición no permitida o EN_CURSO sin líneas.
        """
        # TODO E07: implementar `Renta.cambiar_estado`
        raise NotImplementedError

    def antiguedad(self, hoy: date) -> int:
        """Días transcurridos desde la apertura."""
        # TODO E07: implementar `Renta.antiguedad`
        raise NotImplementedError

    def subtotal(self) -> float:
        """Suma de importes de las líneas."""
        # TODO E08: implementar `Renta.subtotal`
        raise NotImplementedError

    def descuento(self) -> float:
        """Monto de descuento según el nivel del productora."""
        # TODO E08: implementar `Renta.descuento`
        raise NotImplementedError

    def total(self) -> float:
        """Total = subtotal - descuento."""
        # TODO E08: implementar `Renta.total`
        raise NotImplementedError

    def __getstate__(self) -> dict[str, object]:
        """Excluye el candado (no serializable), equivalente a ``transient``."""
        # TODO E14: implementar `Renta.__getstate__`
        raise NotImplementedError

    def __setstate__(self, estado: dict[str, object]) -> None:
        """Restaura atributos y crea un candado nuevo."""
        # TODO E14: implementar `Renta.__setstate__`
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO E07: implementar `Renta.__str__`
        raise NotImplementedError
