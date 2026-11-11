"""E02. Contrato raíz del dominio Renta de equipo audiovisual.

Abstracción (Booch): define QUÉ se puede pedir a todo objeto cotizable,
sin decir CÓMO. Referencias: jerarquia06.py (ABC y @abstractmethod),
construccion09.py (@classmethod y @staticmethod), construccion01.py
(atributos de clase).
"""

from abc import ABC, abstractmethod
from typing import ClassVar


class Tarifable(ABC):
    """Contrato raíz: todo lo que puede cotizarse por un número de días."""

    MONEDA: ClassVar[str] = "MXN"
    IVA: ClassVar[float] = 0.16

    def cotizar(self, dias: int) -> float:
        """Método plantilla: valida ``dias`` y delega en ``_calcular``.

        Raises:
            ValueError: si ``dias`` es menor que 1.
        """
        # TODO E02: implementar `Tarifable.cotizar`
        raise NotImplementedError

    def cotizar_con_iva(self, dias: int) -> float:
        """Cotización con IVA, redondeada a dos decimales."""
        # TODO E02: implementar `Tarifable.cotizar_con_iva`
        raise NotImplementedError

    @abstractmethod
    def _calcular(self, dias: int) -> float:
        """Paso variable del método plantilla (lo define cada subtipo)."""

    @staticmethod
    def redondear(valor: float) -> float:
        """Redondea a dos decimales (no depende de la instancia)."""
        # TODO E02: implementar `Tarifable.redondear`
        raise NotImplementedError

    @classmethod
    def moneda(cls) -> str:
        """Devuelve la moneda declarada en la clase (construccion09bis.py)."""
        # TODO E02: implementar `Tarifable.moneda`
        raise NotImplementedError
