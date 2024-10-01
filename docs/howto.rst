How to?
======================================================================

Começando
----------------------------------------------------------------------

A documentação pode ser escrita como arquivos rst em `core/docs`.

Para construir e servir a documentação, use os comandos::

    docker compose -f local.yml up docs

As alterações nos arquivos em `docs/_source` serão detectadas e recarregadas automaticamente.

`Sphinx <https://www.sphinx-doc.org/>`_ é a ferramenta usada para construir a documentação.

De Docstrings para Documentação
----------------------------------------------------------------------

A extensão sphinx `apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_ é usada para documentar automaticamente o código usando assinaturas e docstrings.

Docstrings no estilo Numpy ou Google serão detectados nos arquivos do projeto e estarão disponíveis para documentação. Consulte a extensão `Napoleon <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_ para obter mais detalhes.

Para um exemplo em uso, consulte a `fonte da página <_sources/users.rst.txt>`_ para :ref:`usuários`.

Para compilar automaticamente todas as docstrings em arquivos de origem de documentação, use o comando::

    make apidocs

Isso pode ser feito no contêiner Docker::

    docker run --rm docs make apidocs


Utilizando Taskipy para Acessar Comandos Rapidamente
----------------------------------------------------------------------

Para facilitar a execução de comandos comuns no projeto, utilizamos o `taskipy`. Ele permite que você execute comandos predefinidos de forma rápida e eficiente. Aqui estão os comandos disponíveis:

task build::

    Constrói e inicia os contêineres Docker

task up::

    Inicia os contêineres Docker

task down::

    Para e remove os contêineres Docker

task reset_db::

    Reseta o banco de dados, cria novas migrações e inicia os contêineres

task ruff::   

    Executa o ruff para verificar e corrigir problemas de linting

task manage -- <comando>::

    Executa comandos do Django manage.py

task format::   

    Formata o código usando blue e isort

task test::     

    Executa os testes com pytest e gera relatórios de cobertura

task logs::

    Exibe os logs dos contêineres Docker

task docs::

    Constrói e serve a documentação
    
task docsl::

    Exibe os logs da documentação

task apidocs:: 

    Compila automaticamente todas as docstrings em arquivos de origem de documentação





Como configurar as variaveis de ambiente?
=========================================

.. _como_configurar_variaveis_de_ambiente:

Para configurar as variáveis de ambiente, crie arquivos `.envs/.local/.django` e `.envs/.local/.postgres` para o ambiente local e `.envs/.production/.django` e `.envs/.production/.postgres` para o ambiente de produção.

**Estrutura de Pastas** ::

    .
    ├── .envs
    │   ├── .local
    │   │   ├── .django
    │   │   └── .postgres
    │   └── .production
    │       ├── .django
    │       └── .postgres
    └── .local
        ├── .django
        └── .postgres

Utilize as variaveis de ambiente para configurar o projeto. 

Aqui está um exemplo de como configurar as variáveis de ambiente para o ambiente local e de produção.

**Variáveis de ambiente** ::

    # .envs/.local/.django
    USE_DOCKER=yes
    IPYTHONDIR=/app/.ipython

    REDIS_URL=redis://redis:6379/0

    CELERY_FLOWER_USER="EXEMPLOcHFAFFAFASFADFAVshUNibHrAaLdVxScQBABCZatiiYYFEXEMPLO"
    CELERY_FLOWER_PASSWORD="EXEMPLOqERHNHSHrXZhZCWQCETDAWDAWQ87ogxqYQCLOeFOcUDAWDAW7jDRyWGV5ZnsRsjPKPzwENFvIGDDASDASDOlEXEMPLO"

    # .envs/.local/.postgres
    POSTGRES_USER=postgrexample
    POSTGRES_PASSWORD=example
    POSTGRES_DB=example
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

    # .envs/.production/.django
    USE_DOCKER=no
    IPYTHONDIR=/app/.ipython

    REDIS_URL=redis://redis:6379/0

    CELERY_FLOWER_USER="EXEMPLOcHFAFFAFASFADFAVshUNibHrAaLdVxScQBABCZatiiYYFEXEMPLO"
    CELERY_FLOWER_PASSWORD="EXEMPLOqERHNHSHrXZhZCWQCETDAWDAWQ87ogxqYQCLOeFOcUDAWDAW7jDRyWGV5ZnsRsjPKPzwENFvIGDDASDASDOlEXEMPLO"

    # .envs/.production/.postgres
    POSTGRES_USER=postgrexampleproduction
    POSTGRES_PASSWORD=example
    POSTGRES_DB=example
    POSTGRES_HOST=db
    POSTGRES_PORT=5432



Como iniciar o ambiente de desenvolvimento?
===========================================

Para iniciar o ambiente de desenvolvimento, siga os passos abaixo:

1. Garanta que você tenha o Docker e o Docker Compose instalados em sua máquina.

2. Crie os arquivos de variáveis de ambiente `.envs/.local/.django` e `.envs/.local/.postgres` com as variáveis de ambiente necessárias, conforme descrito em `Como configurar as variaveis de ambiente <howto.html#como-configurar-as-variaveis-de-ambiente>`_.

3. Execute o comando abaixo para construir e iniciar os contêineres Docker::

    task build

4. Execute o comando abaixo para criar o banco de dados e aplicar as migrações::
    
    task migrate

5. Execute o comando abaixo para iniciar os contêineres Docker::

    task up

6. Caso ainda não tenha um superusuário, crie um com o comando abaixo::

    task manage createsuperuser

7. Acesse o Django Admin em `<http://localhost:8000/admin/>`_ e faça login com as credenciais de superusuário.

8. Acesse a documentação da API em `<http://localhost:8000/api/docs/>`_ e faça login com as credenciais de superusuário.

9. Acesse a documentação da API em `<http://localhost:8000/api/redoc/>`_ e faça login com as credenciais de superusuário.

10. Finalize o ambiente de desenvolvimento com o comando abaixo::

    task down