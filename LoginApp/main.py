from controls.controls import (
    ft,
    rgb2hex,
    LoginUsername
)

def main(page: ft.Page):
    page.title = 'Login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.page = ft.padding.all(0)
    page.bgcolor = rgb2hex([221,221,221])

    Row = ft.Row(
        controls=[
            LoginUsername(page=page)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(Row)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)