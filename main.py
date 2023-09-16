import uvicorn

from web import app

if __name__ == '__main__':
    uvicorn.run(app, host='https://fr-tw.vercel.app/', port=8080)
