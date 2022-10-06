from dataclasses import dataclass
from tipologie import Catalogo
import re


class Ordine:
    def __init__(self, testo) -> None:
        self.testo = testo
        self.serramenti = []
        self.codice_cliente: int = 4417
        self.riferimento_commessa: str = None
        self.note: str = None
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

        self.riferimento_commessa = re.search("^Riferimento (?P<riferimento>.*)", self.testo, re.MULTILINE).group('riferimento')

    def esporta(self):
        '''crea il file TXT per import in F3000'''
        # file_out = open(r's:\F3000_2013\IMPEXP_ORDINI\FINNOVA.txt','w')
        file_out = open(r'result.txt','w')
        numero_ordine = 12212 #input("Numero ordine ? ")
        file_out.write(';\n'.join('%s' % i for i in (1, self.codice_cliente, self.riferimento_commessa, numero_ordine ,self.note,'')))
               
        for pos, serramento in enumerate(self.serramenti): 
            file_out.write(serramento.getF3000(pos+1))
            
        file_out.write('P,0,0;') #fine file
        file_out.close()
            

@dataclass
class Serramento:
    testo: str
    riferimento: str
    pezzi: int
    base: int
    altezza: int
    tabella_tecnica: int = 92 #uniplanar
    colore: int = 61 #saldato RAL
    extras: str = ''

    def setTesto(self, testo):
        self.testo = testo

    def getTipologia(self):
        for key, t in Catalogo.lista.items():
            if key in self.testo:
                return t

    def getF3000(self, pos):
        return f"P,{pos},{self.riferimento},{self.base},{self.altezza},{self.pezzi},{self.tabella_tecnica},{self.getTipologia()},{self.colore};\n{self.extras}"

    def __str__(self) -> str:
        return f"Rif.{self.riferimento} {self.base}x{self.altezza} Pz.{self.pezzi} Type {self.getTipologia()}"

