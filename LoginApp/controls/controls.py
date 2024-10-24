import flet as ft
from rgb2hex import rgb2hex
from flet_toast import flet_toast

class LoginUsername(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.width = page.width * 1/4
        self.bgcolor = rgb2hex([244,244,244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color=ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value='Bem Vindo!',
                            color=ft.colors.with_opacity(0.6, 'black'),
                            size=22,
                            weight='bold'
                        ),
                        ft.Text(
                            value='Descobra mais sobre\nConectando se a nós',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=12,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Container(
                    width=90,
                    height=90,
                    border_radius=90,
                    bgcolor=ft.colors.with_opacity(0.08, 'blue'),
                    content=ft.Icon(
                        name=ft.icons.PERSON,
                        color=rgb2hex([58,145,235]),
                        size=80
                    )
                ),
                ft.TextField(
                    hint_text='Username',
                    hint_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.4, 'black'),
                        weight='bold'
                    ),
                    text_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.8, 'black'),
                        weight='bold'
                    ),
                    bgcolor=ft.colors.WHITE,
                    border_radius=8,
                    border_color=ft.colors.WHITE,
                    border_width=2,
                    prefix_icon=ft.icons.PERSON,
                    autofocus=True
                ),
                ft.FloatingActionButton(
                    text='Conecte-se',
                    foreground_color=ft.colors.WHITE,
                    bgcolor=rgb2hex([99,102,245]),
                    width=self.width,
                    height=45,
                    elevation=0,
                    on_click=self.get_password
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            value='Não tenho uma conta',
                            size=12,
                        ),
                        ft.Container(
                            content=ft.Text(
                                value='Criar Conta',
                                color=rgb2hex([225,110,117])
                            ),
                            on_click=self.register_event,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4
                )
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    def get_password(self, e: ft.ControlEvent):
        username = e.control.parent.controls[2].value

        if username:
            e.page.controls.clear()
            e.page.add(LoginPassword(page=e.page, username=username))
        
        else:
            flet_toast.warning(
                page=e.page,
                message='O usuário não existe!',
                position=flet_toast.Position.TOP_RIGHT
            )

    def register_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(Registar(page=e.page))

class LoginPassword(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        username: str
    ):
        super().__init__()
        self.username = username
        self.width = page.width * 1/4
        self.bgcolor = rgb2hex([244,244,244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color=ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value=self.username,
                            color=ft.colors.with_opacity(0.6, 'black'),
                            size=22,
                            weight='bold'
                        ),
                        ft.Text(
                            value='Descobra mais sobre\nConectando se a nós',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=12,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Container(
                    width=90,
                    height=90,
                    border_radius=90,
                    bgcolor=ft.colors.with_opacity(0.08, 'blue'),
                    content=ft.Icon(
                        name=ft.icons.PERSON,
                        color=rgb2hex([58,145,235]),
                        size=80
                    )
                ),
                ft.TextField(
                    hint_text='Username',
                    hint_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.4, 'black'),
                        weight='bold'
                    ),
                    text_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.8, 'black'),
                        weight='bold'
                    ),
                    bgcolor=ft.colors.WHITE,
                    border_radius=8,
                    border_color=ft.colors.WHITE,
                    border_width=2,
                    prefix_icon=ft.icons.KEY,
                    autofocus=True,
                    password=True,
                    can_reveal_password=True
                ),
                ft.FloatingActionButton(
                    text='Entrar',
                    foreground_color=ft.colors.WHITE,
                    bgcolor=rgb2hex([99,102,245]),
                    width=self.width,
                    height=45,
                    elevation=0
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            value='Esqueci minha senha',
                            size=12,
                        ),
                        ft.Container(
                            content=ft.Text(
                                value='Recuperar',
                                color=rgb2hex([225,110,117])
                            ),
                            on_click=self.reset_password_event,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4
                )
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    def reset_password_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(ResetPassword(page=e.page, username=self.username))

class ResetPassword(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        username: str
    ):
        super().__init__()
        self.username = username
        self.ph = FilePicker(self)
        page.overlay.append(self.ph)
        self.width = page.width * 1/4
        self.bgcolor = rgb2hex([244,244,244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color=ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value='Recuperar Conta',
                            color=ft.colors.with_opacity(0.6, 'black'),
                            size=22,
                            weight='bold'
                        ),
                        ft.Text(
                            value='Recupere a sua conta agora\nNão fique fora das novidades',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=12,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                image_pic := ft.Container(
                    width=90,
                    height=90,
                    border_radius=90,
                    image=ft.DecorationImage(
                        src=None,
                        fit=ft.ImageFit.COVER
                    ),
                    bgcolor=ft.colors.with_opacity(0.08, 'blue'),
                    content=ft.Icon(
                        name=ft.icons.PERSON,
                        color=rgb2hex([58,145,235]),
                        size=80
                    ),
                    on_click=lambda _: self.ph.pick_files(
                        dialog_title='Image Picture',
                        file_type=ft.FilePickerFileType.IMAGE
                    )
                ),
                ft.Column(
                    controls=[
                        ft.TextField(
                            value=self.username,
                            hint_text='Username',
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            border_color=ft.colors.WHITE,
                            border_width=2,
                            prefix_icon=ft.icons.PERSON,
                            disabled=True
                        ),
                        ft.TextField(
                            hint_text='Email',
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.8, 'black'),
                                weight='bold'
                            ),
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            border_color=ft.colors.WHITE,
                            border_width=2,
                            prefix_icon=ft.icons.EMAIL,
                            autofocus=True
                        )
                    ],
                    spacing=5
                ),
                ft.FloatingActionButton(
                    text='Recuperar',
                    foreground_color=ft.colors.WHITE,
                    bgcolor=rgb2hex([99,102,245]),
                    width=self.width,
                    height=45,
                    elevation=0,
                    on_click=self.get_confirm_code
                )
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.image_pic = image_pic
    
    def get_confirm_code(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(ConfirmCode(
                page=e.page,
                username=self.username,
                confirm_code='AA123'
            )
        )


class ConfirmCode(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        username: str,
        confirm_code: str
    ):
        super().__init__()
        self.username = username
        self.confirm_code = confirm_code
        self.width = page.width * 1/4
        self.bgcolor = rgb2hex([244,244,244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color=ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value=self.username,
                            color=ft.colors.with_opacity(0.6, 'black'),
                            size=22,
                            weight='bold'
                        ),
                        ft.Text(
                            value='Descobra mais sobre\nConectando se a nós',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=12,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Container(
                    width=90,
                    height=90,
                    border_radius=90,
                    bgcolor=ft.colors.with_opacity(0.08, 'blue'),
                    content=ft.Icon(
                        name=ft.icons.PERSON,
                        color=rgb2hex([58,145,235]),
                        size=80
                    )
                ),
                ft.ResponsiveRow(
                    controls=[
                        ft.TextField(
                            text_align=ft.TextAlign.CENTER,
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.8, 'black'),
                                weight='bold'
                            ),
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            border_color=ft.colors.WHITE,
                            border_width=2,
                            autofocus=True,
                            col={'xs': 2.40, 'sm': 2.40},
                            data=lambda index = i: index,
                            on_change=self.change_value if i < 4 else self.confirm_code_event
                        ) for i in range(5)
                    ]
                ),
                ft.FloatingActionButton(
                    text='Confirmar',
                    foreground_color=ft.colors.WHITE,
                    bgcolor=rgb2hex([99,102,245]),
                    width=self.width,
                    height=45,
                    elevation=0,
                    on_click=self.confirm_code_event
                )
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    def change_value(self, e: ft.ControlEvent):
        textfield: ft.TextField = e.control

        if len(textfield.value.strip()) > 1:
            textfield.value = textfield.value[-1]

        if len(textfield.value.strip()) == 1 and textfield.data() < 4:
            textfield.parent.controls[textfield.data() + 1].focus()
        
        elif len(textfield.value.strip()) == 0 and textfield.data() > 0:
            textfield.parent.controls[textfield.data() - 1].focus()
        
        e.page.update()
    
    def confirm_code_event(self, e: ft.ControlEvent):
        if e.control._get_control_name() == 'textfield':
            textfields: list[ft.TextField] = e.control.parent.controls
        
        else:
            textfields: list[ft.TextField] = e.control.parent.controls[2].controls
        
        values: str = ''.join([textfield.value for textfield in textfields])
        
        if len(values.strip()) == 5 and self.confirm_code == values:
            e.page.controls.clear()
            e.page.add(LoginUsername(page=e.page))
        
        else:
            for textfield in textfields:
                textfield.value = ''
            
            textfields[0].focus()

            flet_toast.warning(
                page=e.page,
                message=f'control: {e.control}',
                position=flet_toast.Position.TOP_RIGHT
            )

class Registar(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.ph = FilePicker(self)
        page.overlay.append(self.ph)
        self.width = page.width * 1/4
        self.bgcolor = rgb2hex([244,244,244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color=ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value='Criar Conta!',
                            color=ft.colors.with_opacity(0.6, 'black'),
                            size=22,
                            weight='bold'
                        ),
                        ft.Text(
                            value='Descubra as melhores novidades\nCriando uma conta conosco',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=12,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                image_pic := ft.Container(
                    width=90,
                    height=90,
                    border_radius=90,
                    image=ft.DecorationImage(
                        src=None,
                        fit=ft.ImageFit.COVER
                    ),
                    bgcolor=ft.colors.with_opacity(0.08, 'blue'),
                    content=ft.Icon(
                        name=ft.icons.PERSON,
                        color=rgb2hex([58,145,235]),
                        size=80
                    ),
                    on_click=lambda _: self.ph.pick_files(
                        dialog_title='Image Picture',
                        file_type=ft.FilePickerFileType.IMAGE
                    )
                ),
                ft.Column(
                    controls=[
                        ft.TextField(
                            hint_text='Email',
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.8, 'black'),
                                weight='bold'
                            ),
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            border_color=ft.colors.WHITE,
                            border_width=2,
                            prefix_icon=ft.icons.EMAIL,
                            autofocus=True
                        ),
                        ft.TextField(
                            hint_text='Username',
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.8, 'black'),
                                weight='bold'
                            ),
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            border_color=ft.colors.WHITE,
                            border_width=2,
                            prefix_icon=ft.icons.PERSON
                        ),
                        ft.TextField(
                            hint_text='Senha',
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.8, 'black'),
                                weight='bold'
                            ),
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            border_color=ft.colors.WHITE,
                            border_width=2,
                            password=True,
                            can_reveal_password=True,
                            prefix_icon=ft.icons.KEY
                        ),
                        ft.TextField(
                            hint_text='Confirmar Senha',
                            hint_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.4, 'black'),
                                weight='bold'
                            ),
                            text_style=ft.TextStyle(
                                size=13,
                                color=ft.colors.with_opacity(0.8, 'black'),
                                weight='bold'
                            ),
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            border_color=ft.colors.WHITE,
                            border_width=2,
                            password=True,
                            can_reveal_password=True,
                            prefix_icon=ft.icons.KEY
                        ),
                    ],
                    spacing=5
                ),
                ft.FloatingActionButton(
                    text='Registar',
                    foreground_color=ft.colors.WHITE,
                    bgcolor=rgb2hex([99,102,245]),
                    width=self.width,
                    height=45,
                    elevation=0
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            value='Já tenho uma conta',
                            size=12,
                        ),
                        ft.Container(
                            content=ft.Text(
                                value='Entrar',
                                color=rgb2hex([225,110,117])
                            ),
                            on_click=self.login_event,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4
                )
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.image_pic = image_pic
    
    def login_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(LoginUsername(page=e.page))

class FilePicker(ft.FilePicker):
    def __init__(
        self,
        control: Registar
    ):
        super().__init__()
        self.on_result = self.file_picker_result
        self.control = control
    
    def file_picker_result(self, e: ft.FilePickerResultEvent):
        image_path: list[str] = []
        if e.files:
            for file in e.files:
                image_path.append(file.name)

            self.control.image_pic.image.src = image_path[-1]
            self.control.image_pic.content = None

        e.page.update()