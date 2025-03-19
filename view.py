import flet as ft

import controller as c
from controller import SpellChecker


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        self.dd = ft.Dropdown(label="Select language",
                         hint_text="Select language",
                         options=[ft.dropdown.Option("italian"), ft.dropdown.Option("english"), ft.dropdown.Option("spanish")],
                         on_change=self.controlloSelezione)

        self.dd2 = ft.Dropdown(label="Search Modality",
                          hint_text="Search Modality",
                          options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"), ft.dropdown.Option("Dichotomic")],
                          on_change = self.controlloSelezione)

        self.txtIn = ft.TextField(label="Add your sentence here")

        self.btn = ft.ElevatedButton(text = "Spell Check", on_click=self.handleSpellCheck)

        self.__lv = ft.ListView()


        row2 = ft.Row(controls=[self.dd])
        row3 = ft.Row(controls = [self.dd2, self.txtIn, self.btn])

        self.txt = ft.Text("", visible=False)

        self.page.add(row2, row3, self.__lv, self.txt)

        self.page.update()

    def handleSpellCheck(self, e):
        risultato = self.__controller.handleSentence(str(self.txtIn.value), self.dd.value, self.dd2.value)
        if self.txtIn.value == "" or self.dd.value is None or self.dd2.value is None:
            self.__lv.controls.append(ft.Text(f'Errore nella compilazione dei campi'))
        else:
            self.__lv.controls.append(ft.Text(f'Frase Inserita: {self.txtIn.value}'))
            self.__lv.controls.append(ft.Text(f'Parole errate: {risultato[0]}'))
            self.__lv.controls.append(ft.Text(f'Tempo richiesto dalla ricerca: {risultato[1]}'))

        self.txtIn.value = ""

        self.page.update()

    def controlloSelezione(self, e):
        if self.dd.value:
            self.txt.value = f'Selezione corretta della lingua'
            self.txt.color = "green"
        self.txt.visible = True

        if self.dd2.value:
            self.txt.value = f'Selezione corretta della modalità'
            self.txt.color = "green"
        self.txt.visible = True

        self.page.update()


    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
