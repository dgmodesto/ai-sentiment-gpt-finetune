from openai import OpenAI 
from dotenv import load_dotenv
import pandas as pd 
import os
import time 
from avaliacao import avaliar_perfil_usuario, carrega_csv

summary_project = """
Ao criar campanhas de marketing personalizadas, é fundamental entender tanto o comportamento dos usuários quanto os conteúdos que mais geram engajamento. Neste exercício, combinamos dados de comentários sobre filmes com perfis dos usuários para gerar sugestões de campanhas criativas, utilizando modelos da OpenAI.

Essa abordagem pode ser usada para análises de público em contextos como plataformas de streaming, cinemas ou aplicativos de recomendação.

Neste exemplo, você vai:

Importar os dados de comentários dos usuários.
Identificar os filmes mais comentados.
Analisar os perfis dos usuários (gênero, localização, sentimento dos comentários etc.).
Avaliar individualmente cada perfil usando um modelo de linguagem.
Gerar automaticamente uma sugestão de campanha de marketing com base nessas informações.
"""

def combinar_informacoes_filmes(data_frame_cinema, top_n=3):
  contagem_filmes = data_frame_cinema["filme"].value_counts().head(top_n)
  resumo = "Filmes mais comentados:\n"
  for filme, contatgem in contagem_filmes.items():
    resumo += f"- {filme}: {contatgem} comentários\n"
    
  return resumo

def combinar_perfil_usuario(data_frame_cinema, client):
  total_usuarios = data_frame_cinema["user_id"].nunique()
  genero_counts = data_frame_cinema["genero"].value_counts()
  sentimento_counts = data_frame_cinema["sentimento"].value_counts()
  idade_media = data_frame_cinema["idade"].mean()
  top_localizacoes = data_frame_cinema["localizacao"].value_counts().head(3)
  
  resumo = f"Perfi dos usuários (total: {total_usuarios} usuários):\n"
  resumo += "Genero: \n"
  for genero, contagem in genero_counts.items():
    resumo += f"- {genero}: {contagem} usuários\n"
    
  resumo += "Sentimento dos comentários: \n"
  for sentimento, contagem in sentimento_counts.items():
    resumo += f"- {sentimento}: {contagem} comentários\n"
    
  resumo += f"Idade média: {idade_media:.2f}\n"
  resumo += "Top localizações: \n"
  for localizacao, contagem in top_localizacoes.items():
    resumo += f"- {localizacao}: {contagem} usuários\n"

  resumo += "Perfis individuais:\n"
  user_ids = data_frame_cinema["user_id"].unique()
  for user_id in user_ids: 
    comentarios = "\n".join(data_frame_cinema[data_frame_cinema["user_id"] == user_id]["comentario"].dropna().tolist())

    perfil = avaliar_perfil_usuario(comentarios, client)
    nome = data_frame_cinema[data_frame_cinema["user_id"] == user_id].iloc[0]["nome_completo"]
    resumo += f"- {nome} (ID: {user_id}):\n{perfil}\n"
  
  return resumo
    
def gerar_parecer_marketing(informacoes_filmes, Informacoes_pefil, 
                              client, model="ft:gpt-4o-2024-08-06:personal:aluraforum-v2:Bak3jnYG"):
  prompt = (
    "Basedo nos dados a seguir, sugira uma camapnha de marketing criativa "
    "para promover os filmes mais comentados e engajar os usuários com os perfis apresentados.\n"
    f"{informacoes_filmes}\n"
    f"{Informacoes_pefil}\n\n"
    "A sugestão deve considerar as características dos filmes, os perfis dos usuários e as tendências de mercado. "
  )
  
  messages = [
    {
      "role": "system",
      "content": "Você é um consultor de marketing especializado em campanhas de marketing criativas."
    },
    {
      "role": "user",
      "content": prompt
    }
  ]
  
  response = client.chat.completions.create(
    model=model,
    messages=messages
  )
  return response.choices[0].message.content

def main():
  load_dotenv()
  openai_api_key = os.getenv("OPENAI_API_KEY")
  client = OpenAI(api_key=openai_api_key)
  
  data_frame_cinema = carrega_csv("dados/comentarios.csv")
  informacoes_filmes = combinar_informacoes_filmes(data_frame_cinema)
  informacoes_perfil = combinar_perfil_usuario(data_frame_cinema, client)
  sugestao_marketing = gerar_parecer_marketing(informacoes_filmes, informacoes_perfil, client)
  
  print("Sugestão de campanha de marketing:")
  print(sugestao_marketing)
  
if __name__ == "__main__":
  main()