# RAG PDF  

Projeto para criar um sistema de Recuperação de Informação com base em documentos PDF usando técnicas de Vetorização e Modelos de Linguagem (RAG - Retrieval Augmented Generation).


## Descrição  

Este projeto carrega documentos PDF, divide o conteúdo em pedaços (chunks), cria embeddings vetoriais para esses pedaços e permite fazer perguntas ao modelo que responde com base na informação encontrada no PDF.

O objetivo é oferecer uma interface simples para consultas inteligentes em documentos PDF, utilizando ferramentas modernas como LangChain, OpenAI Embeddings e ChromaDB.


## Funcionalidades  

- **Carregamento automático de arquivos PDF.**  
- **Divisão dos documentos em chunks com sobreposição para melhor contexto.** 
- **Vetorização dos chunks usando embeddings da OpenAI.** 
- **Pesquisa por similaridade para encontrar trechos relevantes.**
- **Resposta a perguntas com base nas informações extraídas do PDF.**


## Tecnologias utilizadas  

- Python 
- LangChain
- OpenAI Embeddings (necessita chave API)
- Chroma 
- PyMuPDF
- dotenv 


## Como rodar   

1. Configurar a chave da API OpenAI: 
   ```bash
   No arquivo `.env` na raiz do projeto adicione sua chave da OpenAI

2. Baixe as bibliotecas necessárias:  
   ```bash
   pip install langchain langchain_community langchain_chroma langchain_openai python-dotenv pymupdf

3. Ambiente virtual:  
   ```bash
   .venv\Scripts\activate
   
4. Executar o script para pré-processar os dados:  
   ```bash
   python data.py

5. Executar o script para pré-processar os dados:    
   ```bash
   python main.py

   
## Licença

Este projeto está sob a licença **MIT**, uma licença permissiva que permite uso, modificação e distribuição livre do código. Você pode utilizá-lo em projetos pessoais ou comerciais e também contribuir com melhorias.  


