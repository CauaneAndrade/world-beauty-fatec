# Necto Cookie Cutter

Projeto base para novos projetos com Django e PostgreSQL.

## Criando um projeto do zero

1. Clone o projeto

    ```bash
    git clone git@git.znc.com.br:necto/necto-cookie-cutter.git
    ```

2. Crie um ambiente virtual com Django

    *Nós só usaremos ele uma unica vez pra ter acesso ao django-admin.*

    ```bash
    python -m venv env-django
    ```

3. Ative o ambiente virtual

    ```bash
    source env-django/bin/activate
    ```

4. Instale o Django

    ```bash
    pip install Django
    ```

5. Agora sim, crie o projeto com base no necto-cookie-cutter.

    **IMPORTANTE:** Crie o projeto fora da pasta do necto-cookie-cutter.

    ```bash
    django-admin startproject --template necto-cookie-cutter/ -e=py,env-sample,yml nome_do_novo_projeto
    ```

6. Dentro da pasta que foi criado com o nome_do_novo_projeto crie um arquivo **.env**
com base no .env-sample.

    **IMPORTANTE:** Lembre de adicionar/alterar os valores nas variáveis do novo arquivo (.env)
    com os valores pertinentes.

    Exemplo:
    ```
    APP_PORT=8080
    DB_PORT=5678
    SECRET_KEY=string_aleatoria_gerada_pelo_django
    ```
    gerar a SECRET_KEY
    ```
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```

7. Dê um build na imagem docker

    ```bash
    docker-compose build
    ```

8. Suba o banco de dados

    ```bash
    docker-compose up -d db
    ```

9. Gere as migrações iniciais

    ```bash
    docker-compose run --rm web python manage.py makemigrations
    ```
    **IMPORTANTE:** Caso queira alterar o modelo de usuário dentro da app core, faça antes desse comando.

10. Execute as migrações iniciais

    ```bash
    docker-compose run --rm web python manage.py migrate
    ```

11. Para rodara aplicação

    ```bash
    docker-compose run --rm --service-ports web
    ```

## EXTRA

* Para rodar os testes

    ```bash
    docker-compose run --rm web python manage.py test --settings nome_do_novo_projeto.settings.test
    ```

* Para rodar o linter

    ```bash
    docker-compose run --rm web flake8 .
    ```

* Para rodar o coverage

    ```bash
    docker-compose run --rm web coverage run manage.py test --settings nome_do_novo_projeto.settings.test
    ```

* Para ver a cobertura do coverage no terminal

    ```bash
    docker-compose run --rm web coverage report
    ```

* Para gerar o HTML do coverage

    ```bash
    docker-compose run --rm web coverage html
    ```

pip-tools
```bash
pip-compile requeriments.in --gererate-hashes
```

```bash
pip-sync requirements.txt
```

**IMPORTANTE:** SEJA FELIZ! :D
