from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/tradutor")

texto = remote_chain.invoke({"idioma": "espanhol", "texto": "Que horas são agora?"})

print(texto)
