import os
import hashlib
import shutil
from pathlib import Path


def mover_duplicados(pasta: str) -> list[str]:
    """Move arquivos duplicados (baseado em hash) para a pasta 'Duplicados'."""
    pasta_path = Path(pasta)
    if not pasta_path.exists() or not pasta_path.is_dir():
        raise FileNotFoundError(f"Pasta não encontrada: {pasta}")

    destino = pasta_path / "Duplicados"
    destino.mkdir(exist_ok=True)

    hash_map: dict[str, list[Path]] = {}
    logs = []

    def calcular_hash(caminho: Path) -> str:
        sha256 = hashlib.sha256()
        with open(caminho, "rb") as f:
            for bloco in iter(lambda: f.read(8192), b""):
                sha256.update(bloco)
        return sha256.hexdigest()

    for arquivo in pasta_path.iterdir():
        if arquivo.is_file():
            h = calcular_hash(arquivo)
            hash_map.setdefault(h, []).append(arquivo)

    for arquivos in hash_map.values():
        if len(arquivos) > 1:
            original = arquivos[0]
            duplicados = arquivos[1:]
            for dup in duplicados:
                destino_arquivo = destino / dup.name
                contador = 1
                while destino_arquivo.exists():
                    destino_arquivo = destino / f"{dup.stem}({contador}){dup.suffix}"
                    contador += 1
                shutil.move(str(dup), destino_arquivo)
                logs.append(f"Movido duplicado: {dup.name} → {destino_arquivo.name}")

    if not logs:
        logs.append("Nenhum arquivo duplicado encontrado.")
    return logs
