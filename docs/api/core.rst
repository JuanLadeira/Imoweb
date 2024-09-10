core package
============

- **``core.authentication``**: Gerencia os mecanismos de autenticação da aplicação. Utiliza o pacote `drfsimplejwt` para implementar autenticação baseada em JSON Web Tokens (JWT). O conceito de JWT permite que a autenticação seja realizada de forma segura e eficiente, permitindo que o servidor verifique a identidade do usuário sem necessidade de sessões de estado. A implementação inclui a criação, validação e gestão de tokens JWT, garantindo que as comunicações entre cliente e servidor sejam protegidas.

- **``core.contrib``**: Contém pacotes e módulos adicionais que oferecem funcionalidades extras e contribuições para a aplicação, que podem não se encaixar diretamente nos outros subpacotes.

- **``core.users``**: Faz a gestão de usuários da aplicação. Dentro deste subpacote, você encontrará o CRUD (Create, Read, Update, Delete) para os três tipos principais de usuários:
  - **Agentes Imobiliários**: Profissionais que gerenciam e negociam propriedades.
  - **Inquilinos**: Usuários que alugam propriedades.
  - **Proprietários**: Proprietários de propriedades que estão disponíveis para alugar.

Subpackages
-----------

.. toctree::
   :maxdepth: 2

   core.authentication
   core.contrib
   core.users




Submodules
----------

core.conftest module
--------------------

.. automodule:: core.conftest
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: core
   :members:
   :undoc-members:
   :show-inheritance:
