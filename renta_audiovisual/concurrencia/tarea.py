"""E12. Tarea periódica con detención cooperativa.

Referencias: thread07.py (subclase de ``threading.Thread`` con ``run``),
thread04.py (``threading.Event``), thread01.py (``join``).
"""

import threading
from abc import ABC, abstractmethod


class TareaPeriodica(threading.Thread, ABC):
    """Hilo que ejecuta ``ejecutar()`` cada ``periodo`` segundos hasta ``detener()``."""

    def __init__(self, periodo: float, nombre: str = "tarea") -> None:
        # TODO E12: implementar `TareaPeriodica.__init__`
        raise NotImplementedError

    def run(self) -> None:
        """Ciclo: mientras el evento no esté activo, ejecutar y esperar."""
        # TODO E12: implementar `TareaPeriodica.run`
        raise NotImplementedError

    def detener(self, espera: float = 2.0) -> None:
        """Detención cooperativa: activa el evento y espera con ``join``."""
        # TODO E12: implementar `TareaPeriodica.detener`
        raise NotImplementedError

    @abstractmethod
    def ejecutar(self) -> None:
        """Trabajo de cada ciclo."""
