import flet as ft


def main(page: ft.Page):
    from gui.views import organizador_view, duplicados_view, renomeador_view
    # Configurações iniciais
    page.title = "Orgaexe"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window_min_width = 900
    page.window_min_height = 600



    #Cores base
    azul_principal = ft.Colors.BLUE_ACCENT_400
    texto_claro = ft.Colors.GREY_200

    # Tema claro
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE_ACCENT_400,
            background=ft.Colors.GREY_50,
            on_primary=ft.Colors.WHITE,
            on_background=ft.Colors.BLACK,
        ),
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=ft.Colors.BLACK),
            body_large=ft.TextStyle(color=ft.Colors.BLACK),
        ),
    )



    # Tema escuro
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE_ACCENT_400,
            background=ft.Colors.BLUE_GREY_900,
            on_primary=ft.Colors.BLACK,
            on_background=ft.Colors.WHITE,
        ),
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=ft.Colors.GREY_200),
            body_large=ft.TextStyle(color=ft.Colors.GREY_100),
        ),
    )



    # Controle de tema (claro/escuro)
    def alternar_tema(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        )
        botao_tema.icon = (
            ft.Icons.LIGHT_MODE if page.theme_mode == ft.ThemeMode.DARK else ft.Icons.DARK_MODE
        )
        page.update()



    # Botão do tema no canto superior direito
    botao_tema = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE if page.theme_mode == ft.ThemeMode.DARK else ft.Icons.DARK_MODE,
        tooltip="Alternar tema",
        on_click=lambda e: alternar_tema(e),
    )

    # AppBar superior 
    page.appbar = ft.AppBar(
        title=ft.Text("Orgaexe", color=azul_principal, weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor=ft.Colors.BLUE_GREY_900,
        actions=[
            ft.IconButton(
                icon=ft.Icons.LIGHT_MODE if page.theme_mode == ft.ThemeMode.DARK else ft.Icons.DARK_MODE,
                tooltip="Alternar tema",
                on_click=lambda e: alternar_tema(e),
            )
        ]
    )

    # --- Views (telas) ---
    def home_view():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Willkommen bei Orgaexe", size=32, weight=ft.FontWeight.BOLD, color=azul_principal),
                    ft.Text(
                        "Organisieren Sie Ihre Dateien ganz einfach und machen Sie Ihren Tag produktiver."
                        "Wählen Sie ein Werkzeug im seitlichen Menü, um zu starten.",
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            expand=True,
        )

# --- Inicializa as views importadas ---
    views = {
        0: home_view(),
        1: organizador_view.get_view(page, azul_principal),
        2: duplicados_view.get_view(page, azul_principal),
        3: renomeador_view.get_view(page, azul_principal),
    }

    # --- Função para alternar entre as views ---
    def set_view(index: int):
        body.content = views[index]
        nav_rail.selected_index = index
        page.update()



    # NavigationRail (menu lateral)
    nav_rail = ft.NavigationRail(
        selected_index=0,
        bgcolor=ft.Colors.BLUE_GREY_900,
        extended=False,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Start"),
            ft.NavigationRailDestination(icon=ft.Icons.FOLDER, label="Organisieren"),
            ft.NavigationRailDestination(icon=ft.Icons.FILTER_NONE, label="Duplikate"),
            ft.NavigationRailDestination(icon=ft.Icons.DRIVE_FILE_RENAME_OUTLINE, label="Umbenennen"),
        ],
        on_change=lambda e: set_view(e.control.selected_index),
    )


    # Dicionário de views
    views = [
    home_view(),
    organizador_view.get_view(page, azul_principal),
    duplicados_view.get_view(page, azul_principal),
    renomeador_view.get_view(page, azul_principal),
    ]      

    # Área principal
    body = ft.Container(content=views[0], expand=True)


    # Layout principal
    layout = ft.Column(
        [
            
            ft.Row(
                [
                    ft.Container(content=nav_rail, width=100, bgcolor=ft.Colors.BLUE_GREY_900),
                    body,
                ],
                expand=True,
            ),
            
            #RODAPÉ
            ft.Container(
                content=ft.Text(
                    "© 2025 G.F.L Melk",
                    size=14,
                    color=ft.Colors.GREY_500,
                    text_align=ft.TextAlign.CENTER,
                ),
            alignment=ft.alignment.center,
            padding=10,
            ), 
        ],
        expand=True,
    )

    page.window_icon = "assets/icon.png"

    page.add(layout)

    


ft.app(target=main)
