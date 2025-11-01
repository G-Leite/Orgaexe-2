import os
import shutil
from pathlib import Path


CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Apresentações": [".pptx", ".ppt", ".odp"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv"],
    "Áudios": [".mp3", ".wav", ".ogg", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executáveis": [".exe", ".msi", ".bat"],
    "Outros": []
}


def organizar_arquivos(pasta: str) -> list[str]:
    """Organiza arquivos em subpastas por categoria."""
    pasta_path = Path(pasta)
    if not pasta_path.exists() or not pasta_path.is_dir():
        raise FileNotFoundError(f"Pasta não encontrada: {pasta}")
    
    logs = []
    for categoria in CATEGORIAS.keys():
        (pasta_path / categoria).mkdir(exist_ok=True)

    for item in pasta_path.iterdir():
        if item.is_file():
            extensao = item.suffix.lower()
            categoria = next((cat for cat, exts in CATEGORIAS.items() if extensao in exts), "Outros")
            destino = pasta_path / categoria / item.name

            contador = 1
            while destino.exists():
                destino = destino.with_name(f"{item.stem}({contador}){item.suffix}")
                contador += 1

            shutil.move(str(item), destino)
            logs.append(f"Movido: {item.name} → {categoria}/{destino.name}")

    if not logs:
        logs.append("Nenhum arquivo para organizar.")
    return logs



  