# Orgaexe 2

**ToolKit para Organização de Arquivos**

Aplicativo desktop com interface gráfica que organiza arquivos por tipo, separa arquivos duplicados e renomeia arquivos em lote.

> ⚠️ **Atenção:** o Orgaexe **move** e **renomeia** arquivos, mas não os apaga. Mesmo assim, o programa **não possui função de desfazer**. Antes de usar, teste em uma pasta de teste ou faça uma cópia de segurança.

## Funcionalidades

### 1. Organizador por tipo
Move os arquivos de uma pasta para subpastas de acordo com o tipo:

- imagens vão para a pasta de imagens;
- PDFs e documentos do Word vão para a pasta de documentos;
- todos os demais tipos vão para a pasta de outros.

### 2. Separador de duplicados
Compara os arquivos pelo **hash** (o conteúdo, e não o nome) e move os arquivos idênticos para uma pasta chamada `Duplicados`. Nenhum arquivo é removido.

### 3. Renomeador
Renomeia os arquivos de uma pasta usando um **prefixo escolhido pelo usuário**, seguido de numeração: `prefixo-01`, `prefixo-02`, `prefixo-03` e assim por diante. Por exemplo, com o prefixo `viagem`: `viagem-01`, `viagem-02`, `viagem-03`.

Há três modos:

| Modo | O que faz |
|------|-----------|
| **1. Todos os arquivos** | Renomeia todos os arquivos da pasta. |
| **2. Somente a extensão informada** | Renomeia apenas os arquivos da extensão digitada no campo *extensão*. |
| **3. Do mais antigo para o mais recente** | Renomeia seguindo a ordem de antiguidade; a contagem começa pelo arquivo mais antigo. |

## Interface

Feita com [Flet](https://flet.dev/), com **modo claro e modo escuro**.

<!-- Para adicionar capturas de tela, coloque as imagens em docs/img/ e descomente:
![Tela principal](docs/img/tela-principal.png)
-->

## Como usar

### Opção 1: executável (recomendado)

1. Acesse a página de [Releases](https://github.com/G-Leite/Orgaexe-2/releases/latest).
2. Baixe o arquivo `.exe` da versão mais recente.
3. Execute o programa.

Requisitos: **Windows 10**.

> Baixe o executável somente pela página oficial de Releases deste repositório. Como o arquivo não é assinado digitalmente, o Windows pode exibir um aviso de segurança na primeira execução.

### Opção 2: a partir do código-fonte

```bash
git clone https://github.com/G-Leite/Orgaexe-2.git
cd Orgaexe-2
pip install flet
python main.py
```

## Limitações

- Não há função de desfazer as operações.
- O executável está disponível apenas para Windows 10.

## Status

Versão atual: **2.0.0**, a primeira versão estável.

## Licença

Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
