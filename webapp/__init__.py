import flask
from flask import jsonify
import subprocess
import json

def myapp():
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        """A dummy docstring."""
        return "Hello World!"

    @app.route("/health", methods=['GET'])
    def healthcheck():
        """A dummy docstring."""
        return ""

    @app.route("/metadata")
    def metadata():
        """A dummy docstring."""

        # Git hash info
        bashCommand = "git rev-parse --short HEAD"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        githash, error = process.communicate()

        f = open("setup.py", "r")
        version = "0000000000"
        description = "no description"
        for x in f:
            if "name" in x:
                name = x.split("=")
                name = name[1].replace("'","").replace(",","")
                print(name)
            elif "version" in x:
                version = x.split("=")
                version = version[1].replace("'","").replace(",","")
                print(version)
            elif "description" in x:
                description = x.split("=")
                description = description[1].replace("'","").replace(",","")
                print(description)

        data = {'description': description.strip(), \
                'version': version.strip(), \
                'lastcommitshaame': str(githash,"utf-8")[0:7] }
        fdata = { name.strip() : [ data ]}
        jdata = json.dumps(fdata)

        return jdata

    return app
