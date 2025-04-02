from database.DB_connect import get_connection
from model.studente import Studente
from model.corso import Corso



class studenteDAO:

    def getAllStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "SELECT * FROM studente"
        cursor.execute(query)

        #CREO UNA LISTA DI STUDENTI
        studenti = []
        for row in cursor:
            studenti.append(Studente(row['matricola'], row['cognome'], row['nome'], row['CDS']))

        cnx.close()
        return studenti

    def getIscrizioni(self, codice):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""select * from iscrizione i where codins = %s""")
        cursor.execute(query, (codice,))

        #CREO UNA LISTA DEGLI ISCRITTI
        iscritti = []
        for row in cursor:
            iscritti.append(row)

        #CREO UNA LISTA DI STUDENTI
        studentiIscritti = []
        for iscritto in iscritti:
            for studente in self.getAllStudenti():
                if studente.matricola == iscritto['matricola']:
                    studentiIscritti.append(studente)

        cnx.close()
        return studentiIscritti

    def cercaStudente(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "SELECT * FROM studente WHERE matricola = %s"
        cursor.execute(query, (matricola,))

        row = cursor.fetchone()
        if row is None:
            return None

        studente = Studente(row['matricola'], row['cognome'], row['nome'], row['CDS'])

        cnx.close()
        return studente





