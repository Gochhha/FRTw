import os


__version__ = '1.0.1'

DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://default:C5qV0oYezUSm@ep-blue-salad-48392986.us-east-1.postgres.vercel-storage.com:5432/verceldb')
