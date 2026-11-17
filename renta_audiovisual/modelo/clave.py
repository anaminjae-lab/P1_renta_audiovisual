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
        return (
            len(texto) == 8
            and all("A" <= letra <= "Z" for letra in texto[:3])
            and texto[3] ==  "-"
            and all("0" <= digito <= "9" for digito in texto[4:])
        )
        #raise NotImplementedError

    @classmethod
    def siguiente(cls, prefijo: str) -> str:
        """Devuelve la siguiente clave del prefijo; segura entre hilos.

        Raises:
            ValueError: si el prefijo no son 3 letras mayúsculas.
        """
        if len(prefijo) != 3 or not all(
            "A" <= letra <= "Z" for letra in prefijo
        ):
            raise ValueError("El prefijo debe contener 3 letras mayusculas")

        with cls._candado:
            numero = cls._contadores.get(prefijo,0) + 1
            cls._contadores[prefijo] = numero

        return f"{prefijo}-{numero:04d}"
        # TODO E03: implementar `Clave.siguiente`
        #raise NotImplementedError

    @classmethod
    def registrar(cls, clave: str) -> None:
        """Informa una clave existente (p. ej. leída de SQLite) para no repetirla."""
        if not cls.es_valida(clave):
            raise ValueError("Clave no valida")

        prefijo = clave[:3]
        numero = int(clave[4:])

        with cls._candado:
            actual = cls._contadores.get(prefijo,0)
            cls._contadores[prefijo] = max(actual, numero)
        # TODO E03: implementar `Clave.registrar`
        #raise NotImplementedError

    @classmethod
    def reiniciar(cls) -> None:
        """Reinicia todos los contadores (uso en pruebas)."""
        with cls._candado:
            cls._contadores.clear()
