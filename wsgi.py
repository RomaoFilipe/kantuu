import sys
import os

# Define o caminho do projeto
sys.path.insert(0, '/httpdocs')

# Se estiver a usar um framework como Flask ou Django
from app import app as application  # para Flask
# ou
# from django.core.wsgi import get_wsgi_application
# os.environ['DJANGO_SETTINGS_MODULE'] = 'seu_projeto.settings'
# application = get_wsgi_application()
