import re

def parse_sources(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    clean_text = []
    capture = False
    
    current_line = ""

    for line in lines:
        if "🤖 NotebookLM R" in line:
            capture = True
            continue
        
        if not capture:
            continue
            
        if "╰──" in line:
            break
            
        # Remove box borders
        content = line.strip()
        if content.startswith('│') and content.endswith('│'):
            content = content[1:-1].strip()
        elif content.startswith('│'):
             content = content[1:].strip()
        
        if not content:
            continue
            
        if content == "keep_pin":
            break
            
        # Heuristic to join lines
        # If content starts with bullet point •, it's a new line.
        # If content looks like a title or category, maybe new line.
        
        if content.startswith("•") or content.startswith("◦") or content.endswith(":"):
            if current_line:
                clean_text.append(current_line)
            current_line = content
        else:
            if current_line:
                if current_line.endswith("-"):
                    current_line = current_line[:-1] + content
                else:
                    current_line += " " + content
            else:
                current_line = content

    if current_line:
        clean_text.append(current_line)

    # Post-processing to formatting markdown
    final_output = []
    final_output.append("# Fontes do Notebook de Correlação")
    final_output.append("")
    
    for text in clean_text:
        # Detect headers/categories (often end with :)
        if text.endswith(":") and not text.startswith("•"):
            final_output.append(f"## {text}")
        elif text.startswith("•"):
            final_output.append(f"- {text[1:].strip()}")
        elif text.startswith("◦"):
             final_output.append(f"  - {text[1:].strip()}")
        else:
            final_output.append(text)
            
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_output))

if __name__ == "__main__":
    parse_sources("fontes_correlacao_raw.txt", "fontes_correlacao.md")
