import os


__version__ = '1.0.1'

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://root:secret_password@postgres/data')
