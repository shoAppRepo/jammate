import flet as ft
from router import route_change
from paths import Paths

def main(page: ft.Page):
    page.on_route_change = lambda e: route_change(page, e)
    page.go(Paths.HOME)

ft.app(target=main)
