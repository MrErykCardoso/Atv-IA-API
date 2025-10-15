from pylatex import Document, Section, Subsection, Command
from pylatex.utils import NoEscape
import os

def format_to_pdf(title, content, arq_name):
    try:
        doc = Document()
        
        os.makedirs("./PDF", exist_ok=True)

        doc = Document(default_filepath=f'./PDF/{arq_name}', lmodern=False)
        doc.preamble.append(NoEscape(r'\usepackage{fontspec}'))
        doc.preamble.append(Command('title', title))
        doc.preamble.append(Command('author', 'Gerado pela API do Gemini AI'))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))

        with doc.create(Section("Conteúdo gerado")):
            doc.append(content)

        doc.generate_pdf(compiler='xelatex', clean_tex=True)
        print(f"✅ PDF '{arq_name}.pdf' gerado com sucesso!")
        return f"{arq_name}.pdf"
        
    except Exception as e:
        print("❌ Erro ao gerar o PDF:", e)
        return None