import time
from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd

def avaliar_perfil_usuario(comentarios, client):
  sytem  = """
    Você deve avaliar comentários dos usuários, identificando a qual perfil ele se encaixa.
    Retorne apenas o peil do usuário, sem exemplicações adicionais.
  """


  response = client.chat.completions.create(
    model="ft:gpt-4o-2024-08-06:personal:aluraforum-v2:Bak3jnYG",
    messages=[
      {
        "role": "system", 
        "content": sytem
      },
      {
        "role": "user", 
        "content": comentarios
      }
    ]
  )

  return response.choices[0].message.content

def carrega_csv(caminho_dados):
  try:
     data_frame = pd.read_csv(caminho_dados)
     return data_frame
  except Exception as e:
    print(f"Arquivo não encontrado: {caminho_dados}, erro: {e}")
    return None

def agrupar_comentarios_por_usuarios(data_frame):
  resultados = []
  grupos = data_frame.groupby("user_id")
  
  for user_id, grupo in grupos:
    nome = grupo.iloc[0]["nome_completo"]
    comentarios = "\n".join(grupo["comentario"].dropna().tolist())
    resultados.append({
      "user_id": user_id,
      "nome": nome,
      "comentarios": comentarios
    })    
    
  return resultados


def main():    
  load_dotenv()
  openai_api_key = os.getenv("OPENAI_API_KEY")
  client = OpenAI(api_key=openai_api_key)
  data_frame = carrega_csv("dados/comentarios.csv")
  usuarios = agrupar_comentarios_por_usuarios(data_frame)
  
  resultado_avaliacao = []
  for usuario in usuarios:
    parecer = avaliar_perfil_usuario(usuario["comentarios"], client)
    resultado_avaliacao.append({
      "user_id": usuario["user_id"],
      "nome": usuario["nome"],
      "parecer": parecer
    })
    
    print(f"Usuario {usuario['nome']}")
    print(f"Parecer: {parecer}")
  
    time.sleep(50)
  
  
if __name__ == "__main__":
  main()