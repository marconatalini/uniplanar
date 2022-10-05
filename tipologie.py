from dataclasses import dataclass


@dataclass
class Tipologia:
    numero: int

    def __str__(self) -> str:
        return f"{self.numero}"

@dataclass
class Catalogo:
    lista = {
        'FINESTRA 1A': Tipologia(1100),
        'FINESTRA 2A': Tipologia(1200),
        'FINESTRA 3A': Tipologia(1300),
        'PORTAF.1A': Tipologia(3100),
        'PORTAF.2A': Tipologia(3200),
        'PORTAF.3A': Tipologia(3300),
    }