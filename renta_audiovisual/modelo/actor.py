"""E06. Actor del dominio y jerarquía de niveles.

Referencias: construccion08.py (Singleton con ``__new__``), jerarquia07.py
(polimorfismo sobre una ABC), construccion09.py (constructor alternativo con
@classmethod), persona04.py (privado + propiedad de solo lectura).
"""

from abc import ABC, abstractmethod
from typing import ClassVar

from .clave import Clave


class Nivel(ABC):
    """Nivel del productora; cada subclase es un Singleton con su descuento."""

    NOMBRE: ClassVar[str] = ""
    _instancia: ClassVar["Nivel | None"] = None

    def __new__(cls) -> "Nivel":
        """Devuelve siempre la misma instancia por subclase (construccion08.py)."""
        # TODO E06: implementar `Nivel.__new__`
        raise NotImplementedError

    @abstractmethod
    def descuento(self) -> float:
        """Fracción de descuento (0.0 a 1.0)."""

    @staticmethod
    def desde_nombre(nombre: str) -> "Nivel":
        """Fábrica: ``"BASICO"``, ``"PLATA"`` u ``"ORO"`` → instancia única."""
        # TODO E06: implementar `Nivel.desde_nombre`
        raise NotImplementedError

    def __str__(self) -> str:
        return self.NOMBRE


class Basico(Nivel):
    """Sin descuento."""

    NOMBRE = "BASICO"
    _instancia = None

    def descuento(self) -> float:
        # TODO E06: implementar `Basico.descuento`
        raise NotImplementedError


class Plata(Nivel):
    """Nivel intermedio."""

    NOMBRE = "PLATA"
    _instancia = None

    def descuento(self) -> float:
        # TODO E06: implementar `Plata.descuento`
        raise NotImplementedError


class Oro(Nivel):
    """Nivel superior."""

    NOMBRE = "ORO"
    _instancia = None

    def descuento(self) -> float:
        # TODO E06: implementar `Oro.descuento`
        raise NotImplementedError


class Productora:
    """Actor del dominio: cliente que renta equipo."""

    PREFIJO: ClassVar[str] = "PRD"

    def __init__(
        self, nombre: str, correo: str, nivel: Nivel | None = None, clave: str | None = None
    ) -> None:
        """Nivel por omisión: ``Basico()``."""
        # TODO E06: implementar `Productora.__init__`
        raise NotImplementedError

    @classmethod
    def desde_texto(cls, texto: str) -> "Productora":
        """Constructor alternativo: ``"Nombre;correo;NIVEL"``."""
        # TODO E06: implementar `Productora.desde_texto`
        raise NotImplementedError

    @property
    def clave(self) -> str:
        # TODO E06: implementar `Productora.clave`
        raise NotImplementedError

    @property
    def nombre(self) -> str:
        # TODO E06: implementar `Productora.nombre`
        raise NotImplementedError

    @nombre.setter
    def nombre(self, valor: str) -> None:
        # TODO E06: implementar `Productora.nombre`
        raise NotImplementedError

    @property
    def correo(self) -> str:
        # TODO E06: implementar `Productora.correo`
        raise NotImplementedError

    @correo.setter
    def correo(self, valor: str) -> None:
        # TODO E06: implementar `Productora.correo`
        raise NotImplementedError

    @property
    def nivel(self) -> Nivel:
        # TODO E06: implementar `Productora.nivel`
        raise NotImplementedError

    @nivel.setter
    def nivel(self, valor: Nivel) -> None:
        # TODO E06: implementar `Productora.nivel`
        raise NotImplementedError

    def descuento(self) -> float:
        """Delegación en el nivel (polimorfismo)."""
        # TODO E06: implementar `Productora.descuento`
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.clave} {self.nombre} [{self.nivel}]"
