from dataclasses import dataclass
from tipologie import Catalogo
import re


class Ordine:
    def __init__(self, testo) -> None:
        self.testo = testo
        self.serramenti = []
        self.parse()

    def parse(self):
        seek_idx = []
        for match in re.finditer("^\d+ .+ (?P<base>\d{3,4}) x (?P<altezza>\d{3,4}) NR (?P<pezzi>\d+) (?P<riferimento>\d+)", self.testo, re.MULTILINE):
            self.serramenti.append(Serramento("", match.group('riferimento'), match.group('pezzi'), match.group('base'), match.group('altezza')))
            seek_idx.append(match.start())

        seek_idx.append(len(self.testo))
        for i, value in enumerate(seek_idx[:-1]):
            ser = self.serramenti[i]
            ser.setTesto(self.testo[value:seek_idx[i+1]])
            

@dataclass
class Serramento:
    testo: str
    riferimento: str
    pezzi: int
    base: int
    altezza: int

    def setTesto(self, testo):
        self.testo = testo

    def getTipologia(self):
        for key, t in Catalogo.lista.items():
            if key in self.testo:
                return t

    def __str__(self) -> str:
        return f"Rif.{self.riferimento} {self.base}x{self.altezza} Pz.{self.pezzi} Type {self.getTipologia()}"

