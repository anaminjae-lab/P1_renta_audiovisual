"""E03. Identidad de los objetos: claves ``PPP-0000``.

Referencias: construccion03.py (contador como atributo de clase),
construccion09.py (@classmethod / @staticmethod), thread07.py (sincronización).
"""

import threading
from typing import ClassVar


class Clave:
    """Generador y validador de claves con prefijo de 3 letras y 4 dígitos."""

    _contadores: ClassVar[dict[str, int]] = {}
    _candado: ClassVar[threading.Lock] = threading.Lock()

    @staticmethod
    def es_valida(texto: str) -> bool:
        """``True`` si ``texto`` tiene la forma ``ABC-0001``."""
        # TODO E03: implementar `Clave.es_valida`
        raise NotImplementedError

    @classmethod
    def siguiente(cls, prefijo: str) -> str:
        """Devuelve la siguiente clave del prefijo; segura entre hilos.

        Raises:
            ValueError: si el prefijo no son 3 letras mayúsculas.
        """
        # TODO E03: implementar `Clave.siguiente`
        raise NotImplementedError

    @classmethod
    def registrar(cls, clave: str) -> None:
        """Informa una clave existente (p. ej. leída de SQLite) para no repetirla."""
        # TODO E03: implementar `Clave.registrar`
        raise NotImplementedError

    @classmethod
    def reiniciar(cls) -> None:
        """Reinicia todos los contadores (uso en pruebas)."""
        with cls._candado:
            cls._contadores.clear()
