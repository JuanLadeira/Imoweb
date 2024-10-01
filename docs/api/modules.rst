Introdução ao IMOWEB BACKEND
============================

Bem-vindo à documentação da aplicação IMOWEB. Esta aplicação está estruturada de maneira a garantir uma organização clara e modular, facilitando a manutenção e a expansão. O projeto está dividido principalmente em duas pastas: ``config`` e ``core``. A seguir, detalhamos o propósito de cada uma dessas pastas e os principais componentes que elas contêm.

Estrutura do Projeto
--------------------

Pasta ``config``
~~~~~~~~~~~~~~~~

A pasta ``config`` é responsável por armazenar todas as configurações relacionadas ao projeto. É aqui que você encontrará:

- **Configurações de Rota da API**: Arquivos e definições que determinam como as rotas da API são gerenciadas e configuradas.
- **Arquivo ``wsgi``**: Este arquivo é crucial para a execução da aplicação em ambientes de produção, fornecendo a interface entre o servidor web e a aplicação.
- **Pasta ``settings``**: Contém vários arquivos de configuração para diferentes ambientes:
  - ``base.py``: Configurações comuns a todos os ambientes.
  - ``local.py``: Configurações específicas para o ambiente de desenvolvimento local.
  - ``production.py``: Configurações específicas para o ambiente de produção.
  - ``test.py``: Configurações para o ambiente de testes.

Pasta ``core``
~~~~~~~~~~~~~~~

A pasta ``core`` contém a lógica central da aplicação e é onde a maior parte do código da aplicação reside. Aqui você encontrará:

- **Módulos e Pacotes Principais**: Implementações de funcionalidades essenciais e o código que define o comportamento principal da aplicação.
- **Arquivos de Configuração de Teste**: Arquivos que configuram testes automatizados e garantem que o código funcione conforme o esperado.

Navegação
---------

Utilize a árvore de conteúdo (toctree) para navegar facilmente entre as seções da documentação. As seções principais são:

- **config**: Detalhes sobre as configurações do projeto.
- **core**: Informações sobre a lógica principal da aplicação.


.. toctree::
   :maxdepth: 4

   config
   core


