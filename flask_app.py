from src import create_app
#import os

#Used to run app locally
#Set env variables using os.environ if needed

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')