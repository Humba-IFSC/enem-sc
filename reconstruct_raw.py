def reconstruct(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    full_text = ""
    capture = False
    
    for line in lines:
        if "🤖 NotebookLM R" in line:
            capture = True
            continue
        
        if not capture:
            continue
            
        if "╰──" in line:
            break
            
        content = line.strip()
        # Remove box borders
        if content.startswith('│') and content.endswith('│'):
            content = content[1:-1].strip()
        elif content.startswith('│'):
             content = content[1:].strip()
        
        if content == "keep_pin":
            break
            
        full_text += content + " "

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_text)

if __name__ == "__main__":
    reconstruct("tabela_fontes_raw.txt", "tabela_debug.txt")
