import flet as ft
from pathlib import Path
from backend.renomeador import renomear_arquivos


def get_view(page: ft.Page, azul_principal: str):
    """Retorna a view do Renomeador de Arquivos."""

    caminho_input = ft.TextField(
        label="Ordnerpfad",
        width=400,
        hint_text="Wählen Sie den Ordner mit den Dateien zum Umbenennen aus",
    )

    prefixo_input = ft.TextField(label="Präfix", width=200)
    extensao_input = ft.TextField(label="Erweiterung (optional)", width=150, hint_text=".jpg, .txt, usw.")

    modo_dropdown = ft.Dropdown(
        label="Modo",
        options=[
            ft.dropdown.Option("1 - Alle Dateien"),
            ft.dropdown.Option("2 - Nur angegebene Erweiterung"),
            ft.dropdown.Option("3 - Vom ältesten zum neuesten"),
        ],
        value="1 - Alle Dateien",
        width=300,
    )

    log_area = ft.TextField(
        label="Logs",
        multiline=True,
        read_only=True,
        min_lines=10,
        max_lines=20,
        expand=True,
    )

    def selecionar_pasta(e):
        def pasta_escolhida(result: ft.FilePickerResultEvent):
            if result.path:
                caminho_input.value = result.path
                page.update()

        picker = ft.FilePicker(on_result=pasta_escolhida)
        page.overlay.append(picker)
        page.update()
        picker.get_directory_path()

    def executar_renomeacao(e):
        pasta = caminho_input.value.strip()
        prefixo = prefixo_input.value.strip()
        extensao = extensao_input.value.strip() or None
        opcao = int(modo_dropdown.value[0])  # Pega o número da opção (1, 2 ou 3)

        if not pasta or not Path(pasta).exists():
            log_area.value = "❌ Ungültiger Pfad. Bitte wählen Sie einen gültigen Ordner aus."
        elif not prefixo:
            log_area.value = "⚠️ Geben Sie ein Präfix ein"
        else:
            log_area.value = "⏳ Dateien werden umbenannt..."
            page.update()
            try:
                logs = renomear_arquivos(pasta, prefixo, extensao, opcao)
                log_area.value = "\n".join(logs)
            except Exception as err:
                log_area.value = f"Erro: {err}"
        page.update()

    botao_pasta = ft.ElevatedButton(
        text="Ordner auswählen",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=selecionar_pasta,
    )

    botao_executar = ft.ElevatedButton(
        text="Umbenennen",
        icon=ft.Icons.DRIVE_FILE_RENAME_OUTLINE,
        bgcolor=azul_principal,
        color=ft.Colors.WHITE,
        on_click=executar_renomeacao,
    )

    layout = ft.Column(
        [
            ft.Text("Datei-Umbenenner", size=28, weight=ft.FontWeight.BOLD, color=azul_principal),
            ft.Text("Benennt die Dateien nach Ihrer Auswahl um, z.B. nach Präfix, Erweiterung oder Datum. Muster: name-01.docx, name-02.docx", size=16, weight=ft.FontWeight.BOLD, color=azul_principal, text_align=ft.TextAlign.CENTER),
            ft.Row([caminho_input, botao_pasta]),
            ft.Row([prefixo_input, extensao_input, modo_dropdown]),
            ft.Row([botao_executar]),
            ft.Divider(height=20, color="transparent"),
            log_area,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        expand=True,
    )

    return ft.Container(
        content=layout,
        padding=30,
        expand=True,
    )
