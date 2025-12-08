import os
import shutil
from pathlib import Path


CATEGORIAS = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Dokumente": [".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf"],
    "Tabellen": [".xlsx", ".xls", ".csv"],
    "Präsentationen": [".pptx", ".ppt", ".odp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audiodateien": [".mp3", ".wav", ".ogg", ".flac"],
    "Komprimierte": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Ausführbare": [".exe", ".msi", ".bat"],
    "Andere": []
}


def organizar_arquivos(pasta: str) -> list[str]:
    """Organiza arquivos em subpastas por categoria."""
    pasta_path = Path(pasta)
    if not pasta_path.exists() or not pasta_path.is_dir():
        raise FileNotFoundError(f"Ordner nicht gefunden: {pasta}")
    
    logs = []
    for categoria in CATEGORIAS.keys():
        (pasta_path / categoria).mkdir(exist_ok=True)

    for item in pasta_path.iterdir():
        if item.is_file():
            extensao = item.suffix.lower()
            categoria = next((cat for cat, exts in CATEGORIAS.items() if extensao in exts), "Andere")
            destino = pasta_path / categoria / item.name

            contador = 1
            while destino.exists():
                destino = destino.with_name(f"{item.stem}({contador}){item.suffix}")
                contador += 1

            shutil.move(str(item), destino)
            logs.append(f"Verschoben: {item.name} → {categoria}/{destino.name}")

    if not logs:
        logs.append("Keine doppelten Dateien gefunden.")
    return logs



  