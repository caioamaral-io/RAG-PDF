from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

CAMINHO_DB = "db"

prompt_template = """
Responda a pergunta do cliente:
{perguta}

baseado nessas informações:

{base_conhecimento}"""

def perguntar():
    pergunta = input("Digite sua pergunta: ")

    funcao_embinding = OpenAIEmbeddings()
    db = Chroma(persist_directory=CAMINHO_DB, embedding_function=funcao_embinding)

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=3)
    if len(resultados) == 0 or resultados[0][1] < 0.7:
        print("Não tive nenhuma informação relevante para responder sua pergunta.")
        return
    
    texto_resultado = []
    for resultado in resultados:
        texto = resultado[0].page_content
        texto_resultado.append(texto)

    base_conhecimento = "\n\n----\n\n".join(texto_resultado)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke({"perguta": pergunta, "base_conhecimento": base_conhecimento})

    modelo = ChatOpenAI()
    texto_resposta = modelo.ivoke(prompt)
    print("Resposta da IA:", texto_resposta)

perguntar()
