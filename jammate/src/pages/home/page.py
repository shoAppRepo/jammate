import flet as ft

def home_view(page: ft.Page):
    return ft.View(
        "/",
        [
            ft.Text("Home Page"),
            ft.ElevatedButton("Go to Bands", on_click=lambda _: page.go("/bands"))
        ]
    )
