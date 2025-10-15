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

Execute com o comando "python3 main.py";

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

---

Descrição da tarefa dada pelo professor:

Atividade I
Descrição:
Na aula passada, pediu-se a elaboração de um texto que tratasse do conteúdo ministrados na aula até o momento. Esse material poderia ser escrito com AJUDA (NÃO DE FORMA EXCLUSIVA) de qualquer ferramenta de Inteligência Artificial Generativa.

Os tópicos são:

· Os conceitos básicos da IA e suas aplicações;

· Mudanças históricas da IA;

· A interdisciplinaridade da IA com exemplificações.

Agora, nós podemos iniciar a atividade avaliativa. Você deverá realizar uma transposição textual do documento gerado para um contexto narrativo. Ou seja, o conteúdo deverá ser reescrito como se estivesse sendo contata uma fábula histórica para pessoas que vieram explorar a planeta terra numa época em que os seres humanos foram extintos e só restauram uma inteligência artificial para contar como ela surgiu e suas variações.

No entanto, nós temos algumas regras:

· A IA generativa poderá ser usada, mas via Python e API;

· Todas as requisições e coletas dos resultados deverão ser usadas via linguagem de programação Python;

· No código desenvolvido, vocês deverão organizar e estruturar o documento com o conteúdo de IA numa perspectiva de fábula (recomendo utilizarem o LateX integrado com o Python para isso, no entanto, não é algo obrigatório).

Após realizarem as tarefas, vocês deveram elaborar um relatório. Que deva conter:

· Contexto: a descrição da tarefa desenvolvida;

· Objetivos: geral e específicos;

· Metodologia: relatarem como tudo foi organizado e elaborado (API utilizadas, como os prompts foram construídos, as quantidades de requisições entre o Python e a API da IA, entre outras descrições de como os resultados foram obtidos);

o Arquitetura da solução (fluxo Python → API → pós-processamento → LaTeX/PDF);

o Engenharia de prompts (versões e justificativas).

o Parâmetros da API (max_tokens etc.);

o Controle de versões e reprodutibilidade;

o Critérios de checagem (fontes, datas).

· Resultados:

o Código (trechos principais) + descrição;

o Fábula final (apêndice se preferir manter o PDF separado).

o Tabela de cobertura dos tópicos (onde cada um aparece na fábula).

· Discussão:

o Limitações (alucinações, vieses, custo/latência, variação estocástica);

o O que foi intervenção humana vs. modelo

IMPORTANTE: o conteúdo deve ser obrigatoriamente técnico e real, apenas a forma que ele será apresentado que deve ser no formato de fábula.
