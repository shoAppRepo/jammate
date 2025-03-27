import flet as ft

def main(page: ft.Page):
    # ルート変更時の処理
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()  # 既存のビューをクリア

        if e.route == "/":
            page.views.append(ft.View("/", [ft.Text("Home Page")]))
        elif e.route == "/about":
            page.views.append(ft.View("/about", [ft.Text("About Page")]))
        else:
            page.views.append(ft.View(e.route, [ft.Text("404 Not Found")]))

        page.update()

    page.on_route_change = route_change  # ルート変更時のハンドラ設定
    page.go("/")  # 初期ルートを設定

ft.app(target=main)