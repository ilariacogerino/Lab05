from database.corso_DAO import corsoDAO
from database.studente_DAO import studenteDAO

#CLASSE PER IL TRASFERIMENTO DEI DATI DAI DAO AL CONTROLLER

class Model:
    def __init__(self):
        self.daoC = corsoDAO()
        self.daoS = studenteDAO()

    def getCorsi(self):
        corsi = self.daoC.getAllCorsi
        return corsi

    def getStudenti(self):
        studenti = self.daoS.getAllStudenti
        return studenti

    def getIscritti(self, corso):
        iscritti = self.daoS.getIscrizioni(corso)
        return iscritti

    def cercaStudente(self, matricola):
        studente = self.daoS.cercaStudente(matricola)
        return studente

    def cercaCorsi(self, matricola):
        corsi = self.daoC.cercaCorsi(matricola)
        return corsi

