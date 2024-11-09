from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel


class Cat(Enum):
    KAYTTOPAIKKAPROSESSI = 1
    TUOTEPROSESSI = 2
    MITTAUSTIETOPROSESSI = 3
    ASIAKASTIETOPROSESSI = 4
    SOPIMUSPROSESSI = 5
    SANOMAHALLINTA = 6
    YLEINEN_HALLINTA = 7
    TIETOSUOJA = 8
    KYTKENTA_KATKAISUPROSESSI = 9
    LASKUTUSTIEDOT = 10
    VALTUUTUSPROSESSI = 11
    TIETOTURVA = 12
    ROOLITUS = 13
    MITTAUSTIEDONHALLINTA = 14
    RAPORTOINTI = 15
    TOIMEKSIANTOPROSESSI = 16
    LOPPUASIAKASKAYTTOLIITTYMA = 17
    LASKENNAT = 18
    OSAPUOLITIEDOT = 19
    KUORMANOHJAUSPROSESSI = 20


class Category(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    value: str
    ticket_id: Optional[str]
    update_id: Optional[str]


class Stat(Enum):
    NEW = 1
    CLARIFICATION = 2
    RECOMMENDATION = 3
    WIP = 4
    READY = 5
    REJECTED = 6


class States(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    value: str
    ticket_id: Optional[str]
    update_id: Optional[str]
