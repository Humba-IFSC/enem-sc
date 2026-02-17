#!/bin/bash
LOGFILE="/tmp/notebooklm_mcp_background.log"
echo "--- Starting NotebookLM MCP Background Run at $(date) ---" >> "$LOGFILE"
echo "CWD: $(pwd)" >> "$LOGFILE"
echo "Env PATH: $PATH" >> "$LOGFILE"
echo "Args: $@" >> "$LOGFILE"
/home/humba/Documentos/Meus_Projetos/notebooklm-mcp-fix/.venv/bin/notebooklm-mcp "$@" 2>&1 | tee -a "$LOGFILE"
echo "--- Process exited with code $? at $(date) ---" >> "$LOGFILE"
