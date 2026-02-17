import json
import re

def parse_and_generate(input_file, output_file):
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

    # Find JSON array
    match = re.search(r'\[.*\]', full_text)
    if not match:
        # Try to find from start explicitly if regex fails due to heavy nesting or formatting
        start = full_text.find('[')
        end = full_text.rfind(']')
        if start != -1 and end != -1:
            json_str = full_text[start:end+1]
        else:
            print("No JSON found in output")
            return
    else:
        json_str = match.group(0)
    
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        # Try a more aggressive cleanup if needed
        # Replace smart quotes, etc.
        return

    # Generate HTML
    html_rows = ""
    for item in data:
        # Default keys might vary, handle lowercase/normalization if needed
        title = item.get('titulo', item.get('Título', ''))
        authors = item.get('autores', item.get('Autores', ''))
        summary = item.get('resumo', item.get('Resumo', ''))
        keywords = item.get('palavras_chave', item.get('Palavras-chave', ''))
        if isinstance(keywords, list):
            keywords = ", ".join(keywords)
        alignment = item.get('alinhamento', item.get('Alinhamento', ''))

        html_rows += f"""
                        <tr class="border-b border-slate-100 hover:bg-slate-50 transition">
                            <td class="p-6 font-bold text-navy-dark">{title}</td>
                            <td class="p-6 text-xs text-slate-500">{authors}</td>
                            <td class="p-6 text-xs text-slate-600 leading-relaxed">{summary}</td>
                            <td class="p-6">
                                <span class="bg-blue-50 text-blue-600 px-3 py-1 rounded-full text-[9px] font-black uppercase tracking-widest">{keywords}</span>
                            </td>
                            <td class="p-6 text-xs italic text-slate-500 border-l border-slate-100">{alignment}</td>
                        </tr>
        """

    full_html = f"""
        <!-- SECÇÃO: FONTES & MATERIAIS -->
        <section id="fontes" class="page-content hidden section-animate space-y-12">
            <div class="border-l-8 border-navy-medium pl-6 space-y-2">
                <h2 class="text-3xl font-black uppercase text-navy-dark">Fontes & Materiais</h2>
                <p class="text-slate-500 italic">Acervo documentado e alinhado ao protocolo TBR-2D-BO.</p>
            </div>

            <div class="bg-white rounded-[2.5rem] shadow-xl overflow-hidden border border-slate-200">
                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full text-left min-w-[1000px]">
                        <thead class="bg-navy-medium text-white text-[10px] uppercase tracking-widest">
                            <tr>
                                <th class="p-6 w-1/5">Título</th>
                                <th class="p-6 w-1/6">Autores</th>
                                <th class="p-6 w-1/4">Resumo</th>
                                <th class="p-6 w-1/6">Palavras-chave</th>
                                <th class="p-6 w-1/5">Alinhamento TBR-2D-BO</th>
                            </tr>
                        </thead>
                        <tbody class="text-[11px] leading-relaxed">
                            {html_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
    """

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)

if __name__ == "__main__":
    parse_and_generate("fontes_json_raw.txt", "sources_section.html")
