import flet as ft

#IMPORTO SOLO LA CLASSE MODELLO PERCHE' PRENDO DA LI' LE INFORMAZIONI, NON DAI DAO
from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCercaIscritti(self, e):
        corso = self._view._ddCorsi.value
        if corso is None or corso == "":
            self._view.create_alert("Selezionare un corso!")
            return

        self._view._testo.controls.clear()
        self._view._page.update()

        iscritti = self._model.getIscritti(corso)
        self._view._testo.controls.append(ft.Text(f"Ci sono {len(iscritti)} al corso: \n"))

        for iscritto in iscritti:
            self._view._testo.controls.append(ft.Text(f"{iscritto}"))

        self._view._testo.controls.append(ft.Text(f"--------------"))

        self._view._page.update()


    def handleCercaStudente(self, e):
        matricola = self._view._matricola.value

        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare un matricola!")
            return

        studente = self._model.cercaStudente(matricola)

        if studente is None:
            self._view.create_alert("Studente non presente!")
            return

        self._view._testo.controls.clear()
        self._view._nome.value = studente.nome
        self._view._cognome.value = studente.cognome

        self._view._page.update()


    def handleCercaCorsi(self, e):
        matricola = self._view._matricola.value

        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare un matricola!")
            return

        self._view._testo.controls.clear()

        corsi = self._model.cercaCorsi(matricola)

        self._view._testo.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
        for corso in corsi:
            self._view._testo.controls.append(ft.Text(f"{corso}"))

        self._view._page.update()


