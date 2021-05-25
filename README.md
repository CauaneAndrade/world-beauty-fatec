# World Beauty
**Matéria:** Testes de Software <br>
**Professor:** Gerson Penha Neto

Sistema feito utilizando framework Django, banco de dados PostgreSQL e ambiente Docker/Dockerfile

O grupo World Beauty atua no ramo da estética e beleza, fornecendo serviços como manicure, pedicure, entre outros.
O objetivo é desenvolver um sistema com os seguintes requisitos:
- [x] Cadastro de clientes com as seguintes informações:
    - Nome
    - Telefone
    - Data de nascimento
    - Gênero.
- [x] Edição de um cadastro.
- [x] Remoção de um cadastro.
- [x] Listagem de todos os clientes em ordem alfabética.
- [x] Listagem de somente os clientes de um determinado gênero em ordem alfabética.
- [x] Para cada cliente a lista dos serviços e/ou produtos que este consumiu.
- [x] Relatórios básicos com as seguintes informações:
    - [x] Qual é a idade média de todo o público de uma unidade.
    - [x] Qual é a idade média do público para um determinado gênero.
    - [x] Qual é o serviço mais procurado para todo o público.
    - [x] Qual é o serviço mais procurado para um determinado gênero.
- [x] Capacidade de persistência de dados. A agenda deverá ser salva em algum banco
de dados relacional.

---

## Passos para rodar o sistema localmente

1. Para rodara aplicação

    ```bash
    docker-compose run --rm --service-ports web
    ```

2. Suba o banco de dados

    ```bash
    docker-compose up -d db
    ```

3. Acessando o app
http://localhost:8080/

* Rodar os testes

    ```bash
    docker-compose run --rm web python manage.py test --settings world_beauty.settings.test
    ```

* Rodar o coverage

    ```bash
    docker-compose run --rm web coverage run manage.py test --settings nome_do_novo_projeto.settings.test
    ```

* Cobertura do coverage no terminal

    ```bash
    docker-compose run --rm web coverage report
    ```
