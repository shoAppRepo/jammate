import flet as ft

def not_found_view(route: str):
    return ft.View(route, [ft.Text("404 Not Found")])
