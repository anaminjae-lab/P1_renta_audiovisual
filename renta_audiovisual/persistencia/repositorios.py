"""E13. Repositorios SQLite con SQL explícito y mapeo de filas.

Referencias: jerarquia06.py (contrato abstracto), elemento.py
(reconstrucción polimórfica con ``Equipo.crear``).
"""

import sqlite3
from abc import ABC, abstractmethod
from datetime import date

from ..modelo.actor import Nivel, Productora
from ..modelo.elemento import Equipo
from ..modelo.transaccion import Renta
from .conexion import transaccion


class Repositorio[T](ABC):
    """Contrato genérico de repositorio (la anotación ``[T]`` es sólo de tipos)."""

    def __init__(self, con: sqlite3.Connection) -> None:
        self._con = con

    @abstractmethod
    def guardar(self, objeto: T) -> None:
        """Inserta o actualiza (upsert)."""

    @abstractmethod
    def obtener(self, clave: str) -> T | None:
        """Busca por clave."""

    @abstractmethod
    def todos(self) -> list[T]:
        """Recupera todos."""

    @abstractmethod
    def _mapear(self, fila: sqlite3.Row) -> T:
        """Convierte una fila en objeto."""


class RepositorioEquipo(Repositorio[Equipo]):
    """Persistencia de equipos (los tres subtipos en una tabla)."""

    _UPSERT = (
        "INSERT INTO equipos (clave, tipo, nombre, precio_base, atributo) "
        "VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(clave) DO UPDATE SET nombre = excluded.nombre, "
        "precio_base = excluded.precio_base, atributo = excluded.atributo"
    )

    @staticmethod
    def _parametros(e: Equipo) -> tuple[str, str, str, float, int]:
        return (e.clave, e.tipo, e.nombre, e.precio_base, e.valor_atributo())

    def guardar(self, objeto: Equipo) -> None:
        # TODO E13: implementar `RepositorioEquipo.guardar`
        raise NotImplementedError

    def guardar_varios(self, objetos: list[Equipo]) -> None:
        """Inserción masiva con ``executemany``."""
        # TODO E13: implementar `RepositorioEquipo.guardar_varios`
        raise NotImplementedError

    def obtener(self, clave: str) -> Equipo | None:
        # TODO E13: implementar `RepositorioEquipo.obtener`
        raise NotImplementedError

    def todos(self) -> list[Equipo]:
        # TODO E13: implementar `RepositorioEquipo.todos`
        raise NotImplementedError

    def _mapear(self, fila: sqlite3.Row) -> Equipo:
        """Reconstrucción polimórfica por la columna ``tipo``."""
        # TODO E13: implementar `RepositorioEquipo._mapear`
        raise NotImplementedError


class RepositorioProductora(Repositorio[Productora]):
    """Persistencia de productoras."""

    def guardar(self, objeto: Productora) -> None:
        # TODO E13: implementar `RepositorioProductora.guardar`
        raise NotImplementedError

    def obtener(self, clave: str) -> Productora | None:
        # TODO E13: implementar `RepositorioProductora.obtener`
        raise NotImplementedError

    def todos(self) -> list[Productora]:
        # TODO E13: implementar `RepositorioProductora.todos`
        raise NotImplementedError

    def _mapear(self, fila: sqlite3.Row) -> Productora:
        # TODO E13: implementar `RepositorioProductora._mapear`
        raise NotImplementedError


class RepositorioRenta(Repositorio[Renta]):
    """Persistencia de rentas y sus líneas (composición)."""

    def __init__(
        self,
        con: sqlite3.Connection,
        repo_equipos: RepositorioEquipo,
        repo_productoras: RepositorioProductora,
    ) -> None:
        super().__init__(con)
        self._repo_equipos = repo_equipos
        self._repo_productoras = repo_productoras

    def guardar(self, objeto: Renta) -> None:
        """Upsert de la transacción y reemplazo de sus líneas en UNA transacción."""
        # TODO E13: implementar `RepositorioRenta.guardar`
        raise NotImplementedError

    def obtener(self, clave: str) -> Renta | None:
        # TODO E13: implementar `RepositorioRenta.obtener`
        raise NotImplementedError

    def todos(self) -> list[Renta]:
        # TODO E13: implementar `RepositorioRenta.todos`
        raise NotImplementedError

    def _mapear(self, fila: sqlite3.Row) -> Renta:
        """Reconstruye la transacción, su productora y sus líneas."""
        # TODO E13: implementar `RepositorioRenta._mapear`
        raise NotImplementedError
