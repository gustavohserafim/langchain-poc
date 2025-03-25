from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/tradutor")

texto = chain_remota.invoke({"idioma": "espanhol", "texto": "Que horas são agora?"})

print(texto)
