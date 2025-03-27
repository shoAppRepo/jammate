import flet as ft
from pages.home.page import home_view
from pages.bands.page import bands_view
from pages.not_found import not_found_view

def route_change(page: ft.Page, e: ft.RouteChangeEvent):
    page.views.clear()

    if e.route == "/":
        page.views.append(home_view(page))
    elif e.route == "/bands":
        page.views.append(bands_view(page))
    else:
        page.views.append(not_found_view(e.route))

    page.update()
