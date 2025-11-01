import os
from pathlib import Path
from typing import Optional


def renomear_arquivos(pasta: str, prefixo: str, extensao: Optional[str] = None, opcao: int = 1) -> list[str]:
    """
    Renomeia arquivos em uma pasta.

    Args:
        pasta (str): Caminho da pasta com os arquivos.
        prefixo (str): Prefixo usado nos novos nomes.
        extensao (str | None): Extensão alvo (se opcao == 2).
        opcao (int): Define o modo de renomeação:
            1 - Renomeia todos os arquivos (mantém extensões originais).
            2 - Renomeia apenas arquivos da extensão informada.
            3 - Renomeia do mais antigo para o mais recente.

    Returns:
        list[str]: Lista de strings com o log das renomeações.
    """
    pasta = Path(pasta)
    if not pasta.exists() or not pasta.is_dir():
        raise FileNotFoundError(f"Pasta inválida: {pasta}")

    arquivos = [f for f in pasta.iterdir() if f.is_file()]

    # Filtro por extensão se opção 2
    if opcao == 2 and extensao:
        arquivos = [f for f in arquivos if f.suffix.lower() == extensao.lower()]

    if not arquivos:
        return ["Nenhum arquivo encontrado para renomear."]

    # Ordenação
    if opcao == 3:
        arquivos.sort(key=lambda f: f.stat().st_mtime)  # Mais antigo → mais recente
    else:
        arquivos.sort()  # Ordem alfabética padrão

    log = []
    for idx, arquivo in enumerate(arquivos, start=1):
        nova_ext = arquivo.suffix if opcao != 2 or not extensao else extensao
        novo_nome = f"{prefixo}-{idx:02d}{nova_ext}"
        novo_caminho = pasta / novo_nome

        arquivo.rename(novo_caminho)
        log.append(f"{arquivo.name} → {novo_nome}")

    log.append(f"Total renomeado: {len(arquivos)} arquivo(s).")
    return log
