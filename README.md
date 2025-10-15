# Atv-IA-API

Criação de uma API básica para se comunicar com a API de um serviço de IA para a resolução da atividade proposta pelo Prf. Alex Oliveira Barradas Filho da UFMA na cadeira de Inteligência artificial:

A api escolhida foi o a da google ai studio no modelo "gemini-2.5-flash";
Conexão estabelecida com o token de acesso "GEMINI_API_KEY" que deve ser fixada em um arquivo ".env" na pasta raiz do programa;

Antes de instalar as dependências, considere iniciar um ambiente virtual python:
(Requisitos):

- Instalação do python3 client e do gerenciador de pacotes pip: "sudo apt install python3 pip";
- Na pasta do programa, execute: "python3 -m venv venv";
- Inicialização do ambiente virtual: "source venv/bin/activate";

Para um bom funcionamento são necessárias as dependências:

- sudo apt update -> atualiza os programas no Linux;
- sudo apt install texlive-latex-base texlive-xetex texlive-latex-extra texlive-fonts-recommended fonts-noto-color-emoji -> Para um bom funcionamento do gerador de PDF via PyLatex;
- "pip install -q -U google-genai" -> biblioteca SDK da IA generativa do google para python;
- Para outras dependências veja o arquivo "requisitos.txt" e execute o comando "pip install -r requisitos.txt";

Arquitetura básica da aplicação:

🙋🏻 [main.py] (Usuário escreve a pergunta)
↓
chama função
↓
🤖 [api_gemini.py] ---> envia requisição → [Google gemini API] → retorna texto
↓
resposta formatada
↓
📝 [formatador_latex.py] (gera PDF e grada na pasta PDF)
