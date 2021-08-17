"""System module."""
import subprocess
import json
import flask
from flask import jsonify

def myapp():
    """A dummy docstring."""
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        """A dummy docstring."""
        return "Hello World!"

    @app.route("/health")
    def healthcheck():
        """A dummy docstring."""
        return ""

    @app.route("/metadata")
    def metadata():
        """A dummy docstring."""

        # Git hash info
        gitcmd = "git rev-parse --short HEAD"
        #process = subprocess.Popen(gitcmd.split(), stdout=subprocess.PIPE)
        with subprocess.Popen(gitcmd.split(), stdout=subprocess.PIPE) as process:
            githash, error = process.communicate()
            print(error)

        name="none"
        version = "0000000000"
        description = "no description"
        with open("setup.py", "r") as line:
            if "name" in line:
                name = line.split("=")
                name = name[1].replace("'","").replace(",","")
                #print(name)
            elif "version" in line:
                version = line.split("=")
                version = version[1].replace("'","").replace(",","")
                #print(version)
            elif "description" in line:
                description = line.split("=")
                description = description[1].replace("'","").replace(",","")
                #print(description)
        data = {'description': description.strip(), \
                'version': version.strip(), \
                'lastcommitsha': str(githash,"utf-8")[0:7] }
        fdata = { name.strip() : [ data ]}
        jdata = json.dumps(fdata)

        return jdata

    return app
