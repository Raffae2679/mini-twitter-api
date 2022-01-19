# :computer: Mini Twitter API

Mini twitter API é um projeto utilizando django rest framework, postgres e docker. Atráves dele o usuário pode se cadastrar (tendo um token que expira a cada x tempo durante a sessão), criar posts, seguir outros usuários, ver o feed geral e o feed personalizado dos seguidores.


## :toolbox: Tecnologias Utilizadas
- Python
- Django
- Django Rest Framework
- Docker
- PostgreSQL

## :pushpin: Objetivos
- [x] **Caso 1*: Cadastri de usuário :heavy_check_mark:
- [x] **Caso 2**: Autenticação (login) :heavy_check_mark:
- [x] **Caso 3**: Fazer uma publicação :heavy_check_mark:
- [x] **Caso 4**: Feed Geral :heavy_check_mark:
- [x] **Caso 5**: Feed personalizado :heavy_check_mark:
- [x] Deploy de projeto :heavy_check_mark:
- [x] Upload de arquivos estáticos :heavy_check_mark:
- [x] Servir arquivos estaticos - AWS 3 :heavy_check_mark:


## Executando Localmente

> Caso você não tenha um ambiente virtual configurado para o projeto, como um VirtualEnv ou Anaconda, recomendo configurar um para que todos os passos funcionem sem erros.

1. Clone o repositório no seu ambiente local

$ git clone https://github.com/Raffae2679/mini-twitter-api.git

2. Acesse o diretório que foi criado/clonado

$ cd mini-twitter-api


3. Instale os pacotes python que são requisitos para o `build` do sistema

$ pip install -r requirements.txt


4. Após baixar o projeto, você deve acessar o diretorio /docker e executar o comando afim de criar e iniciar um container contendo um banco de dados postgres local e pg4admin.

$ twitterApi\docker>docker-compose up 


5.Agora você deve criar o banco de dados e realizar as migrações para que o DB esteja pronto para conexão e uso pelo Django

$ python manage.py migrate


6. Crie um superusuário para ter acesso ao /admin

$ python manage.py createsuperuser


> A saída deve ser algo semelhante a isto:

Email:
Password:
Password (again):
Superuser created successfully.


7. Inicie seu servidor local Django

$ python manage.py runserver


> A saída deve ser algo semelhante a isto:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 18, 2022 - 22:57:44
Django version 4.0.1, using settings 'twitterApi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


Pronto! O sistema está rodando no seu servidor local e você pode acessá-lo na URL http://127.0.0.1:8000/ .

## :page_with_curl: Documentação para rotas implementadas

- `http://127.0.0.1:8000/api/login/` (POST): Esse endpoint responsável por realizar o login. Ele é feito passando um json contendo senha e username. Após autorizado o login, é necessário adicionar ao header um campo "Authorization" e passar "Token codigo_disponibilizado_pos_login".
- `http://127.0.0.1:8000/api/logout/` (GET): Esse endpoint é responsável por realizar o logout da api. Basicamente ele apaga o token da sessão, forçando o usuário fazer o login para geração de um novo.
- `http://127.0.0.1:8000/api/cadastrar_usuario/` (POST): Esse endpoint é responsável por realizar cadastro de usuário na api. Deve ser passado um json contendo username, email, password e password_confirm.
- `http://127.0.0.1:8000/api/user_info` (GET): Esse endpoint retorna informação a respeito do usuário, como seu token de segurança, id (necessário para criar posts) e username.
- `http://127.0.0.1:8000/api/criar_post/` (POST): Esse endpoint é responsável por cadastrar posts na api. A criação de um post pode ser feita passando um json ou atráves de um formulário (para enviar imagens).
- `http://127.0.0.1:8000/api/feed_geral/` (GET): Esse endpoint é responsável por retornar os 10 posts recentes da api. 
- `http://127.0.0.1:8000/api/feed_seguidores/` (GET): Esse endpoint é responsável por retornar os posts dos seguidores do usuário. 
- `http://127.0.0.1:8000/api/seguidores/` (GET): Esse endpoint é responsável por retornar um json com os seguidores do usuário.
- `http://127.0.0.1:8000/api/usuarios/` (GET): Esse endpoint é responsável por retornar um json com os usuários da api.
- `http://127.0.0.1:8000/api/seguir/<str:email>/` (POST): Esse endpoint é responsável por realizar a ação de seguir um usuário. Deve ser passado um e-mail através da url desse endpoint, assim o usuário do e-mail será adicionado a lista de seguidores.

### Pgadmin
- O acesso ao pgadmin (executando pelo docker) é feito através do endereço `http://localhost:16543/login?next=%2Fbrowser%2F`
- As credenciais são: Usuario - `admin@linuxhint.com`   |   Senha - `secret`

## :cloud: Deploy
O projeto está feito deploy na plataforma heroku e para acessa-lo, basta [clicar aqui](https://twitter-django-api.herokuapp.com) para acessar. Todas as rotas mencionadas acima, estão em pleno funcionamento no ambiente que está feio o deploy. A diferença é que para acessar, você deve utilizar `https://twitter-django-api.herokuapp.com/` ao invés de `http://127.0.0.1:8000/`

Além disso, os arquivos estáticos estão sendo servidos pelo AWS 3, ou seja, estão sendo salvos nos servidores da AWS.

<br/>

---

<p align="center">Desenvolvido com 💜 por Raffael Morais</p>
