# 🚀 Projeto: Fine-Tuning GPT com Análise de Sentimentos e pandas

## 📄 Descrição

Fine-tuning de modelo GPT para análise de sentimentos e classificação de perfis em fóruns online, com dados preparados e avaliados usando Python e pandas.

---

## 💡 Como Abrir e Rodar o Projeto Localmente

1. **Clone este repositório** ou baixe o código-fonte.
2. Abra a pasta do projeto no **Visual Studio Code** (ou outro editor).
3. Crie e ative um ambiente virtual.
4. Instale as dependências.
5. Configure as variáveis de ambiente localmente (arquivo `.env`).

### 1. Criar e Ativar o Ambiente Virtual

#### Windows:

```bash
python -m venv venv-fine-tuning
venv-fine-tuning\Scripts\activate.bat
```

#### Mac/Linux:

```bash
python3 -m venv venv-fine-tuning
source venv-fine-tuning/bin/activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## 📊 Análise Avançada com pandas + Integração com Modelos da OpenAI

Exploramos funcionalidades essenciais para análise de dados e preparação para IA:

### ✔️ Frequências com `value_counts()`

```python
contagem_filmes = data_frame_cinema["filme"].value_counts().head(3)
```

* Destaca os filmes mais comentados.

### ✔️ Valores Únicos com `nunique()`

```python
total_usuarios = data_frame_cinema["user_id"].nunique()
```

* Conta quantos usuários distintos existem.

### ✔️ Média com `mean()`

```python
idade_media = data_frame_cinema["idade"].mean()
```

* Obtém a idade média dos usuários.

Outras funções úteis: `.median()`, `.min()`, `.max()`, `.std()`

### ✔️ Filtragem de Dados

```python
data_frame_cinema[data_frame_cinema["user_id"] == user_id]
```

* Seleciona linhas com base em condições.

### ✔️ Extração Otimizada de Dados

```python
nome = data_frame_cinema[data_frame_cinema["user_id"] == user_id].iloc[0]["nome_completo"]
```

* Combinando filtro e posição para extrair informações de forma precisa.

---

## 🧐 Integração com OpenAI para IA Generativa

Após processar os dados com pandas, construímos prompts para modelos OpenAI baseados em:

* Gênero, idade, localização, sentimento
* Filmes mais comentados

```python
prompt = (
    "Baseado nos dados a seguir, sugira uma campanha de marketing criativa..."
)
```

### ⚖️ Fine-Tuning OpenAI

Usamos um modelo fine-tuned:

```python
model="ft:gpt-4o-2024-08-06:alura-aulas:aluracinemav2:BHEGJ2Xp"
```

* Customizado para entender o contexto de cinema e perfis.
* Mais adequado e preciso que o modelo base.

---

## 🔗 pandas + Fine-Tuning = Pipelines Poderosos

Essa combinação permite criar soluções inteligentes para:

* Atendimento ao cliente
* Campanhas de marketing
* Análise de sentimentos
* Personalização de experiência

## 📚 Referência

Curso [Pandas: Conhecendo a Biblioteca - Alura](https://www.alura.com.br/curso-online-pandas)

---

## ✅ Conclusão

Com pandas, transformamos dados brutos em informações valiosas. Com fine-tuning da OpenAI, aplicamos IA de forma contextualizada e eficiente. Essa integração é a base de soluções reais com IA.
