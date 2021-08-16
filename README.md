# Webapp Rest API application

This is simple webapp using Python Flask module


## Build

    python3 setup.py bdist_wheel

## Install

    python3 install <package-name>
    
    <package-name> - generated Wheel distribution file

## Run the app

    To run from source code root directory

    export FLASK_APP=webapp:myapp
    flask run

    To run using .whl distribution package via Waitress module
    
    waitress-server --call --port=500 "webapp:myapp"

## Run the tests

    Run the command from source code root directory
    
    pytest test_webapp.py

## CI/CD Workflow

* Source Code Checkin to Github
* Github executes Github Actions
  * checkout code
  * run test using Pytest
  * build Wheel distro package
  * deploys file to the target server       

# REST API

The REST API to the webapp is described below.

## Get response from root path

### Request

`GET /`

    curl -i -H 'Accept: application/json' http://localhost:5000/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []

## Get response from health check

`GET /health`

    curl -i -H 'Accept: application/json' http://localhost:5000/health

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []

## Get application metadata

`GET /metadata`

    curl -i -H 'Accept: application/json' http://localhost:5000/metadata

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []
