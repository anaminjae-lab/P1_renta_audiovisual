"""E09–E10. Catálogo (agregación) y tipos anidados/locales.

Referencias: construccion05.py (``*args`` y ``**kwargs``), demo.py (el todo
referencia partes que existen por sí mismas), jerarquia13.py (clase anidada),
p10_match.py (``match``).
"""

from .elemento import Equipo


class Inventario:
    """Agregación de equipos: los contiene, pero no los crea ni los destruye."""

    def __init__(self, *equipos: Equipo) -> None:
        # TODO E09: implementar `Inventario.__init__`
        raise NotImplementedError

    def agregar(self, *equipos: Equipo) -> int:
        """Agrega uno o varios; rechaza claves repetidas. Devuelve cuántos agregó."""
        # TODO E09: implementar `Inventario.agregar`
        raise NotImplementedError

    def obtener(self, clave: str) -> Equipo:
        """Raises: KeyError si no existe."""
        # TODO E09: implementar `Inventario.obtener`
        raise NotImplementedError

    def quitar(self, clave: str) -> Equipo:
        # TODO E09: implementar `Inventario.quitar`
        raise NotImplementedError

    def todos(self) -> tuple[Equipo, ...]:
        """Vista inmutable en orden de inserción."""
        # TODO E09: implementar `Inventario.todos`
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO E09: implementar `Inventario.__len__`
        raise NotImplementedError

    def buscar(self, **criterios: object) -> list[Equipo]:
        """Filtra por ``tipo=``, ``texto=`` (en el nombre) y ``precio_max=``.

        Raises:
            ValueError: criterio desconocido.
        """
        # TODO E09: implementar `Inventario.buscar`
        raise NotImplementedError

    def ordenados(self, por: str = "nombre", descendente: bool = False) -> list[Equipo]:
        """Ordena por ``"nombre"``, ``"precio"`` o ``"clave"`` usando ``key=lambda``."""
        # TODO E09: implementar `Inventario.ordenados`
        raise NotImplementedError

    def resumen_por_tipo(self) -> dict[str, int]:
        """Cuenta equipos por tipo usando una CLASE LOCAL como acumulador."""

        class Acumulador:
            """Clase local: sólo existe dentro de este método."""

            def __init__(self) -> None:
                self.cuentas: dict[str, int] = {}

            def sumar(self, tipo: str) -> None:
                self.cuentas[tipo] = self.cuentas.get(tipo, 0) + 1

        # TODO E10: implementar `Inventario.resumen_por_tipo`
        raise NotImplementedError
