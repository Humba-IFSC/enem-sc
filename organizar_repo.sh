#!/bin/bash

# ==============================================================================
# Script para Automatizar a Criação da Estrutura de Pastas dos Estudos
# Autor: Seu Nome
# Data: 14/10/2025
# ==============================================================================

# Defina aqui a lista com os nomes exatos de cada estudo.
# O script irá iterar sobre esta lista.
ESTUDOS=(
    "Perfil Socioeconômico do Candidato"
    "Qualidade de Ensino nos Institutos Federais"
    "Melhores e Piores Desempenhos (Ranking de Escolas)"
    "Revisão Bibliométrica"
    "Correlação Habilidades vs. Situação-Problema"
    "Desigualdade, Meritocracia e Propostas de Políticas Públicas"
)

echo "🚀 Iniciando a organização do repositório..."
echo "================================================="

# Inicializa o contador para o prefixo numérico das pastas
CONTADOR=1

# Loop principal que itera sobre a lista de estudos
for ESTUDO_NOME_COMPLETO in "${ESTUDOS[@]}"; do
    
    # Formata o contador para ter sempre dois dígitos (01, 02, 03...)
    PREFIXO_NUM=$(printf "%02d" $CONTADOR)

    # Cria um nome de pasta "slug" (amigável para sistemas de arquivos):
    # 1. Converte para minúsculas.
    # 2. Substitui espaços e parênteses por underscores.
    # 3. Remove caracteres especiais para evitar problemas.
    NOME_SLUG=$(echo "$ESTUDO_NOME_COMPLETO" | tr '[:upper:]' '[:lower:]' | sed 's/[ ()]/\_/g' | sed 's/\_vs\_/\_vs_/g' | tr -cd 'a-z0-9_')

    # Monta o nome final da pasta do estudo
    NOME_PASTA_ESTUDO="estudo_${PREFIXO_NUM}_${NOME_SLUG}"

    echo "-> Criando estrutura para: '$ESTUDO_NOME_COMPLETO'"
    echo "   Pasta: ./${NOME_PASTA_ESTUDO}/"

    # Cria a estrutura de subpastas.
    # A flag "-p" garante que o comando não dará erro se a pasta já existir.
    mkdir -p "${NOME_PASTA_ESTUDO}/notebooks"
    mkdir -p "${NOME_PASTA_ESTUDO}/src"
    mkdir -p "${NOME_PASTA_ESTUDO}/figures"
    mkdir -p "${NOME_PASTA_ESTUDO}/data"

    # Cria o arquivo README.md específico para o estudo usando um "here document".
    # Isso permite escrever um bloco de texto de forma limpa.
    cat <<EOF > "${NOME_PASTA_ESTUDO}/README.md"
# Estudo ${CONTADOR}: ${ESTUDO_NOME_COMPLETO}

Este diretório contém todos os artefatos relacionados a este estudo específico.

## 🎯 Objetivos

- (Descreva aqui o objetivo principal deste estudo)
- (Adicione mais objetivos se necessário)

## 📂 Estrutura

- **/notebooks**: Contém os Jupyter Notebooks com as análises exploratórias e o desenvolvimento do estudo.
- **/src**: Contém scripts em Python com funções reutilizáveis.
- **/figures**: Contém os gráficos e visualizações gerados pela análise.
- **/data**: Pasta local para os dados (ignorada pelo .gitignore).

## 📈 Conclusões

- (Resuma aqui as principais conclusões e achados deste estudo)
EOF

    # Incrementa o contador para o próximo estudo
    ((CONTADOR++))
    echo "   ... Estrutura criada com sucesso."
    echo ""
done

echo "================================================="
echo "✅ Processo concluído! Todas as pastas foram criadas."
