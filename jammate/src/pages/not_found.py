import flet as ft
from paths import Paths

def not_found_view(route: str):
    return ft.View(
        Paths.NOT_FOUND,
        [
            ft.Text("404 Not Found"),
        ]
    )
