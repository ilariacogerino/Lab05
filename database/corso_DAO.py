from database.DB_connect import get_connection
from model.corso import Corso


class corsoDAO:

    def getAllCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "select * from corso c"
        cursor.execute(query)

        corsi = []
        for row in cursor:
            corsi.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

        cnx.close()
        return corsi

    def cercaCorsi(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "SELECT * FROM iscrizione WHERE matricola = %s"

        cursor.execute(query, (matricola,))
        corsi = []
        for row in cursor:
            corsi.append(row)

        corsii = []
        for corso in corsi:
            for c in self.getAllCorsi():
                if c.codins  == corso['codins']:
                    corsii.append(c)

        cnx.close()
        return corsii