import flet as ft
from router import route_change

def main(page: ft.Page):
    page.on_route_change = lambda e: route_change(page, e) 
    page.go("/")

ft.app(target=main)
