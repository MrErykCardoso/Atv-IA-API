from api_gemini import gen_text
from formatador_latex import format_to_pdf

def start_chat():
    print("🤖 API de acesso (Powered by Google Gemini!)\n\n")
    print("💬 Insira seu contexto abaixo (ou 'sair' para encerrar): ")
    
    while True:
        prompt = input("🧠 Você: ")
        
        if prompt.lower() in ["sair", "Sair", "quit", "Quit"]:
            print("\n👋 Encerrando a conversa. Até mais!\n")
            break

        res = gen_text(prompt)
        
        print("\n🤖 IA:", res )
        print("-" * 60, "\n")
        
        pdf = input("Gostaria de inserir essa resposta em um documento PDF (s ou n)?")
        if pdf.lower() in ["s", "sim"]:
            print("-" * 60, "\n")
            print("\n🍷📄 Informações do PDF: ")
            title = input("\n\n💡 Insira o título do PDF: ")
            arq_name = input("\n💡 Insira o nome do arquivo: ")
            content = res
            
            format_to_pdf(title, content, arq_name)
            
    
if __name__ == "__main__":
    start_chat()