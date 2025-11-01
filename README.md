# Orgaexe

Orgaexe — toolkit para organizar arquivos, remover duplicados e renomear em lote.

## Funcionalidades
- Organizar arquivos por categorias (imagens, documentos, vídeos...)
- Detectar e mover duplicados (SHA-256)
- Renomeador em lote (prefixo, extensão, ordenação por data)

## Como rodar (dev)
```bash
# criar venv (recomendado)
python -m venv venv
source venv/Scripts/activate     # Windows
pip install -r requirements.txt
python main.py
