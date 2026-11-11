"""E04–E05. Clase base abstracta, capacidades (mixins) y subtipos.

Referencias: jerarquia05.py (especialización), jerarquia06.py (ABC),
jerarquia11.py y jerarquia12.py (herencia múltiple y colisión de métodos),
encapsulacion03.py (propiedad calculada), persona03.py (name mangling),
p10_match.py (``match``).
"""

from abc import abstractmethod
from typing import ClassVar

from .clave import Clave
from .contrato import Tarifable


class Equipo(Tarifable):
    """Abstracción central: equipo rentable por día."""

    PREFIJO: ClassVar[str] = ""

    def __init__(self, nombre: str, precio_base: float, clave: str | None = None) -> None:
        """Inicializa nombre, precio base y clave (se genera si es ``None``)."""
        # TODO E04: implementar `Equipo.__init__`
        raise NotImplementedError

    @property
    def clave(self) -> str:
        """Identidad inmutable (solo lectura)."""
        # TODO E04: implementar `Equipo.clave`
        raise NotImplementedError

    @property
    def nombre(self) -> str:
        """Nombre descriptivo, no vacío."""
        # TODO E04: implementar `Equipo.nombre`
        raise NotImplementedError

    @nombre.setter
    def nombre(self, valor: str) -> None:
        # TODO E04: implementar `Equipo.nombre`
        raise NotImplementedError

    @property
    def precio_base(self) -> float:
        """Precio base por día, estrictamente positivo."""
        # TODO E04: implementar `Equipo.precio_base`
        raise NotImplementedError

    @precio_base.setter
    def precio_base(self, valor: float) -> None:
        # TODO E04: implementar `Equipo.precio_base`
        raise NotImplementedError

    @property
    def tipo(self) -> str:
        """Prefijo del subtipo (propiedad calculada)."""
        return self.PREFIJO

    def recargo(self) -> float:
        """Recargo por capacidades; la base no tiene ninguno."""
        return 0.0

    @abstractmethod
    def factor(self) -> float:
        """Factor multiplicativo propio del subtipo."""

    @abstractmethod
    def valor_atributo(self) -> int:
        """Valor del atributo distintivo del subtipo (para persistencia)."""

    def _calcular(self, dias: int) -> float:
        """Tarifa del subtipo por ``dias`` (fórmula: §6 del DOCX, por deducir)."""
        # TODO E04: implementar `Equipo._calcular`
        raise NotImplementedError

    def copiar(self) -> "Equipo":
        """Crea un objeto equivalente con clave NUEVA (identidad distinta)."""
        # TODO E05: implementar `Equipo.copiar`
        raise NotImplementedError

    @staticmethod
    def crear(
        prefijo: str, nombre: str, precio_base: float, valor: int, clave: str | None = None
    ) -> "Equipo":
        """Fábrica polimórfica: reconstruye el subtipo correcto según el prefijo.

        Raises:
            ValueError: si el prefijo no corresponde a ningún subtipo.
        """
        # TODO E05: implementar `Equipo.crear`
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.clave} {self.nombre} (${self.precio_base:.2f}/día)"


class Capacidad:
    """Raíz de las capacidades: termina la cadena cooperativa de ``super()``."""

    def recargo(self) -> float:
        """Recargo neutro."""
        return 0.0

    def etiquetas(self) -> list[str]:
        """Etiquetas acumuladas por la cadena de ``super()``."""
        return []


class Asegurable(Capacidad):
    """Capacidad: incluye póliza contra daño."""

    RECARGO: ClassVar[float]  # TODO E05: valor por deducir de los ejemplos (§6)

    def recargo(self) -> float:
        # TODO E05: implementar `Asegurable.recargo`
        raise NotImplementedError

    def etiquetas(self) -> list[str]:
        # TODO E05: implementar `Asegurable.etiquetas`
        raise NotImplementedError


class Transportable(Capacidad):
    """Capacidad: incluye estuche y traslado."""

    RECARGO: ClassVar[float]  # TODO E05: valor por deducir de los ejemplos (§6)

    def recargo(self) -> float:
        # TODO E05: implementar `Transportable.recargo`
        raise NotImplementedError

    def etiquetas(self) -> list[str]:
        # TODO E05: implementar `Transportable.etiquetas`
        raise NotImplementedError


class Camara(Equipo):
    """Cámara de cine o fotografía. Atributo ``resolucion_mp`` (megapíxeles) entre 8 y 100."""

    # TODO E05: declarar las capacidades que hereda y su orden (§6 y prueba 05)

    PREFIJO: ClassVar[str] = "CAM"
    MINIMO: ClassVar[int] = 8
    MAXIMO: ClassVar[int] = 100
    ESCALA: ClassVar[int]  # TODO E05: valor por deducir de los ejemplos (§6)

    def __init__(self, nombre: str, precio_base: float, resolucion_mp: int, clave: str | None = None) -> None:
        # TODO E05: implementar `Camara.__init__`
        raise NotImplementedError

    @property
    def resolucion_mp(self) -> int:
        """megapíxeles."""
        # TODO E05: implementar `Camara.resolucion_mp`
        raise NotImplementedError

    @resolucion_mp.setter
    def resolucion_mp(self, valor: int) -> None:
        # TODO E05: implementar `Camara.resolucion_mp`
        raise NotImplementedError

    def factor(self) -> float:
        """Factor propio del subtipo; depende de ``resolucion_mp`` y de ``ESCALA``."""
        # TODO E05: implementar `Camara.factor`
        raise NotImplementedError

    def valor_atributo(self) -> int:
        # TODO E05: implementar `Camara.valor_atributo`
        raise NotImplementedError


class Iluminacion(Equipo):
    """Luminaria de estudio. Atributo ``potencia_w`` (watts) entre 50 y 2000."""

    # TODO E05: declarar las capacidades que hereda y su orden (§6 y prueba 05)

    PREFIJO: ClassVar[str] = "ILU"
    MINIMO: ClassVar[int] = 50
    MAXIMO: ClassVar[int] = 2000
    ESCALA: ClassVar[int]  # TODO E05: valor por deducir de los ejemplos (§6)

    def __init__(self, nombre: str, precio_base: float, potencia_w: int, clave: str | None = None) -> None:
        # TODO E05: implementar `Iluminacion.__init__`
        raise NotImplementedError

    @property
    def potencia_w(self) -> int:
        """watts."""
        # TODO E05: implementar `Iluminacion.potencia_w`
        raise NotImplementedError

    @potencia_w.setter
    def potencia_w(self, valor: int) -> None:
        # TODO E05: implementar `Iluminacion.potencia_w`
        raise NotImplementedError

    def factor(self) -> float:
        """Factor propio del subtipo; depende de ``potencia_w`` y de ``ESCALA``."""
        # TODO E05: implementar `Iluminacion.factor`
        raise NotImplementedError

    def valor_atributo(self) -> int:
        # TODO E05: implementar `Iluminacion.valor_atributo`
        raise NotImplementedError


class Audio(Equipo):
    """Consola o kit de audio. Atributo ``canales`` (canales) entre 1 y 32."""

    # TODO E05: declarar las capacidades que hereda y su orden (§6 y prueba 05)

    PREFIJO: ClassVar[str] = "AUD"
    MINIMO: ClassVar[int] = 1
    MAXIMO: ClassVar[int] = 32
    ESCALA: ClassVar[int]  # TODO E05: valor por deducir de los ejemplos (§6)

    def __init__(self, nombre: str, precio_base: float, canales: int, clave: str | None = None) -> None:
        # TODO E05: implementar `Audio.__init__`
        raise NotImplementedError

    @property
    def canales(self) -> int:
        """canales."""
        # TODO E05: implementar `Audio.canales`
        raise NotImplementedError

    @canales.setter
    def canales(self, valor: int) -> None:
        # TODO E05: implementar `Audio.canales`
        raise NotImplementedError

    def factor(self) -> float:
        """Factor propio del subtipo; depende de ``canales`` y de ``ESCALA``."""
        # TODO E05: implementar `Audio.factor`
        raise NotImplementedError

    def valor_atributo(self) -> int:
        # TODO E05: implementar `Audio.valor_atributo`
        raise NotImplementedError

    def recargo(self) -> float:
        """Colisión: ambas capacidades definen recargo(); resuélvela de forma explícita (regla: §6)."""
        # TODO E05: implementar `Audio.recargo`
        raise NotImplementedError
