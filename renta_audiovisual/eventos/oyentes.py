"""E15. Oyentes de eventos (Observer) para desacoplar servicio y UI.

Referencias: jerarquia07.py (interfaz común vía ABC). ``queue.Queue`` es la
única biblioteca adicional (estándar) para pasar eventos entre hilos.
"""

import queue
from abc import ABC, abstractmethod


class Oyente(ABC):
    """Interfaz de quien desea ser notificado."""

    @abstractmethod
    def notificar(self, evento: str, detalle: str) -> None:
        """Recibe un evento (``ALTA``, ``ESTADO``, ``CANCELACION``, ``ALERTA``...)."""


class OyenteMemoria(Oyente):
    """Guarda los eventos en una lista (pruebas y bitácora)."""

    def __init__(self) -> None:
        self.eventos: list[tuple[str, str]] = []

    def notificar(self, evento: str, detalle: str) -> None:
        # TODO E15: implementar `OyenteMemoria.notificar`
        raise NotImplementedError


class OyenteCola(Oyente):
    """Deposita eventos en una cola segura; el hilo de la UI la vacía."""

    def __init__(self) -> None:
        self.cola: queue.Queue[tuple[str, str]] = queue.Queue()

    def notificar(self, evento: str, detalle: str) -> None:
        # TODO E15: implementar `OyenteCola.notificar`
        raise NotImplementedError

    def pendientes(self) -> list[tuple[str, str]]:
        """Extrae sin bloquear todos los eventos pendientes."""
        # TODO E15: implementar `OyenteCola.pendientes`
        raise NotImplementedError
