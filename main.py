from dotenv import load_dotenv
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

API_TOKEN = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
    model="gpt-4o-mini",
)
parser = StrOutputParser()
chain = modelo | parser


template_mensagem = ChatPromptTemplate.from_messages(
    [
        ("system", "Traduza o texto a seguir para {idioma}"),
        ("user", "{texto}"),
    ]
)

chain = template_mensagem | modelo | parser

print(chain.invoke({"idioma": "francês", "texto": "Você gosta de tomar café?"}))
