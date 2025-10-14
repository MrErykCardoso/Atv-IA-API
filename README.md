# Atv-IA-API
Criação de uma API básica para se comunicar com a API de um serviço de IA para a resolução da atividade proposta pelo Prf. Alex Oliveira Barradas Filho da UFMA na cadeira de Inteligência artificial:

A api escolhida foi o a da google ai studio no modelo "gemini-2.5-flash";

Conexão estabelecida com o token de acesso "GEMINI_API_KEY";

Acesso realizado atravez da biblioteca SDK da IA generativa do google para python instalável via "pip install -q -U google-genai". Para outras dependências veja o arquivo "requisitos.txt".

Arquitetura básica da aplicação:

🙋🏻 [main.py] (Usuário escreve a pergunta)
     ↓
  chama função
     ↓
🤖 [api_gemini.py]  --->  envia requisição → [Google gemini API] → retorna texto
     ↓
  resposta formatada
     ↓
📝 [formatador_latex.py] (gera PDF)

