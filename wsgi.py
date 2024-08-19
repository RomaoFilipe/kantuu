import sys
import os

# Define o caminho do projeto
sys.path.insert(0, '/httpdocs')

# Importa a função create_app da app
from app import create_app

# Cria a aplicação usando a factory function
application = create_app()
