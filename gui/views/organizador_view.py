import flet as ft
from pathlib import Path
from backend.organizador import organizar_arquivos


def get_view(page: ft.Page, azul_principal: str):
    """Retorna a view do Organizador de Arquivos."""

    caminho_input = ft.TextField(
        label="Ordnerpfad",
        hint_text="Wählen Sie den Ordner mit den Dateien zum Organisieren aus",
        width=400,
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

    def executar_organizacao(e):
        pasta = caminho_input.value.strip()
        if not pasta or not Path(pasta).exists():
            log_area.value = "❌ Ungültiger Pfad. Bitte wählen Sie einen gültigen Ordner aus."
        else:
            log_area.value = "⏳ Dateien werden organisiert…"
            page.update()
            try:
                logs = organizar_arquivos(pasta)
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
        text="Organisieren",
        icon=ft.Icons.CHECK_CIRCLE,
        bgcolor=azul_principal,
        color=ft.Colors.WHITE,
        on_click=executar_organizacao,
    )

    layout = ft.Column(
        [
            ft.Text("Datei-Organizer", size=28, weight=ft.FontWeight.BOLD, color=azul_principal),
            ft.Text("Organisiert die Dateien im ausgewählten Ordner nach Typ", size=16, weight=ft.FontWeight.BOLD, color=azul_principal, text_align=ft.TextAlign.CENTER),
            ft.Row([caminho_input, botao_pasta]),
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
