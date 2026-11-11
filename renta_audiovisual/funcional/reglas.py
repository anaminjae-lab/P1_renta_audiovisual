"""E11. Programación funcional: reglas invocables y combinables.

Referencias: construccion15.py (objetos invocables con ``__call__``),
jerarquia10b.py (funciones como valores), uso de ``lambda`` en los ejemplos.
"""

from collections.abc import Callable, Iterable

from ..modelo.elemento import Equipo

Predicado = Callable[[Equipo], bool]


class Regla:
    """Predicado con nombre; se usa como función: ``regla(equipo)``."""

    def __init__(self, predicado: Predicado, nombre: str = "regla") -> None:
        self._predicado = predicado
        self.nombre = nombre

    def __call__(self, equipo: Equipo) -> bool:
        """Evalúa la regla (construccion15.py)."""
        # TODO E11: implementar `Regla.__call__`
        raise NotImplementedError

    def y(self, otra: "Regla") -> "Regla":
        """Conjunción: nueva regla con lambda que captura self y otra."""
        # TODO E11: implementar `Regla.y`
        raise NotImplementedError

    def o(self, otra: "Regla") -> "Regla":
        """Disyunción."""
        # TODO E11: implementar `Regla.o`
        raise NotImplementedError

    def negar(self) -> "Regla":
        """Negación."""
        # TODO E11: implementar `Regla.negar`
        raise NotImplementedError

    def __str__(self) -> str:
        return self.nombre


def precio_maximo(limite: float) -> Regla:
    """Fábrica de reglas: la lambda captura ``limite``."""
    # TODO E11: implementar `precio_maximo`
    raise NotImplementedError


def de_tipo(prefijo: str) -> Regla:
    """Fábrica de reglas por prefijo de subtipo."""
    # TODO E11: implementar `de_tipo`
    raise NotImplementedError


def filtrar(equipos: Iterable[Equipo], regla: Callable[[Equipo], bool]) -> list[Equipo]:
    """Función de orden superior: recibe la regla como argumento."""
    # TODO E11: implementar `filtrar`
    raise NotImplementedError


def aplicar(equipos: Iterable[Equipo], funcion: Callable[[Equipo], float]) -> list[float]:
    """Función de orden superior: transforma cada equipo con ``funcion``."""
    # TODO E11: implementar `aplicar`
    raise NotImplementedError
