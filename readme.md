## Zappa-Flask Lambda Template

* This template is used to build aws lambda api's
* This template is based on python 3.7.x using the Zappa framework to build a flask application as a aws lambda function

### Setup

* Create a python 3.7.x virtual env named `env`
* Install the dependencies located in requirements.txt using `pip install -r requirements.txt`
    * Some other useful libraries (pylint, rope, etc.) are preinstalled as well, if you want to leave them out simple install zappa and flask without using the requirements.txt file
* Modify zappa_settings.json to match your deployment specifications