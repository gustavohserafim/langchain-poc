from dotenv import load_dotenv
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

API_TOKEN = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o-mini",
)
parser = StrOutputParser()

message_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Traduza o texto a seguir para {idioma}"),
        ("user", "{texto}"),
    ]
)

chain = message_template | model | parser

print(chain.invoke({"idioma": "francês", "texto": "Você gosta de tomar café?"}))
