config.settings package
=======================

Submodules
----------

config.settings.base module
---------------------------


Configurações Base
==================

Este módulo contém as configurações base para construir outros arquivos de configurações.

.. automodule:: config.settings.base
    :members:

Configurações Gerais
-------------------------


   .. code-block:: python

      BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
      APPS_DIR = BASE_DIR / "core"
      env = environ.Env()

      READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
      if READ_DOT_ENV_FILE:
         env.read_env(str(BASE_DIR / ".env"))

      DEBUG = env.bool("DJANGO_DEBUG", False)
      TIME_ZONE = "UTC"
      LANGUAGE_CODE = "en-us"
      SITE_ID = 1
      USE_I18N = True
      USE_TZ = True
      LOCALE_PATHS = [str(BASE_DIR / "locale")]


**BASE_DIR**: Define o diretório base do projeto, resolvendo o caminho absoluto três níveis acima do arquivo atual.

o BASE_DIR referencia o diretório onde está o arquivo manage.py, que é o diretório raiz do projeto.
As referências a outros diretórios são feitas a partir do BASE_DIR.

Por exemplo, APPS_DIR é definido como BASE_DIR / "core", que é o diretório onde os aplicativos principais do projeto estão localizados.

**APPS_DIR**: Define o diretório onde os aplicativos principais do projeto estão localizados.

**env**: Inicializa a instância de variáveis de ambiente usando a biblioteca `environ`.

**READ_DOT_ENV_FILE**: Variável booleana que indica se o arquivo `.env` deve ser lido. O valor padrão é `False`.

**DEBUG**: Define o modo de depuração do Django, baseado na variável de ambiente `DJANGO_DEBUG`. O valor padrão é `False`.

**TIME_ZONE**: Define o fuso horário do projeto. O valor padrão é "UTC".

**LANGUAGE_CODE**: Define o código de idioma padrão do projeto. O valor padrão é "en-us".

**SITE_ID**: Define o ID do site para o framework de sites do Django. O valor padrão é `1`.

**USE_I18N**: Habilita a internacionalização no projeto. O valor padrão é `True`.

**USE_TZ**: Habilita o uso de fusos horários no projeto. O valor padrão é `True`.

**LOCALE_PATHS**: Define os caminhos para os arquivos de localização. Neste caso, aponta para o diretório `locale` dentro do diretório base do projeto.



Configurações de Banco de Dados
-------------------------------

.. code-block:: python

   DATABASES = {"default": env.db("DATABASE_URL")}
   DATABASES["default"]["ATOMIC_REQUESTS"] = True
   DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

**DATABASES**: Define as configurações de banco de dados para o projeto. Neste caso, é definido um dicionário com uma chave "default" que contém as configurações do banco de dados.

**env.db("DATABASE_URL")**: Obtém a URL do banco de dados a partir das variáveis de ambiente usando a função `db` do objeto `env`.

**DATABASES["default"]["ATOMIC_REQUESTS"]**: Define a opção `ATOMIC_REQUESTS` como `True` para habilitar transações atômicas em cada requisição.

**DEFAULT_AUTO_FIELD**: Define o tipo de campo automático padrão para os modelos do Django como `django.db.models.BigAutoField`.

Configurações de URLs
---------------------

Para mais detalhes sobre as rotas da API, consulte a seção `URLs da API <config.html#urls-da-api>`_.

.. code-block:: python

    ROOT_URLCONF = "config.urls"
    WSGI_APPLICATION = "config.wsgi.application"

Aplicativos Instalados
----------------------

.. code-block:: python

   DJANGO_APPS = [
      "django.contrib.auth",
      "django.contrib.contenttypes",
      "django.contrib.sessions",
      "django.contrib.sites",
      "django.contrib.messages",
      "django.contrib.staticfiles",
      "django.contrib.admin",
      "django.forms",
   ]
   THIRD_PARTY_APPS = [
      "crispy_forms",
      "crispy_bootstrap5",
      "rest_framework",
      "rest_framework.authtoken",
      "rest_framework_simplejwt",
      "rest_framework_simplejwt.token_blacklist",
      "django_celery_beat",
      "corsheaders",
      "drf_spectacular",
      "guardian",
   ]
   LOCAL_APPS = [
      "core.users",
   ]
   INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


* - Aplicativos do Django
      - Descrição
   * - ``django.contrib.auth``
      - Para autenticação e autorização.
   * - ``django.contrib.contenttypes``
      - Para gerenciar tipos de conteúdo.
   * - ``django.contrib.sessions``
      - Para gerenciar sessões.
   * - ``django.contrib.sites``
      - Para gerenciar vários sites com Django.
   * - ``django.contrib.messages``
      - Para exibir mensagens aos usuários.
   * - ``django.contrib.staticfiles``
      - Para gerenciar arquivos estáticos.
   * - ``django.contrib.admin``
      - Para o site de administração do Django.
   * - ``django.forms``
      - Para trabalhar com formulários.

   * - Aplicativos de Terceiros
      - Descrição
   * - ``crispy_forms``
      - Para renderizar formulários com estilo.
   * - ``crispy_bootstrap5``
      - Para usar o pacote de modelos do Bootstrap 5 com o crispy forms.
   * - ``rest_framework``
      - Para construir APIs da web.
   * - ``rest_framework.authtoken``
      - Para autenticação baseada em token no Django REST Framework.
   * - ``rest_framework_simplejwt``
      - Para autenticação JSON Web Token (JWT) no Django REST Framework.
   * - ``rest_framework_simplejwt.token_blacklist``
      - Para colocar em lista negra tokens JWT no Django REST Framework.
   * - ``django_celery_beat``
      - Para agendar tarefas periódicas com o Celery.
   * - ``corsheaders``
      - Para lidar com Compartilhamento de Recursos de Origem Cruzada (CORS) no Django.
   * - ``drf_spectacular``
      - Para gerar esquemas OpenAPI para o Django REST Framework.
   * - ``guardian``
      - Para permissões de nível de objeto no Django.

   * - Aplicativos Locais
      - Descrição
   * - ``core.users``
      - Um aplicativo local para gerenciar funcionalidades relacionadas a usuários.

Configurações de Migrações
--------------------------
   .. code-block:: python

      MIGRATION_MODULES = {"sites": "core.contrib.sites.migrations"}

      """
      Esta configuração define o módulo de migrações personalizado para o aplicativo "sites". 
      O valor é um dicionário com uma chave "sites" e o valor é o caminho para o módulo de migrações personalizado.
      Neste caso, o caminho é "core.contrib.sites.migrations".
      """

Configurações de Autenticação
-----------------------------

   .. code-block:: python

      AUTHENTICATION_BACKENDS = [
         "django.contrib.auth.backends.ModelBackend",
         "guardian.backends.ObjectPermissionBackend",
      ]
      AUTH_USER_MODEL = "users.User"
      LOGIN_REDIRECT_URL = "users:redirect"
      LOGIN_URL = "account_login"

   **AUTHENTICATION_BACKENDS**: Define a lista de backends de autenticação utilizados pelo Django. Neste caso, são utilizados dois backends: `django.contrib.auth.backends.ModelBackend` e `guardian.backends.ObjectPermissionBackend`.

   **AUTH_USER_MODEL**: Define o modelo de usuário personalizado utilizado pelo projeto. Neste caso, o modelo de usuário é definido como `users.User`.

   **LOGIN_REDIRECT_URL**: Define a URL para redirecionamento após o login bem-sucedido. Neste caso, a URL definida é `users:redirect`.

   **LOGIN_URL**: Define a URL para a página de login. Neste caso, a URL definida é `account_login`.

Essas configurações são específicas para o lado do backend. Se você estiver construindo um serviço de frontend que consome a API, você precisará implementar essas funcionalidades no lado do frontend também. Isso pode incluir a criação de páginas de login e redirecionamento após o login bem-sucedido no seu aplicativo de frontend.

Configurações de Senhas
-----------------------

.. code-block:: python

    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    ]
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

Configurações de Middleware
---------------------------

.. code-block:: python

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.locale.LocaleMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

Configurações de Arquivos Estáticos
-----------------------------------

.. code-block:: python

    STATIC_ROOT = str(BASE_DIR / "staticfiles")
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [str(APPS_DIR / "static")]
    STATICFILES_FINDERS = [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ]

Configurações de Arquivos de Mídia
----------------------------------

.. code-block:: python

    MEDIA_ROOT = str(APPS_DIR / "media")
    MEDIA_URL = "/media/"

Configurações de Templates
--------------------------

.. code-block:: python

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [str(APPS_DIR / "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]
    FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

Configurações de Fixtures
-------------------------

.. code-block:: python

    FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

Configurações de Segurança
--------------------------

.. code-block:: python

    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True
    X_FRAME_OPTIONS = "DENY"

Configurações de Email
----------------------

.. code-block:: python

    EMAIL_BACKEND = env(
        "DJANGO_EMAIL_BACKEND",
        default="django.core.mail.backends.smtp.EmailBackend",
    )
    EMAIL_TIMEOUT = 5

Configurações de Admin
----------------------

.. code-block:: python

    ADMIN_URL = "admin/"
    ADMINS = [("""juan""", "juan@example.com")]
    MANAGERS = ADMINS

Configurações de Logging
------------------------

.. code-block:: python

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
        },
        "root": {"level": "INFO", "handlers": ["console"]},
    }

Configurações do Celery
-----------------------

.. code-block:: python

    if USE_TZ:
        CELERY_TIMEZONE = TIME_ZONE
    CELERY_BROKER_URL = env("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_RESULT_EXTENDED = True
    CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
    CELERY_RESULT_BACKEND_MAX_RETRIES = 10
    CELERY_ACCEPT_CONTENT = ["json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_TASK_TIME_LIMIT = 5 * 60
    CELERY_TASK_SOFT_TIME_LIMIT = 60
    CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
    CELERY_WORKER_SEND_TASK_EVENTS = True
    CELERY_TASK_SEND_SENT_EVENT = True

Configurações do Django REST Framework
--------------------------------------

.. code-block:: python

   REST_FRAMEWORK = {
      "DEFAULT_AUTHENTICATION_CLASSES": (
         "rest_framework_simplejwt.authentication.JWTAuthentication",
      ),
      "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
   }

Esta configuração define as opções do Django REST Framework.

**DEFAULT_AUTHENTICATION_CLASSES**: Define as classes de autenticação padrão utilizadas pelo Django REST Framework. Neste caso, é utilizada a classe `rest_framework_simplejwt.authentication.JWTAuthentication` para autenticação baseada em JSON Web Token (JWT).

**DEFAULT_SCHEMA_CLASS**: Define a classe de esquema padrão utilizada pelo Django REST Framework para geração de documentação. Neste caso, é utilizada a classe `drf_spectacular.openapi.AutoSchema` para gerar esquemas OpenAPI automaticamente.

Configurações do django-cors-headers
------------------------------------

.. code-block:: python

   CORS_URLS_REGEX = r"^/api/.*$"

Esta configuração define a expressão regular que será usada pelo django-cors-headers para determinar quais URLs devem ter as configurações de CORS aplicadas. Neste caso, a expressão regular é "^/api/.*$", o que significa que todas as URLs que começam com "/api/" terão as configurações de CORS aplicadas.

.. _config-drf-spectacular:

Configurações do drf-spectacular
-------------------------------

.. code-block:: python

   SPECTACULAR_SETTINGS = {
      "TITLE": "core API",
      "DESCRIPTION": "Documentation of API endpoints of core",
      "VERSION": "1.0.0",
      "SCHEMA_PATH_PREFIX": "/api/",
   }

Este trecho de código define as configurações do drf-spectacular para a documentação da API.

- **TITLE**: Define o título da documentação da API como "core API".
- **DESCRIPTION**: Define a descrição da documentação da API como "Documentation of API endpoints of core".
- **VERSION**: Define a versão da documentação da API como "1.0.0".
- **SCHEMA_PATH_PREFIX**: Define o prefixo do caminho do esquema da API como "/api/".

.. code-block:: python

    SPECTACULAR_SETTINGS = {
        "TITLE": "core API",
        "DESCRIPTION": "Documentation of API endpoints of core",
        "VERSION": "1.0.0",
        "SCHEMA_PATH_PREFIX": "/api/",
    }

Este trecho de código define as configurações do drf-spectacular para a documentação da API.

- **TITLE**: Define o título da documentação da API como "core API".
- **DESCRIPTION**: Define a descrição da documentação da API como "Documentation of API endpoints of core".
- **VERSION**: Define a versão da documentação da API como "1.0.0".
- **SCHEMA_PATH_PREFIX**: Define o prefixo do caminho do esquema da API como "/api/".


Configurações do Simple JWT
---------------------------

.. code-block:: python

   from datetime import timedelta

   SIMPLE_JWT = {
      "AUTH_HEADER_TYPES": ("JWT",),
      "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
      "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
      "ROTATE_REFRESH_TOKENS": False,
      "BLACKLIST_AFTER_ROTATION": False,
      "UPDATE_LAST_LOGIN": True,
   }

**AUTH_HEADER_TYPES**: Define os tipos de cabeçalho de autenticação suportados pelo Simple JWT. Neste caso, apenas o tipo "JWT" é suportado.

**ACCESS_TOKEN_LIFETIME**: Define o tempo de vida do token de acesso. Neste caso, é definido como 5 minutos.

**REFRESH_TOKEN_LIFETIME**: Define o tempo de vida do token de atualização. Neste caso, é definido como 1 dia.

**ROTATE_REFRESH_TOKENS**: Define se os tokens de atualização devem ser rotacionados. Neste caso, a rotação de tokens está desativada.

**BLACKLIST_AFTER_ROTATION**: Define se os tokens antigos devem ser colocados em lista negra após a rotação. Neste caso, a lista negra não é ativada.

**UPDATE_LAST_LOGIN**: Define se o último login do usuário deve ser atualizado. Neste caso, o último login é atualizado.

.. automodule:: config.settings.base
   :members:
   :undoc-members:
   :show-inheritance:


Configurações para ambiente de desenvolvimento
===============================================


Configuração do ambiente de Desenvolvimento
-------------------------------------------

**config.settings.local module**

.. _config-settings-local:

.. code-block:: python

   DEBUG = True

   SECRET_KEY = "PtRntYxsahIUOELcd4X9QEsHoS9ZuMJdrgJRCqfBXgQ2PkQaXRCko6xp75Z0nVcT"

   ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

   CACHES = {
      "default": {
         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
         "LOCATION": "",
      }
   }

   EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

   INSTALLED_APPS += ["whitenoise.runserver_nostatic"]

   MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

   DEBUG_TOOLBAR_CONFIG = {
      "SHOW_REDIRECTS": False,
      "SHOW_TEMPLATE_CONTEXT": True,
   }

   INTERNAL_IPS += ["127.0.0.1", "10.0.2.2"]

   INSTALLED_APPS += ["django_extensions"]

   CELERY_TASK_EAGER_PROPAGATES = True

**DEBUG_TOOLBAR_CONFIG**: Define as configurações da barra de ferramentas de depuração do Django. Neste caso, é desabilitado o painel de redirecionamentos e é ativada a exibição do contexto do template.

**INTERNAL_IPS**: Define a lista de IPs internos para os quais a barra de ferramentas de depuração do Django será exibida. Neste caso, são adicionados os IPs "127.0.0.1" e "10.0.2.2".

**INSTALLED_APPS**: Define a lista de aplicativos instalados para o projeto. Neste caso, é adicionado o aplicativo "django_extensions" para fornecer extensões adicionais ao Django.

**CELERY_TASK_EAGER_PROPAGATES**: Define se as tarefas do Celery devem ser propagadas imediatamente. Neste caso, as tarefas do Celery são propagadas imediatamente.

Essas configurações são específicas para o ambiente de desenvolvimento. Certifique-se de ajustar as configurações de acordo com o seu ambiente específico.


Settings para ambiente de produção
===================================

Configuração do ambiente de Produção
------------------------------------
**config.settings.production module**


.. automodule:: config.settings.production
   :members:
   :undoc-members:
   :show-inheritance:

.. code-block:: python

      SECRET_KEY = env("DJANGO_SECRET_KEY")
      ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

      DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

      CACHES = {
         "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": env("REDIS_URL"),
            "OPTIONS": {
                  "CLIENT_CLASS": "django_redis.client.DefaultClient",
                  "IGNORE_EXCEPTIONS": True,
            },
         },
      }

      SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
      SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
      SESSION_COOKIE_SECURE = True
      CSRF_COOKIE_SECURE = True
      SECURE_HSTS_SECONDS = 60
      SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
         "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS",
         default=True,
      )
      SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
      SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
         "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF",
         default=True,
      )

      STORAGES = {
         "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
         },
         "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
         },
      }

      DEFAULT_FROM_EMAIL = env(
         "DJANGO_DEFAULT_FROM_EMAIL",
         default="core <noreply@example.com>",
      )
      SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
      EMAIL_SUBJECT_PREFIX = env(
         "DJANGO_EMAIL_SUBJECT_PREFIX",
         default="[core] ",
      )

      ADMIN_URL = env("DJANGO_ADMIN_URL")

      INSTALLED_APPS += ["anymail"]
      EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
      ANYMAIL = {
         "SENDGRID_API_KEY": env("SENDGRID_API_KEY"),
         "SENDGRID_API_URL": env("SENDGRID_API_URL", default="https://api.sendgrid.com/v3/"),
      }

      LOGGING = {
         "version": 1,
         "disable_existing_loggers": False,
         "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
         "formatters": {
            "verbose": {
                  "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            },
         },
         "handlers": {
            "mail_admins": {
                  "level": "ERROR",
                  "filters": ["require_debug_false"],
                  "class": "django.utils.log.AdminEmailHandler",
            },
            "console": {
                  "level": "DEBUG",
                  "class": "logging.StreamHandler",
                  "formatter": "verbose",
            },
         },
         "root": {"level": "INFO", "handlers": ["console"]},
         "loggers": {
            "django.request": {
                  "handlers": ["mail_admins"],
                  "level": "ERROR",
                  "propagate": True,
            },
            "django.security.DisallowedHost": {
                  "level": "ERROR",
                  "handlers": ["console", "mail_admins"],
                  "propagate": True,
            },
         },
      }

      SPECTACULAR_SETTINGS["SERVERS"] = [
         {"url": "https://example.com", "description": "Production server"},
      ]


**SECRET_KEY**: Define a chave secreta do Django a partir de uma variável de ambiente `DJANGO_SECRET_KEY`.	

**ALLOWED_HOSTS**: Define a lista de hosts permitidos a partir de uma variável de ambiente `DJANGO_ALLOWED_HOSTS`. O valor padrão é `["example.com"]`.

**DATABASES["default"]["CONN_MAX_AGE"]**: Define o tempo máximo de conexão do banco de dados a partir de uma variável de ambiente `CONN_MAX_AGE`. O valor padrão é `60`.

**CACHES**: Define as configurações de cache para o projeto. Neste caso, é utilizado o cache Redis a partir de uma variável de ambiente `REDIS_URL`.

**SECURE_PROXY_SSL_HEADER**: Define o cabeçalho SSL de proxy seguro como `("HTTP_X_FORWARDED_PROTO", "https")`.

**SECURE_SSL_REDIRECT**: Define se o redirecionamento SSL é seguro a partir de uma variável de ambiente `DJANGO_SECURE_SSL_REDIRECT`. O valor padrão é `True`.

**SESSION_COOKIE_SECURE**: Define se o cookie de sessão é seguro.

**CSRF_COOKIE_SECURE**: Define se o cookie CSRF é seguro.

**SECURE_HSTS_SECONDS**: Define o tempo de vida do cabeçalho HSTS.

**SECURE_HSTS_INCLUDE_SUBDOMAINS**: Define se os subdomínios estão incluídos no cabeçalho HSTS.

**SECURE_HSTS_PRELOAD**: Define se o pré-carregamento HSTS está ativado.

**SECURE_CONTENT_TYPE_NOSNIFF**: Define se o tipo de conteúdo é seguro contra sniffing.

**STORAGES**: Define as configurações de armazenamento para o projeto. Neste caso, são definidos os armazenamentos padrão e de arquivos estáticos.

**DEFAULT_FROM_EMAIL**: Define o endereço de e-mail padrão a partir de uma variável de ambiente `DJANGO_DEFAULT_FROM_EMAIL`.

**SERVER_EMAIL**: Define o endereço de e-mail do servidor a partir de uma variável de ambiente `DJANGO_SERVER_EMAIL`.

**EMAIL_SUBJECT_PREFIX**: Define o prefixo do assunto do e-mail a partir de uma variável de ambiente `DJANGO_EMAIL_SUBJECT_PREFIX`.

**ADMIN_URL**: Define a URL do admin do Django a partir de uma variável de ambiente `DJANGO_ADMIN_URL`.

**INSTALLED_APPS**: Adiciona o aplicativo `anymail` à lista de aplicativos instalados.

**EMAIL_BACKEND**: Define o backend de e-mail como `anymail.backends.sendgrid.EmailBackend`.

**ANYMAIL**: Define as configurações do AnyMail, incluindo a chave da API do SendGrid.

**LOGGING**: Define as configurações de logging para o projeto.

**SPECTACULAR_SETTINGS["SERVERS"]**: Define a lista de servidores para a documentação da API.

Essas configurações são específicas para o ambiente de produção. Certifique-se de ajustar as configurações de acordo com o seu ambiente específico.

config.settings.test module
---------------------------

.. automodule:: config.settings.test
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: config.settings
   :members:
   :undoc-members:
   :show-inheritance:
