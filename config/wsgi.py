# ruff: noqa
"""
Configuração WSGI para o projeto core.

Este módulo contém a aplicação WSGI usada pelo servidor de desenvolvimento do Django
e por qualquer implantação WSGI de produção. Ele deve expor uma variável de nível de módulo
chamada ``application``. Os comandos ``runserver`` e ``runfcgi`` do Django descobrem
esta aplicação através da configuração ``WSGI_APPLICATION``.

Normalmente, você terá a aplicação WSGI padrão do Django aqui, mas também pode fazer sentido
substituir toda a aplicação WSGI do Django por uma personalizada
que posteriormente delega para a aplicação do Django. Por exemplo, você poderia introduzir
middleware WSGI aqui ou combinar uma aplicação Django com uma aplicação de outro
framework.

"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior
# core directory.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "core"))
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()
# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
