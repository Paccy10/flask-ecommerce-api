import os
import sys
from dotenv import load_dotenv

load_dotenv()

env = 'test' if 'pytest' in sys.modules else os.environ.get(
    'PYTHON_ENV', 'development')

environments = {
    'development': {
        'port': 5000,
        'debug': True,
        'swagger-url': '/documentation'
    },
    'test': {
        'port': 3000,
        'debug': False,
        'swagger-url': '/documentation'
    }
}

environment = environments[env]
