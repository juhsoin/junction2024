from enum import IntEnum, Enum


class Category(Enum):
    KAYTTOPAIKKAPROSESSI = "Käyttöpaikkaprosessi"
    TUOTEPROSESSI = "Tuoteprosessi"
    MITTAUSTIETOPROSESSI = "Mittaustietoprosessi"
    ASIAKASTIETOPROSESSI = "Asiakastietoprosessi"
    SOPIMUSPROSESSI = "Sopimusprosessi"
    SANOMAHALLINTA = "Sanomahallinta"
    YLEINEN_HALLINTA = "Yleinen hallinta"
    TIETOSUOJA = "Tietosuoja"
    KYTKENTA_KATKAISUPROSESSI = "Kytkentä/katkaisuprosessi"
    LASKUTUSTIEDOT = "Laskutustiedot"
    VALTUUTUSPROSESSI = "Valtuutusprosessi"
    TIETOTURVA = "Tietoturva"
    ROOLITUS = "Roolitus"
    MITTAUSTIEDONHALLINTA = "Mittaustiedonhallinta"
    RAPORTOINTI = "Raportointi"
    TOIMEKSIANTOPROSESSI = "Toimeksiantoprosessi"
    LOPPUASIAKASKAYTTOLIITTYMA = "Loppuasiakaskäyttöliittymä"
    LASKENNAT = "Laskennat"
    OSAPUOLITIEDOT = "Osapuolitiedot"
    KUORMANOHJAUSPROSESSI = "Kuormanohjausprosessi"


class States(IntEnum):
    NEW = 1
    CLARIFICATION = 2
    RECOMMENDATION = 3
    WIP = 4
    READY = 5
    REJECTED = 6
