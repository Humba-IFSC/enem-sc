#!/bin/bash

# Notebook IDs
NOTEBOOK_ENEM="54edf03f-279f-41ca-8f4a-fd23d8fc9d87"
NOTEBOOK_NEW="0b8ee894-e07f-4b64-bc2e-b6f5ce8f318b"

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

function show_help {
    echo "Usage: ./notebook_manager.sh [notebook_alias] [command]"
    echo ""
    echo "Aliases:"
    echo "  modelagem_multivariada : Notebook de Estatística e Modelagem ($NOTEBOOK_ENEM)"
    echo "  Correlacao             : Notebook de Correlação ENEM ($NOTEBOOK_NEW)"
    echo ""
    echo "Commands:"
    echo "  list   : List sources (sends 'Liste as fontes' message)"
    echo "  chat   : Start interactive chat (or send custom message)"
    echo "  login  : Open browser for manual authentication"
    echo ""
    echo "Example:"
    echo "  ./notebook_manager.sh modelagem_multivariada list"
    echo "  ./notebook_manager.sh Correlacao chat \"Summarize this notebook\""
    echo "  ./notebook_manager.sh Correlacao login"
}

if [ -z "$1" ]; then
    show_help
    exit 1
fi

ALIAS=$1
COMMAND=$2
MESSAGE=$3

case $ALIAS in
    "modelagem_multivariada")
        NB_ID=$NOTEBOOK_ENEM
        echo -e "${BLUE}Selected Notebook: Modelagem Multivariada ($NB_ID)${NC}"
        ;;
    "Correlacao")
        NB_ID=$NOTEBOOK_NEW
        echo -e "${BLUE}Selected Notebook: Correlação ($NB_ID)${NC}"
        ;;
    *)
        echo "Unknown alias: $ALIAS"
        show_help
        exit 1
        ;;
esac

MCP_BIN="/home/humba/Documentos/Meus_Projetos/notebooklm-mcp-fix/.venv/bin/notebooklm-mcp"
CONFIG_FILE="/home/humba/.config/notebooklm-mcp/notebooklm-config.json"

if [ "$COMMAND" == "login" ]; then
    echo -e "${GREEN}Starting browser for manual authentication...${NC}"
    echo "Make sure to login in the browser window that appears."
    $MCP_BIN chat -n $NB_ID
elif [ "$COMMAND" == "list" ]; then
    echo -e "${GREEN}Listing sources for notebook...${NC}"
    $MCP_BIN chat -n $NB_ID -m "Liste as fontes deste notebook em formato de lista (incluindo autores e títulos)."
elif [ "$COMMAND" == "chat" ]; then
    if [ -z "$MESSAGE" ]; then
        echo -e "${GREEN}Starting interactive chat...${NC}"
        $MCP_BIN chat -n $NB_ID
    else
        echo -e "${GREEN}Sending message: $MESSAGE${NC}"
        $MCP_BIN chat -n $NB_ID -m "$MESSAGE"
    fi
else
    echo "Unknown command: $COMMAND"
    show_help
    exit 1
fi
