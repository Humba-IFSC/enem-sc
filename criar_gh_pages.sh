#!/bin/bash

# ==============================================================================
# Script para Automatizar a Criação da Estrutura do GitHub Pages
# Autor: Seu Nome
# Data: 14/10/2025
# ==============================================================================

# A mesma lista de estudos do script anterior para manter a consistência.
ESTUDOS=(
    "Perfil Socioeconômico do Candidato"
    "Qualidade de Ensino nos Institutos Federais"
    "Melhores e Piores Desempenhos (Ranking de Escolas)"
    "Revisão Bibliométrica"
    "Correlação Habilidades vs. Situação-Problema"
    "Desigualdade, Meritocracia e Propostas de Políticas Públicas"
)

# Nome da pasta raiz do GitHub Pages
PASTA_GH_PAGES="docs"

echo "🚀 Iniciando a criação da estrutura para o GitHub Pages..."
echo "================================================="

# Cria a pasta raiz 'docs' se ela não existir.
mkdir -p "$PASTA_GH_PAGES"
echo "-> Pasta principal './${PASTA_GH_PAGES}/' garantida."

# Gera o conteúdo do index.html principal (o portal)
# Primeiro, a parte superior do HTML
cat <<EOF > "${PASTA_GH_PAGES}/index.html"
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal de Relatórios - Observatório de Dados Educacionais</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; margin: 2em; }
        h1, h2 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin-bottom: 10px; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Portal de Relatórios</h1>
    <p>Bem-vindo ao portal de relatórios do Observatório de Dados Educacionais. Clique em um dos links abaixo para visualizar a análise detalhada de cada estudo.</p>
    <h2>Índice de Estudos</h2>
    <ul>
EOF

# Loop para adicionar cada link de estudo ao index.html principal
CONTADOR=1
for ESTUDO_NOME_COMPLETO in "${ESTUDOS[@]}"; do
    PREFIXO_NUM=$(printf "%02d" $CONTADOR)
    NOME_SLUG=$(echo "$ESTUDO_NOME_COMPLETO" | tr '[:upper:]' '[:lower:]' | sed 's/[ ()]/\_/g' | sed 's/\_vs\_/\_vs_/g' | tr -cd 'a-z0-9_')
    NOME_PASTA_ESTUDO="estudo_${PREFIXO_NUM}_${NOME_SLUG}"

    # Adiciona o item da lista ao index.html principal
    echo "        <li><a href=\"./${NOME_PASTA_ESTUDO}/\">Estudo ${CONTADOR}: ${ESTUDO_NOME_COMPLETO}</a></li>" >> "${PASTA_GH_PAGES}/index.html"

    # Cria a subpasta para o estudo dentro de 'docs'
    mkdir -p "${PASTA_GH_PAGES}/${NOME_PASTA_ESTUDO}"

    # Cria o arquivo index.html placeholder para o estudo específico
    cat <<EOF_STUDY > "${PASTA_GH_PAGES}/${NOME_PASTA_ESTUDO}/index.html"
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Estudo ${CONTADOR}: ${ESTUDO_NOME_COMPLETO}</title>
</head>
<body>
    <h1>Estudo ${CONTADOR}: ${ESTUDO_NOME_COMPLETO}</h1>
    <p>Este é o relatório interativo referente ao estudo sobre "${ESTUDO_NOME_COMPLETO}".</p>
    <br>
    <a href="../index.html">Voltar para o portal</a>
</body>
</html>
EOF_STUDY

    echo "   - Estrutura HTML criada para: '${ESTUDO_NOME_COMPLETO}'"

    ((CONTADOR++))
done

# Adiciona a parte final do HTML ao index principal
cat <<EOF >> "${PASTA_GH_PAGES}/index.html"
    </ul>
</body>
</html>
EOF

echo "================================================="
echo "✅ Processo concluído! A pasta './${PASTA_GH_PAGES}/' está pronta para o GitHub Pages."
