import flet as ft
from paths import Paths

def bands_view(page: ft.Page):
    return ft.View(
        Paths.BANDS,
        [
            ft.Text("Bands Page"),
        ]
    )
