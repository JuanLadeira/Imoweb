.. module:: config

Pacote de configuração
======================

Este pacote contém os arquivos de configuração e módulos para a aplicação.

Subpacotes
----------

.. toctree::
   :maxdepth: 5

   config.settings

Submódulos
----------

Módulo config.celery_app
-------------------------

Este módulo fornece a configuração para o aplicativo Celery.

.. automodule:: config.celery_app
   :members:
   :undoc-members:
   :show-inheritance:

URLs Configuration
==================

Este módulo contém a configuração de URLs para o projeto Django. Ele define as rotas para o Django Admin, URLs de API, páginas de erro e outras ferramentas de desenvolvimento.

.. automodule:: config.urls
    :members:

URLs do Django Admin
--------------------

.. code-block:: python

    path(settings.ADMIN_URL, admin.site.urls),

Esta rota configura o Django Admin. Você pode acessar o Django Admin usando a URL definida em `settings.ADMIN_URL`.

URLs de Arquivos Estáticos
--------------------------

.. code-block:: python

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

Esta configuração serve arquivos estáticos durante o desenvolvimento. Os arquivos são servidos a partir do diretório definido em `settings.MEDIA_ROOT` e acessíveis através da URL definida em `settings.MEDIA_URL`.

URLs da API
-----------
.. _urls-da-api:


.. code-block:: python

    path("api/users/", include("core.users.urls")),
    path("api/auth/", include("core.authentication.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="api-schema"),
        name="api-redoc",
    ),

Estas rotas configuram as URLs da API:

- `api/users/`: Inclui as URLs do aplicativo `core.users`.
- `api/auth/`: Inclui as URLs do aplicativo `core.authentication`.
- `api/schema/`: Exibe o esquema da API usando `drf_spectacular`.
- `api/docs/`: Exibe a documentação da API usando Swagger.
- `api/redoc/`: Exibe a documentação da API usando ReDoc.

URLs de Páginas de Erro
-----------------------

.. code-block:: python

    if settings.DEBUG:
        urlpatterns += [
            path(
                "400/",
                default_views.bad_request,
                kwargs={"exception": Exception("Bad Request!")},
            ),
            path(
                "403/",
                default_views.permission_denied,
                kwargs={"exception": Exception("Permission Denied")},
            ),
            path(
                "404/",
                default_views.page_not_found,
                kwargs={"exception": Exception("Page not Found")},
            ),
            path("500/", default_views.server_error),
        ]

Estas rotas permitem que as páginas de erro sejam depuradas durante o desenvolvimento. Você pode visitar essas URLs no navegador para ver como as páginas de erro se parecem:

- `400/`: Página de erro "Bad Request".
- `403/`: Página de erro "Permission Denied".
- `404/`: Página de erro "Page not Found".
- `500/`: Página de erro "Server Error".

Ferramentas de Desenvolvimento
------------------------------

.. code-block:: python

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

Se o `debug_toolbar` estiver instalado, esta rota adiciona o Django Debug Toolbar às URLs do projeto. A Debug Toolbar pode ser acessada através da URL `__debug__/`.


Módulo config.wsgi
------------------

Este módulo fornece a configuração para o servidor WSGI.

.. automodule:: config.wsgi
   :members:
   :undoc-members:
   :show-inheritance:

Conteúdo do módulo
------------------

Este módulo contém a configuração principal para a aplicação.

.. automodule:: config
   :members:
   :undoc-members:
   :show-inheritance:



