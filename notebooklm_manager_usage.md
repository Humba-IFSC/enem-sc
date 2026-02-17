# Guia de Uso: Gerenciador do NotebookLM (`notebook_manager.sh`)

Este script facilita a interação com múltiplos cadernos do Google NotebookLM via linha de comando, utilizando o servidor MCP configurado.

## Visão Geral

O script atua como um "wrapper" (invólucro) para o comando `notebooklm-mcp`, gerenciando automaticamente os IDs dos cadernos para que você não precise decorá-los.

## Aliases (Apelidos)

Os seguintes apelidos foram configurados para os seus cadernos:

| Alias | Descrição | Notebook Original |
| :--- | :--- | :--- |
| **`modelagem_multivariada`** | Caderno focado em Estatística e Modelagem. | (Antigo "ENEM") |
| **`Correlacao`** | Caderno focado em Correlação e TBR-2D-BO. | (Antigo "Novo") |

## Comandos Disponíveis

| Comando | Descrição |
| :--- | :--- |
| `list` | Envia automaticamente o prompt "Liste as fontes..." para o caderno. |
| `chat` | Inicia um chat interativo ou envia uma mensagem específica. |
| `login` | Abre uma janela do navegador para autenticação manual (caso o token expire). |

## Exemplos de Uso

### 1. Listar fontes

Para listar as fontes do caderno de **Correlação**:
```bash
./notebook_manager.sh Correlacao list
```

Para listar as fontes do caderno de **Modelagem Multivariada**:
```bash
./notebook_manager.sh modelagem_multivariada list
```

### 2. Conversar com o caderno (Chat Interativo)

Para abrir um chat interativo com o caderno de **Correlação**:
```bash
./notebook_manager.sh Correlacao chat
```
*(Digite `quit` para sair do chat)*

### 3. Enviar uma pergunta rápida

Para perguntar algo específico sem abrir o modo interativo:
```bash
./notebook_manager.sh modelagem_multivariada chat "Qual é o resumo do arquivo de Estatística Básica?"
```

### 4. Fazer Login

Se o sistema informar que você precisa se autenticar, use:
```bash
./notebook_manager.sh Correlacao login
```
*(Uma janela do navegador abrirá. Faça login na sua conta Google e feche a janela ou pressione Enter no terminal quando terminar).*
