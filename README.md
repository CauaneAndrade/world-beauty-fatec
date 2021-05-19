# World Beauty

Django e PostgreSQL

## Criando um projeto do zero

1. *.env** com base no .env-sample.
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

2. Dê um build na imagem docker

    ```bash
    docker-compose build
    ```

3. Suba o banco de dados

    ```bash
    docker-compose up -d db
    ```

4. Gere as migrações iniciais

    ```bash
    docker-compose run --rm web python manage.py makemigrations
    ```

5. Execute as migrações iniciais

    ```bash
    docker-compose run --rm web python manage.py migrate
    ```

6. Para rodara aplicação

    ```bash
    docker-compose run --rm --service-ports web
    ```

## Extras

* Rodar os testes

    ```bash
    docker-compose run --rm web python manage.py test --settings world_beauty.settings.test
    ```

* Rodar o linter

    ```bash
    docker-compose run --rm web flake8 .
    ```

* Rodar o coverage

    ```bash
    docker-compose run --rm web coverage run manage.py test --settings nome_do_novo_projeto.settings.test
    ```

* Cobertura do coverage no terminal

    ```bash
    docker-compose run --rm web coverage report
    ```

* Gerar o HTML do coverage

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
