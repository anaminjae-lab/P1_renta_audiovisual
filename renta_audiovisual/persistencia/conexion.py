"""E13. Conexión SQLite, esquema y transacciones como context manager.

Referencias: p21_contexto1.py y p22_contexto2.py (``@contextmanager``),
p23_contexto3.py (adquirir y liberar un recurso). Biblioteca: ``sqlite3``
(estándar). Investigación del estudiante: ``row_factory``, ``PRAGMA``,
``executemany`` e ``INSERT ... ON CONFLICT`` en la documentación de sqlite3.
"""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager

DDL = """
CREATE TABLE IF NOT EXISTS equipos (
    clave        TEXT PRIMARY KEY CHECK (length(clave) = 8),
    tipo         TEXT NOT NULL CHECK (tipo IN ('CAM', 'ILU', 'AUD')),
    nombre       TEXT NOT NULL CHECK (length(trim(nombre)) > 0),
    precio_base  REAL NOT NULL CHECK (precio_base > 0),
    atributo     INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS productoras (
    clave   TEXT PRIMARY KEY CHECK (length(clave) = 8),
    nombre  TEXT NOT NULL,
    correo  TEXT NOT NULL UNIQUE,
    nivel   TEXT NOT NULL CHECK (nivel IN ('BASICO', 'PLATA', 'ORO'))
);
CREATE TABLE IF NOT EXISTS rentas (
    clave     TEXT PRIMARY KEY CHECK (length(clave) = 8),
    productora   TEXT NOT NULL REFERENCES productoras(clave),
    fecha     TEXT NOT NULL,
    estado    TEXT NOT NULL
              CHECK (estado IN ('ABIERTA', 'EN_CURSO', 'CERRADA', 'CANCELADA')),
    alertada  INTEGER NOT NULL DEFAULT 0 CHECK (alertada IN (0, 1))
);
-- TODO E13: diseña la tabla lineas (composición): llave, llaves foráneas,
-- política de borrado y restricciones. Justifícala en el README (§7).
"""


def abrir(ruta: str) -> sqlite3.Connection:
    """Abre la base, activa llaves foráneas, configura ``row_factory`` y crea el esquema."""
    # TODO E13: implementar `abrir`
    raise NotImplementedError


@contextmanager
def transaccion(con: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    """Unidad de trabajo: ``commit`` al salir bien, ``rollback`` ante excepción."""
    # TODO E13: implementar `transaccion`
    raise NotImplementedError
