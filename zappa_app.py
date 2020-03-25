from src import create_app

#Used by Zappa to get WSGI app for deployment
#Set env variables in zappa_settings.json

app = create_app()