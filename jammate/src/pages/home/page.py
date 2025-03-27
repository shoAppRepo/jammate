import flet as ft
from paths import Paths

def home_view(page: ft.Page):
    return ft.View(
        Paths.HOME,
        [
            ft.Text("Home Page"),
            ft.ElevatedButton("Go to Bands", on_click=lambda _: page.go(Paths.BANDS))
        ]
    )
