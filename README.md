# Blog Setup Linux BR

## Descrição

O **Blog Setup Linux BR** é um blog pessoal onde é possível **postar e gerenciar artigos próprios**. Além disso, o sistema consome a API **Top Stories** do **New York Times**, garantindo que as **5 notícias mais recentes sobre tecnologia** sejam sempre exibidas na plataforma.

O projeto é dividido em **dois aplicativos**:

1. **API REST**: Responsável por gerenciar o banco de dados e fornecer os endpoints CRUD.
2. **Frontend (Django Template)**: Consome a API e renderiza as páginas usando **Django Template, CSS e Bootstrap**.

## Tecnologias Utilizadas

- **Python 3.x**
- **Django** (Backend e Templates)
- **Django Rest Framework (DRF)**
- **Django-Knox** (Autenticação via Token)
- **SQLite ** (Banco de Dados)
- **Bootstrap** (Estilização do Frontend)
- **API Top Stories do NY Times**

## Instalação e Configuração

### 1. Clonar o Repositório

```sh
git clone https://github.com/seu-usuario/blog-setup-linux-br.git
cd blog-setup-linux-br
```

### 2. Criar e Ativar um Ambiente Virtual

```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar as Dependências

```sh
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

```sh
python manage.py migrate
```


### 5. Configurar o Banco de Dados

```sh
python manage.py migrate
```

### 6. Criar arquivo .env na raiz do projeto

```sh
NYT_API_KEY=SUA-API-KEY-DO-NYT-TOP-STORIES
SECRET_KEY=SUA-CHAVE-SECRETA
INTERNAL_URL=http://localhost:8000/
```

### 7. Criar pasta media na raiz do projeto

```sh
/media/
```

### 8. Executar o Servidor

```sh
python manage.py runserver
```



Acesse o sistema em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Endpoints da API

### Autenticação

- **`POST /auth/login/`** - Rota para autenticação, utilizando **Django-Knox** para gerar um token.
- **`POST /auth/logout/`** - Rota para desautenticação.

### Gerenciamento de Autores

- **`GET /authors/`** - Lista os autores cadastrados.
- **`POST /authors/`** - Cadastra um autor (**exige autenticação via token**).
- **`GET /authors/<id>/`** - Retorna detalhes de um autor específico.
- **`PUT /authors/<id>/`** - Atualiza um autor (**exige autenticação**).
- **`DELETE /authors/<id>/`** - Exclui um autor (**exige autenticação**).

### Gerenciamento de Artigos

- **`POST /articles/`** - Cria um artigo (**exige autenticação e o ID de um autor**).
- **`GET /articles/`** - Lista os artigos mais recentes.
- **`GET /articles/<id>/`** - Retorna detalhes de um artigo específico.
- **`PUT /articles/<id>/`** - Atualiza um artigo (**exige autenticação**).
- **`DELETE /articles/<id>/`** - Exclui um artigo (**exige autenticação**).
- **`GET /articles/<slug>/`** - Retorna informações detalhadas do artigo pelo **slug**.

### Integração com NY Times

- **`GET /articles/nyt/tech/`** - Retorna as **5 notícias mais recentes sobre tecnologia** do **NY Times**, filtrando e serializando apenas os dados necessários para o frontend.


## Estrutura das Views do Frontend

![Captura de tela de 2025-03-01 22-43-20](https://github.com/user-attachments/assets/40b1544f-7db6-4535-9434-7b643e587cb3)

- **`login`** → Renderiza um formulário de login e realiza autenticação tanto pelo `django-authenticate` quanto no endpoint `Django-Knox` da API. O token é salvo no **localStorage**.
- **`logout`** → Não renderiza template, apenas consome a rota de logout da API, desautenticando o usuário e redirecionando para `index`.

![Captura de tela de 2025-03-01 21-59-44](https://github.com/user-attachments/assets/36014cd7-f863-430a-a435-5249aacf0f44)

![Captura de tela de 2025-03-01 21-59-49](https://github.com/user-attachments/assets/b65b0ea2-9223-44da-a3ed-ed6d3d421fbd)

- **`index`** → Renderiza a página inicial do blog, consumindo dois endpoints da API: um que retorna as notícias próprias e outro que retorna as notícias do **NYTimes**.

![Captura de tela de 2025-03-01 21-59-18](https://github.com/user-attachments/assets/a10b6e92-4618-4321-a851-19ca2d7a8944)

![Captura de tela de 2025-03-01 21-59-28](https://github.com/user-attachments/assets/3776f595-3806-4ef5-bb5b-1f93d680197d)

- **`full_article`** → Renderiza a página de visualização do post completo, consumindo a rota da API correspondente e a do **NYTimes** para preencher a seção lateral (**aside**).

![Captura de tela de 2025-03-01 22-00-22](https://github.com/user-attachments/assets/2bc24c90-4521-455e-8958-b36455c7d5f9)

- **`editorial`** → Área reservada para gerenciamento dos artigos, requer autenticação e exibe uma tabela com os artigos recuperados do banco de dados.

![Captura de tela de 2025-03-01 22-00-38](https://github.com/user-attachments/assets/40c4669e-2add-411a-b9b9-920f0a080769)

- **`edit_article`** → Formulário para edição de um artigo existente.

![Captura de tela de 2025-03-01 22-00-30](https://github.com/user-attachments/assets/bd576f63-364e-49f8-a964-803d9d0fa69c)

- **`new_article`** → Formulário para cadastro de um novo artigo.



