import flet as ft

from database.corso_DAO import corsoDAO


class View:
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        self.dao=corsoDAO()

        # graphical elements
        self._titolo = None
        self._ddCorsi = None
        self._btnCercaIscritti = None
        self._matricola = None
        self._nome = None
        self._cognome = None
        self._btnCercaStudente = None
        self._btnCercaCorsi = None
        self._btnIscrivi = None
        self._testo = None

    def load_interface(self):
        #self._page.bgcolor = "white"
        self._titolo = ft.Text("App Gestione Studenti", color = "blue", size = 24)

        self._ddCorsi = ft.Dropdown(label = "corso")
        self._fillddCorsi()

        self._btnCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                   on_click = self._controller.handleCercaIscritti)

        row1 = ft.Row(controls=[self._ddCorsi, self._btnCercaIscritti], alignment=ft.MainAxisAlignment.CENTER)

        self._matricola = ft.TextField(label = "matricola")
        self._nome = ft.TextField(label = "nome", read_only=True)
        self._cognome = ft.TextField(label = "cognome", read_only=True)

        row2 = ft.Row(controls=[self._matricola, self._nome, self._cognome], alignment=ft.MainAxisAlignment.CENTER)

        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente", on_click = self._controller.handleCercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click = self._controller.handleCercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi")

        row3 = ft.Row(controls=[self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi], alignment=ft.MainAxisAlignment.CENTER)

        self._testo = ft.ListView(expand = True, spacing=10, padding=20, auto_scroll=True)

        self._page.add(self._titolo, row1, row2, row3, self._testo)

        self._page.update()



    def _fillddCorsi(self):
        corsi = self.dao.getAllCorsi()
        for corso in corsi:
            self._ddCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))




    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
