
# Webapp Rest API application

This is simple webapp using Python Flask module

Dependencies:
* flask
* waitress
* pytest
* pylint
* setuptools

## Build

Generates a Wheel distribution file <b>\<package-name\></b> by running

    python3 setup.py bdist_wheel


## Install

Installs the "webapp" package into the local or virtual environment

    python3 install <package-name>


## Run the app

   Development - Run from source code root directory

    export FLASK_APP=webapp:myapp
    flask run

   Production - Run using .whl distribution package via Waitress module

    waitress-serve --call --port=5000 "webapp:myapp"

## Run the tests

   Run the command from source code root directory

    pytest test_webapp.py

## CI/CD Workflow

* Source code is pushed to Github
* Github executes Github Actions with the following steps
  * checkout code
  * lint code using Pylint
  * run test using Pytest
  * build Wheel distro package
  * deploys file to the target server    
    
* Assumption
  * Build server - local Mac machine via Gtihub action runner
  * Target server - local Mac machine
    
# REST API Requirement

The REST API to the webapp is described below.

## Get response from root path

### Request

`GET /`

    curl -i -H 'Accept: application/json' http://localhost:5000/

### Response

    HTTP/1.1 200 OK
    Content-Length: 95
    Content-Type: application/json
    Date: Mon, 16 Aug 2021 12:04:51 GMT
    Server: waitress

    Hello World!

## Get response from health check

`GET /health`

    curl -i -H 'Accept: application/json' http://localhost:5000/health

### Response

    HTTP/1.1 200 OK
    Content-Length: 95
    Content-Type: application/json
    Date: Mon, 16 Aug 2021 12:04:51 GMT
    Server: waitress

    []

## Get application metadata

`GET /metadata`

    curl -i -H 'Accept: application/json' http://localhost:5000/metadata

### Response

    HTTP/1.1 200 OK
    Content-Length: 95
    Content-Type: application/json
    Date: Mon, 16 Aug 2021 12:04:51 GMT
    Server: waitress

    [{"description":"pre-interview technical test","lastcommitsha":"abc57858585","version":"0.1"}]
